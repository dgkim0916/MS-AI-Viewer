# UI Update Strategy - ui_v1.7.0

## 개요
이 문서는 MS-AI-Viewer의 기술 부채, 성능 병목, 개선 포인트, 그리고 UI 업데이트 전략을 정리합니다. 새로운 UI 버전 개발 시 반드시 유지해야 할 핵심 기능과 변경 가능한 유연한 부분을 구분합니다.

---

## 1. 기술 부채 (Technical Debt)

### 1.1 보안 취약점 (🔴 높음)

#### 1.1.1 하드코딩된 암호화 키
**위치**: [main.py:46](main.py#L46)
```python
KEY = "FBRBdZIbc_ULGN_qOlZjdMLDLPPzdRJ2Nb63kX3wuDI="
```

**문제점**:
- Fernet 암호화 키가 소스코드에 노출
- Git 저장소에 푸시되면 누구나 설정 파일 복호화 가능
- 키 변경 시 모든 설정 파일 재암호화 필요

**개선 방안**:
1. 환경 변수로 키 관리 (`os.getenv("ENCRYPTION_KEY")`)
2. 키 관리 시스템 (KMS) 사용
3. 사용자별 키 파생 (PBKDF2 등)
4. 설정 파일을 OS keyring에 저장

**우선순위**: 🔴 높음 - 즉시 수정 필요

---

#### 1.1.2 하드코딩된 API 키 및 민감 정보
**위치**: [main.py:606-622](main.py#L606)
```python
api_key="NCSV30HGFAONWEPN"
api_secret="KTNWYZVICVQ7XU5AFUZGNC8OQXT9AACT"
pf_id="KA01PF251028000707180RUlDmOmEIHl"
template_id="KA01TP251029053533686cVW9f2fory3"
from_="01084461617"  # TODO: 회사 번호로 변경
```

**문제점**:
- Solapi API 키가 소스코드에 노출
- 발신 전화번호 하드코딩
- Git 저장소에 민감 정보 노출

**개선 방안**:
1. `.env` 파일 + `python-dotenv` 사용
2. 설정 파일에서 로드 (암호화 필수)
3. 빌드 시 환경 변수 주입

**우선순위**: 🔴 높음 - 즉시 수정 필요

---

#### 1.1.3 광범위한 예외 처리 (Bare except)
**위치**: [main.py:362, 1533, 1802, 1810](main.py#L362)
```python
except :  # 예외 타입 미지정
    self.client_ip = "127.0.0.1"
```

**문제점**:
- 모든 예외를 무조건 잡음 (KeyboardInterrupt, SystemExit 포함)
- 디버깅 어려움
- 숨겨진 버그 발생 가능

**개선 방안**:
```python
except (requests.RequestException, socket.error) as e:
    logger.error(f"Failed to get IP: {e}")
    self.client_ip = "127.0.0.1"
```

**우선순위**: 🟡 중간 - 리팩토링 시 수정

---

### 1.2 로깅 및 디버깅 (🟡 중간)

#### 1.2.1 print 문 남용
**통계**: 45개의 `print()` 호출 발견

**문제점**:
- 로그 레벨 조정 불가
- 파일 저장 불가
- 프로덕션 환경에서 성능 저하

**개선 방안**:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info(f"Login attempt from {user_info}")
```

**우선순위**: 🟡 중간 - 유지보수성 향상

---

### 1.3 성능 병목 (🔴 높음)

#### 1.3.1 폴링 방식 알람 체크 (1초마다)
**위치**: [main.py:149-233](main.py#L149)

**문제점**:
```python
while self._is_running:
    for ai_server_ip, ai_server_info in ...:
        alarm_data = requests.get(alarm_url, timeout=1)  # 1초마다 HTTP 요청
    time.sleep(0.1)  # 총 1초 대기
```

- AI 서버마다 1초마다 HTTP 요청
- 서버 5개면 5 RPS (초당 요청 수)
- 네트워크 지연 시 UI 블로킹 가능

**개선 방안**:
1. **WebSocket 방식**으로 전환 (Server Push)
   ```python
   import websockets

   async def listen_alarms():
       async with websockets.connect(f"ws://{ip}:{port}/alarms") as ws:
           async for message in ws:
               alarm_data = json.loads(message)
               self.new_alarm.emit(...)
   ```

2. **Server-Sent Events (SSE)** 사용
3. **롱 폴링 (Long Polling)** 적용 (타임아웃 30초)
4. **Pub/Sub 패턴** (MQTT, Redis)

**우선순위**: 🔴 높음 - 확장성 문제

---

#### 1.3.2 메인 스레드에서 HTTP 요청
**위치**: [main.py:1032](main.py#L1032)
```python
def login_admin_page(self):
    # 메인 UI 스레드에서 동기 HTTP 요청
    receive_data = requests.post(url, json=data, timeout=1).json()
```

**문제점**:
- 네트워크 지연 시 UI 프리징
- 사용자 경험 저하

**개선 방안**:
```python
class ApiRequestThread(QThread):
    finished = Signal(dict)

    def __init__(self, url, data):
        super().__init__()
        self.url = url
        self.data = data

    def run(self):
        response = requests.post(self.url, json=self.data, timeout=5)
        self.finished.emit(response.json())

# 사용
self.api_thread = ApiRequestThread(url, data)
self.api_thread.finished.connect(self.on_response)
self.api_thread.start()
```

**우선순위**: 🟡 중간 - UX 개선

---

#### 1.3.3 GStreamer vs OpenCV 성능
**위치**: [utils.py:50-195](utils.py#L50) (Video_Buffer), [utils.py:196-299](utils.py#L196) (RtspVideoReader)

**현황**:
- `Video_Buffer`: GStreamer 사용 (GPU 가속 가능)
- `RtspVideoReader`: OpenCV 사용 (CPU 기반)

**벤치마크 필요**:
| 방식 | CPU 사용률 | 지연시간 | GPU 지원 |
|------|-----------|---------|----------|
| GStreamer (nvh264dec) | 낮음 | ~200ms | ✅ |
| GStreamer (decodebin) | 중간 | ~300ms | ❌ |
| OpenCV | 높음 | ~500ms | ❌ |

**개선 방안**:
1. NVIDIA GPU 있으면 `nvh264dec` 사용 (현재 주석 처리됨)
2. 해상도를 사용자 설정으로 변경 (현재 640x480 고정)
3. FPS 제한 (현재 15 FPS, 상황별 조정 필요)

**우선순위**: 🟢 낮음 - 현재 충분히 작동

---

### 1.4 코드 품질 (🟡 중간)

#### 1.4.1 중복 코드
**예시**: FadeOutWindow 생성 로직 중복
- [main.py:442-478](main.py#L442) (LoginWindow)
- [main.py:2110-2147](main.py#L2110) (MainWindow)

**개선 방안**:
```python
# utils.py
def show_fade_out_message(parent_window, message):
    if not hasattr(parent_window, 'fadeout_window') or not parent_window.fadeout_window.isVisible():
        parent_window.fadeout_window = FadeOutWindow(parent_window, message)
        # ... 위치 계산 로직 ...
    parent_window.fadeout_window.show()
    parent_window.fadeout_window.raise_()
```

**우선순위**: 🟡 중간 - 유지보수성

---

#### 1.4.2 긴 메서드 (God Method)
**위치**: [main.py:967-1028](main.py#L967) (`setup_slot_connect`)

**문제점**:
- 62줄의 Signal/Slot 연결 코드
- 가독성 저하

**개선 방안**:
```python
def setup_slot_connect(self):
    self._setup_server_slots()
    self._setup_camera_slots()
    self._setup_admin_slots()
    self._setup_menu_slots()

def _setup_server_slots(self):
    self.ui_main.nvr_add_bnt.clicked.connect(self.add_nvr_server)
    # ...
```

**우선순위**: 🟡 중간 - 리팩토링 권장

---

### 1.5 의존성 관리 (🟡 중간)

#### 1.5.1 UI 모듈 (✅ 해결됨)

`ui/` 디렉토리가 프로젝트에 추가되었습니다. 현재 포함된 파일:

| 구분 | 파일 | UI 클래스 |
|------|------|-----------|
| 로그인 | ui_login.py ← login.ui | `Ui_login_windows` |
| 메인 | ui_main.py ← main.ui | `Ui_MainWindow` |
| AI 설정 | ui_ai_setting.py ← ai_setting.ui | `Ui_Ai_Setting_Window` |
| 스케줄 | ui_schedule.py ← schedule.ui | `Ui_schedule_window` |
| 검색 | ui_search.py ← search.ui | `Ui_Search_window` |
| 서버 설정 | ui_server_setting.py ← server_setting.ui | `Ui_server_setting_window` |
| 라벨링 | ui_ai_labeling.py ← ai_labeling.ui | `Ui_labeling_window` |
| 객체 설정 | ui_object_setting.py ← object_setting.ui | `Ui_object_setting` |
| 정보 | ui_info.py ← info.ui | `Ui_Form` |

비즈니스 로직 파일: `utils_ai_setting_window.py`, `utils_schedule_window.py`, `utils_search_window.py`, `utils_labeling_window.py`, `utils_server_setting_window.py`, `utils_object_setting_window.py`

> **주의**: `ui_*.py` 파일은 `.ui` 파일에서 `pyside6-uic`로 자동 생성됩니다. UI 수정은 Qt Designer에서 `.ui` 파일을 편집한 후 재변환해야 합니다.

---

#### 1.5.2 requirements.txt 없음
**문제점**:
- 의존성 관리 어려움
- 배포 환경 재현 불가

**개선 방안**:
```txt
# requirements.txt
PySide6>=6.5.0
opencv-python>=4.8.0
numpy>=1.24.0
requests>=2.31.0
cryptography>=41.0.0
solapi>=1.0.0
PyGObject>=3.46.0  # GStreamer
```

**우선순위**: 🟡 중간 - 배포 편의성

---

## 2. 성능 개선 포인트

### 2.1 메모리 관리 (🟡 중간)

#### 2.1.1 이벤트 리스트 크기 제한 미흡
**위치**: [main.py:220-222](main.py#L220)
```python
# 최근 10개만 유지
self.ai_server_event_alarm_dict[nvr_ip][camera_name] = \
    self.ai_server_event_alarm_dict[nvr_ip][camera_name][:10]
```

**개선 가능**:
- 현재는 카메라당 10개 이벤트만 보관 (적절함)
- 다만 카메라가 100개면 총 1000개 이벤트 메모리에 상주
- 주기적인 가비지 컬렉션 필요 없음 (크기 제한 잘 되어 있음)

**우선순위**: 🟢 낮음 - 현재 충분

---

#### 2.1.2 비디오 프레임 버퍼
**위치**: [utils.py:67](utils.py#L67)
```python
max-buffers=5 drop=true  # GStreamer 설정
```

**현황**:
- 5개 프레임 버퍼링 (약 333ms @ 15 FPS)
- drop=true로 오래된 프레임 자동 폐기

**개선 방안**:
- 네트워크 상태에 따라 동적 조정
- `max-buffers=1`로 최소 지연 (실시간성 중요 시)

**우선순위**: 🟢 낮음 - 현재 적절

---

### 2.2 네트워크 최적화 (🟡 중간)

#### 2.2.1 연결 재사용 (Connection Pooling)
**위치**: [main.py:168](main.py#L168)
```python
alarm_data = requests.get(alarm_url, timeout=1)  # 매번 새 연결
```

**개선 방안**:
```python
# 클래스 초기화 시
self.session = requests.Session()

# 요청 시
alarm_data = self.session.get(alarm_url, timeout=1)
```

**효과**:
- TCP 핸드셰이크 감소
- 지연시간 20-50% 감소

**우선순위**: 🟡 중간 - 성능 개선

**참고**: [main.py:362](main.py#L362)의 Connect_Camera에서는 이미 Session 사용 중 ✅

---

#### 2.2.2 타임아웃 설정 일관성
**현황**:
- CheckAlarmThread: `timeout=1` ([Line 168](main.py#L168))
- login_admin_page: `timeout=1` ([Line 1033](main.py#L1033))
- Connect_Camera: 타임아웃 없음 ([Line 384](main.py#L384))

**개선 방안**:
```python
# config.py
DEFAULT_TIMEOUT = 5
ALARM_TIMEOUT = 2
CAMERA_TIMEOUT = 3
```

**우선순위**: 🟢 낮음 - 현재 작동 중

---

### 2.3 UI 렌더링 최적화 (🟢 낮음)

#### 2.3.1 카메라 프레임 업데이트 빈도
**위치**: [utils.py:332](utils.py#L332)
```python
self.fps = 15  # 15 FPS
```

**현황**: 15 FPS는 모니터링 용도로 적절

**개선 가능**:
- 백그라운드 카메라: 5 FPS
- 포커스된 카메라: 30 FPS
- 동적 FPS 조정

**우선순위**: 🟢 낮음 - 현재 충분

---

## 3. 아키텍처 개선 포인트

### 3.1 레이어 분리 (🟡 중간)

#### 3.1.1 API 통신 레이어 미분리
**현재 구조**:
```
MainWindow
  └─ requests.post(url, ...)  # 직접 호출
```

**개선 방안**:
```python
# api_client.py
class AIServerClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get_alarm_info(self, detect_types):
        url = f"{self.base_url}/get-alarm-info"
        response = self.session.post(url, json={"msg": {"detect_type": detect_types}})
        return response.json()

    def get_camera_plot_data(self, camera_name):
        url = f"{self.base_url}/get-camera-ai-plot-data"
        response = self.session.get(url, json={"msg": camera_name})
        return response.json()

# 사용
api_client = AIServerClient(f"http://{ip}:{port}")
alarm_data = api_client.get_alarm_info(enabled_types)
```

**장점**:
- API 변경 시 한 곳만 수정
- 테스트 용이 (Mock 주입)
- 에러 처리 일관성

**우선순위**: 🟡 중간 - 유지보수성

---

#### 3.1.2 설정 관리 중앙화
**현재 구조**:
```python
# 여러 곳에서 직접 접근
self.ai_server_info_dict["SETTING"]["notice"]["active"]
self.ai_server_info_dict["AI_SERVER"][ip]["port"]
```

**개선 방안**:
```python
# config_manager.py
class ConfigManager:
    def __init__(self, config_file):
        self.config = load_crypography_json(config_file)

    def get_notice_duration(self):
        return self.config["SETTING"]["notice"]["duration"]

    def is_sms_enabled_for(self, phone_num, alarm_type):
        return self.config["SETTING"]["sms"]["user"].get(phone_num, {}).get(alarm_type, False)

    def save(self):
        save_crypography_json(self.config_file, self.config)

# 사용
config = ConfigManager("ai_sever_info.json")
duration = config.get_notice_duration()
```

**우선순위**: 🟡 중간 - 리팩토링 권장

---

### 3.2 상태 관리 (🟡 중간)

#### 3.2.1 중앙 집중식 상태 관리 부재
**현재 구조**:
- 각 위젯이 자체 상태 관리
- `ai_server_info_dict`가 여러 컴포넌트에서 공유

**개선 방안** (Qt MVC 패턴):
```python
# models.py
class AppState(QObject):
    alarm_updated = Signal(dict)
    camera_connected = Signal(str, bool)

    def __init__(self):
        super().__init__()
        self._alarms = []
        self._connected_cameras = set()

    def add_alarm(self, alarm_data):
        self._alarms.append(alarm_data)
        self.alarm_updated.emit(alarm_data)

    def set_camera_status(self, camera_name, connected):
        if connected:
            self._connected_cameras.add(camera_name)
        else:
            self._connected_cameras.discard(camera_name)
        self.camera_connected.emit(camera_name, connected)

# 사용
app_state = AppState()
app_state.alarm_updated.connect(self.on_alarm_updated)
```

**우선순위**: 🟡 중간 - 대규모 리팩토링

---

## 4. 가독성 및 유지보수성

### 4.1 타입 힌팅 (🟢 낮음)

**현재**: 타입 힌팅 전혀 없음

**개선 방안**:
```python
from typing import Dict, List, Optional

def __init__(self, user_info: str, ai_server_info_dict: Dict, client_ip: str) -> None:
    self.ai_server_info_dict: Dict = ai_server_info_dict
    self.client_ip: str = client_ip

def notify(self, title: str, message: str, camera_name: Optional[str] = None,
           alarm_time: Optional[str] = None) -> None:
    pass
```

**장점**:
- IDE 자동완성 향상
- 버그 사전 발견
- 문서화 효과

**우선순위**: 🟢 낮음 - 점진적 적용

---

### 4.2 문서화 (🟢 낮음)

**현재**: Docstring 거의 없음

**개선 방안**:
```python
def connect_camera_page_camera(self, camera_name: Optional[str] = None, tray_notify: bool = False) -> None:
    """
    카메라 페이지에서 선택한 카메라를 연결하고 스트리밍을 시작합니다.

    Args:
        camera_name: 연결할 카메라 이름. None이면 현재 선택된 카메라 사용.
        tray_notify: 트레이 알림에서 호출된 경우 True.

    Returns:
        None

    Raises:
        ValueError: 카메라 이름을 찾을 수 없는 경우

    Example:
        >>> self.connect_camera_page_camera("카메라1")
    """
    pass
```

**우선순위**: 🟢 낮음 - 점진적 적용

---

## 5. 반드시 유지해야 할 핵심 기능

새로운 UI 업데이트 시 다음 기능은 **반드시 유지**해야 합니다:

### 5.1 필수 핵심 기능 (🔴 변경 불가)

#### 5.1.1 실시간 비디오 스트리밍
- **프로토콜**: RTSP over TCP
- **코덱**: H.264
- **해상도**: 640x480 이상 (사용자 설정 가능)
- **지연시간**: 500ms 이하
- **동시 카메라**: 최소 4개 이상

#### 5.1.2 AI 알람 감지 및 알림
- **알람 타입**: 침입, 배회, 쓰러짐, 방화, 싸움, 무단투기
- **알림 방식**: 팝업, SMS, 카카오톡, 이메일
- **알림 설정**: 타입별 활성화/비활성화
- **알림 기록**: 최소 100개 이벤트 저장

#### 5.1.3 다중 NVR/AI 서버 지원
- **NVR**: 동시에 여러 NVR 연결
- **AI 서버**: 여러 AI 서버 모니터링
- **인증**: HTTPBasicAuth 지원
- **설정**: 서버별 독립적인 설정

#### 5.1.4 사용자 인증 및 권한
- **로그인**: ID/PW 기반 인증
- **권한**: admin/일반 사용자 구분
- **암호화**: 설정 파일 암호화 (Fernet 또는 더 강력한 방식)

#### 5.1.5 ROI (Region of Interest) 설정
- **그리기**: 마우스로 폴리곤 ROI 그리기
- **저장**: ROI 설정 저장/로드
- **표시**: 실시간 비디오에 ROI 오버레이

#### 5.1.6 검색 및 라벨링
- **검색**: 날짜/시간/카메라/알람 타입별 검색
- **라벨링**: 이벤트 라벨링 기능
- **재생**: 과거 이벤트 재생

---

### 5.2 유지하되 개선 가능 (🟡 변경 가능)

#### 5.2.1 UI 프레임워크
- **현재**: PySide6 (Qt for Python)
- **대안**: PyQt6, Tkinter, Kivy, Web 기반 (Electron + React)
- **권장**: PySide6 유지 (안정성, 네이티브 성능)

#### 5.2.2 비디오 처리 백엔드
- **현재**: GStreamer
- **대안**: FFmpeg, OpenCV, VLC
- **권장**: GStreamer 유지 (GPU 가속, 낮은 지연)

#### 5.2.3 설정 저장 방식
- **현재**: JSON (Fernet 암호화)
- **대안**: SQLite, YAML, TOML, OS Keyring
- **권장**: SQLite + OS Keyring (구조화된 데이터, 보안 향상)

#### 5.2.4 알람 수신 방식
- **현재**: 폴링 (1초마다 HTTP 요청)
- **대안**: WebSocket, SSE, MQTT, Redis Pub/Sub
- **권장**: WebSocket (실시간, 낮은 오버헤드)

#### 5.2.5 로깅 시스템
- **현재**: print 문
- **대안**: logging 모듈, structlog, loguru
- **권장**: Python logging + 파일 로테이션

---

### 5.3 완전히 변경 가능 (🟢 자유롭게 변경)

#### 5.3.1 UI 레이아웃
- 현재 레이아웃은 참고용
- 사용자 경험(UX) 개선 자유롭게 진행
- 다크 모드, 테마 커스터마이징 추가 가능

#### 5.3.2 알림 UI
- **현재**: CustomNotification (커스텀 위젯)
- **대안**: OS 네이티브 알림, 시스템 트레이 알림
- **개선**: 알림 그룹화, 스와이프 제스처

#### 5.3.3 설정 UI
- **현재**: 여러 별도 창 (AI 설정, 스케줄, 객체 설정 등)
- **대안**: 통합 설정 패널, 탭 기반 UI
- **개선**: 설정 검색, 즉시 적용

#### 5.3.4 카메라 그리드 레이아웃
- **현재**: 고정 그리드
- **개선**: 드래그 앤 드롭, 크기 조정, 전체 화면

---

## 6. 업데이트 우선순위 로드맵

### Phase 1: 긴급 수정 (1-2주)
1. ✅ **보안 수정**
   - 암호화 키를 환경 변수로 이동
   - API 키를 설정 파일로 이동
   - Bare except 제거

2. ✅ **UI 모듈 복구 완료**
   - `ui/` 디렉토리 추가됨 (.ui 파일 10개, ui_*.py 9개, utils_*.py 6개)
   - Qt Designer 원본 파일 및 자동 생성 Python 코드 포함

3. ✅ **의존성 문서화**
   - `requirements.txt` 작성
   - 설치 가이드 업데이트

---

### Phase 2: 성능 개선 (2-4주)
1. ✅ **로깅 시스템 도입**
   - print → logging 변환
   - 로그 레벨 설정 (DEBUG, INFO, WARNING, ERROR)
   - 파일 로그 저장

2. ✅ **WebSocket 방식 알람 수신**
   - CheckAlarmThread를 WebSocket 클라이언트로 전환
   - 폴링 방식 제거
   - AI 서버 WebSocket 엔드포인트 구현 필요

3. ✅ **Connection Pooling**
   - requests.Session 일관성 있게 사용
   - 타임아웃 설정 중앙화

---

### Phase 3: 아키텍처 개선 (4-8주)
1. ✅ **API 통신 레이어 분리**
   - `AIServerClient`, `NVRClient` 클래스 구현
   - 에러 처리 일관성

2. ✅ **설정 관리 중앙화**
   - `ConfigManager` 클래스 구현
   - 타입 안전성 보장

3. ✅ **상태 관리 개선**
   - `AppState` 클래스 구현 (Qt Signal 기반)
   - 위젯 간 의존성 감소

---

### Phase 4: 코드 품질 (8-12주)
1. ✅ **타입 힌팅 추가**
   - 모든 함수/메서드에 타입 힌트
   - mypy로 타입 체크

2. ✅ **문서화**
   - Docstring 추가
   - Sphinx로 API 문서 생성

3. ✅ **테스트 코드 작성**
   - pytest 도입
   - 핵심 로직 유닛 테스트
   - Integration 테스트

---

### Phase 5: 차세대 UI (12주+)
1. ✅ **Web 기반 UI 검토**
   - Electron + React/Vue 평가
   - 크로스 플랫폼 지원
   - 원격 접속 용이

2. ✅ **모바일 앱**
   - Flutter/React Native
   - Push 알림
   - 외부 접속

---

## 7. 마이그레이션 전략

### 7.1 점진적 마이그레이션 (권장)

```
v1.7.0 (현재)
    ↓
v1.8.0 (Phase 1-2: 보안 + 성능)
    ↓
v2.0.0 (Phase 3-4: 아키텍처 개선)
    ↓
v3.0.0 (Phase 5: 차세대 UI)
```

**장점**:
- 각 버전마다 배포 및 테스트
- 사용자 피드백 반영
- 위험 분산

---

### 7.2 Big Bang 마이그레이션 (비권장)

**장점**:
- 깔끔한 재시작
- 기술 부채 완전 제거

**단점**:
- 높은 위험
- 긴 개발 기간 (6개월+)
- 사용자 불편

---

## 8. 기술 스택 권장 사항

### 8.1 현재 스택 유지 (v2.0까지)
```
- UI: PySide6
- 비디오: GStreamer
- 네트워크: requests + WebSocket
- 데이터: JSON → SQLite
- 보안: Fernet → AES-GCM + OS Keyring
```

### 8.2 차세대 스택 (v3.0+)
```
- UI: Electron + React/TypeScript
- 비디오: WebRTC + MSE
- 백엔드: FastAPI (Python) 또는 Node.js
- 데이터: PostgreSQL
- 알림: WebSocket + Push Notification
```

---

## 9. 체크리스트

### 업데이트 전 확인 사항
- [ ] 모든 핵심 기능 동작 확인 (섹션 5.1)
- [ ] 설정 파일 백업
- [ ] 기존 사용자 데이터 마이그레이션 계획
- [ ] 롤백 계획 수립

### 업데이트 후 확인 사항
- [ ] 모든 카메라 연결 테스트
- [ ] 알람 발생 및 알림 테스트
- [ ] 설정 저장/로드 테스트
- [ ] 성능 벤치마크 (CPU, 메모리, 네트워크)
- [ ] 보안 테스트 (암호화, 인증)

---

## 10. 결론

### 즉시 수정 필요 (🔴)
1. 하드코딩된 암호화 키 및 API 키 제거
2. ~~누락된 UI 모듈 복구~~ → ✅ 완료 (`ui/` 디렉토리 추가됨)
3. WebSocket 방식 알람 수신 (폴링 제거)

### 리팩토링 권장 (🟡)
1. 로깅 시스템 도입
2. API 통신 레이어 분리
3. 설정 관리 중앙화
4. 메인 스레드 HTTP 요청 비동기화

### 장기 개선 (🟢)
1. 타입 힌팅 및 문서화
2. 테스트 코드 작성
3. 차세대 UI (Web 기반)

### 유지해야 할 핵심
- 실시간 비디오 스트리밍 (RTSP)
- AI 알람 감지 및 알림
- 다중 NVR/AI 서버 지원
- ROI 설정 및 검색 기능

---

**다음 단계**: Phase 1 (긴급 수정)부터 시작하여 점진적으로 개선하는 것을 권장합니다.
