# UI Structure Overview - ui_v1.7.0

## 프로젝트 개요
MS-AI-Viewer는 PySide6(Qt for Python) 기반의 AI 영상 감시 시스템 데스크톱 애플리케이션입니다. NVR(Network Video Recorder)과 AI 서버를 연동하여 실시간 영상 모니터링 및 이벤트 감지 기능을 제공합니다.

## 프로젝트 타입
- **UI 프레임워크**: PySide6 (Qt for Python)
- **애플리케이션 타입**: 데스크톱 GUI 애플리케이션
- **언어**: Python 3.x

## 주요 의존성 (Dependencies)

### 핵심 UI 라이브러리
```python
PySide6              # Qt GUI 프레임워크 (QtWidgets, QtGui, QtCore)
```

### 비디오 처리
```python
gi.repository.Gst    # GStreamer - 실시간 비디오 스트리밍 (RTSP)
opencv-python (cv2)  # 이미지/비디오 처리
numpy                # 배열 및 수치 연산
```

### 네트워크 및 통신
```python
requests             # HTTP 통신 (NVR/AI 서버와 REST API 연동)
socket               # 소켓 통신
```

### 보안 및 암호화
```python
cryptography.Fernet  # 설정 파일 암호화/복호화
```

### 메시징 및 알림
```python
solapi               # SMS/카카오톡 알림 서비스
smtplib              # 이메일 전송
```

### 기타
```python
threading            # 멀티스레딩
json                 # JSON 데이터 처리
base64               # Base64 인코딩
```

## 프로젝트 폴더 구조

```
ui_v1.7.0/
├── main.py                      # 메인 애플리케이션 엔트리 포인트 (2299 lines)
├── utils.py                     # 유틸리티 함수 및 클래스 모음
├── video_read_gtstreamer.py     # GStreamer 비디오 처리 (추가)
├── resourece_rc.py              # Qt 리소스 파일 (컴파일된 QRC)
├── resourece.qrc                # Qt 리소스 정의 파일
├── ai_sever_info.json           # AI 서버 설정 (암호화됨)
├── ai_sever_info_init.json      # AI 서버 초기 설정
├── crypto_json.py               # JSON 암호화 유틸리티
├── uncrypto_json.py             # JSON 복호화 유틸리티
├── test.py                      # 테스트 스크립트
├── main.spec                    # PyInstaller 빌드 설정
├── install.sh                   # 설치 스크립트
├── main.sh                      # 실행 스크립트
├── LICENSE                      # 라이선스 파일
└── README.md                    # 프로젝트 설명

ui/                                  # UI 모듈 디렉토리
├── __init __.py                     # 모듈 초기화 (ms_ai_img_rc, Ui_Dialog, Ui_MainWindow import)
├── Qt Designer UI 정의 파일 (.ui)
│   ├── login.ui                     # 로그인 다이얼로그 (19KB)
│   ├── main.ui                      # 메인 윈도우 (343KB)
│   ├── ai_setting.ui                # AI 설정 (66KB)
│   ├── schedule.ui                  # 스케줄 설정 (85KB)
│   ├── search.ui                    # 이벤트 검색 (136KB)
│   ├── server_setting.ui            # 서버 설정 (100KB)
│   ├── ai_labeling.ui               # AI 라벨링 (33KB)
│   ├── object_setting.ui            # 객체 설정 (25KB)
│   ├── search_backup.ui             # 검색 백업 (42KB)
│   └── info.ui                      # 정보 다이얼로그 (1KB)
├── 자동 생성 UI Python 파일 (ui_*.py) - pyside6-uic로 생성, 수동 편집 금지
│   ├── ui_login.py                  # Ui_login_windows (12KB)
│   ├── ui_main.py                   # Ui_MainWindow (195KB)
│   ├── ui_ai_setting.py             # Ui_Ai_Setting_Window (45KB)
│   ├── ui_schedule.py               # Ui_schedule_window (61KB)
│   ├── ui_search.py                 # Ui_Search_window (81KB)
│   ├── ui_server_setting.py         # Ui_server_setting_window (69KB)
│   ├── ui_ai_labeling.py            # Ui_labeling_window (26KB)
│   ├── ui_object_setting.py         # Ui_object_setting (20KB)
│   └── ui_info.py                   # Ui_Form (2KB)
├── 비즈니스 로직 구현 파일 (utils_*.py)
│   ├── utils_ai_setting_window.py   # AI 설정 창 로직 (23KB)
│   │   └── 클래스: Ai_setting_page_view(QLabel)
│   │   └── 함수: open_ai_setting_window(click, self)
│   ├── utils_schedule_window.py     # 스케줄 설정 창 로직 (21KB)
│   │   └── 클래스: SchedulePageView(QLabel), ScheduleDialog(QDialog)
│   │   └── 함수: open_schedule_window(click, self)
│   ├── utils_search_window.py       # 검색 창 로직 (46KB)
│   │   └── 클래스: SearchPageViewer(QLabel), SearchDialog(QDialog)
│   │   └── 함수: open_search_window(click, self)
│   ├── utils_labeling_window.py     # 라벨링 창 로직 (38KB)
│   │   └── 클래스: Labeling_Viewer(QLabel), LabelingDialog(QDialog)
│   │   └── 함수: open_labeling_window(click, self)
│   ├── utils_server_setting_window.py  # 서버 설정 창 로직 (20KB)
│   │   └── 함수: open_server_setting_window(click, self)
│   └── utils_object_setting_window.py  # 객체 설정 창 로직 (5KB)
│       └── 클래스: Object_settint_Dialog(QDialog)
│       └── 함수: open_object_setting_window(click, self)
└── images/                          # UI 이미지 에셋 (57개 파일)
    ├── SVG 아이콘 (24개)             # ico_setting.svg, ico_camera.svg 등
    ├── PNG 이미지 (28개)             # 버튼, 로고, 배경 이미지
    ├── JPG 이미지 (2개)              # checkm.jpg, main_bg2.jpg
    └── ICO 파일 (1개)               # icon2.ico (애플리케이션 아이콘)
```

> **참고**: `ui_*.py` 파일은 Qt Designer `.ui` 파일에서 `pyside6-uic`로 자동 생성됩니다. UI 수정 시 `.ui` 파일을 Qt Designer에서 편집한 후 재변환해야 합니다.

## 메인 엔트리 파일 분석

### [main.py](main.py) (2299 lines)

#### 주요 클래스 구조

```python
# 백그라운드 스레드
class UpdateCameraImageThread(QThread)     # Line 79
    - 카메라 이미지를 백그라운드에서 주기적으로 업데이트
    - NVR에서 HTTP 요청으로 이미지 가져오기
    - Signal: finished(dict)

class CheckAlarmThread(QThread)            # Line 137
    - AI 서버에서 알람 이벤트 체크
    - 백그라운드에서 주기적으로 폴링
    - Signal: finished(dict)

# 메인 UI 윈도우
class LoginWindow(QDialog)                 # Line 351
    - Ui_login_windows 상속
    - 로그인 인증 처리
    - 서버 연결 확인

class MainWindow(QMainWindow)              # Line 480
    - Ui_MainWindow 상속
    - 메인 애플리케이션 윈도우
    - 카메라 뷰어, 알람 관리, 설정 등 모든 기능 통합
```

#### 핵심 기능 모듈

```python
# 전역 상수
NOTICE_DURATION = {0: 3000, 1: 5000, 2: 10000, 3: 60000, 4: -1}
ALARM_TYPE_DIC = {
    2: "침입",
    1: "배회",
    6: "쓰러짐",
    4: "방화",
    7: "싸움",
    5: "무단투기"
}

# 암호화 함수
load_crypography_json(info_filename)       # JSON 복호화 및 로드
save_crypography_json(filename, info)      # JSON 암호화 및 저장
KEY = "FBRBdZIbc_ULGN_qOlZjdMLDLPPzdRJ2Nb63kX3wuDI="  # Fernet 키
```

### [utils.py](utils.py)

#### 주요 클래스

```python
class Video_Buffer:                        # Line 50
    - GStreamer 기반 RTSP 비디오 스트리밍
    - 실시간 프레임 버퍼링
    - 연결 상태 관리 및 자동 재연결
    - 해상도 조정 및 FPS 제어

    주요 메서드:
    - start_gst(config): GStreamer 파이프라인 시작
    - gst_to_opencv(sample): GStreamer 샘플을 OpenCV 배열로 변환
    - read(): 현재 프레임 읽기
    - on_message(bus, message): GStreamer 메시지 처리 (에러, EOS)
```

#### 기타 클래스 및 유틸리티 함수

```python
# 클래스
class RtspVideoReader:                    # Line 196 - OpenCV 기반 RTSP 비디오 리더
class Connect_Camera(QThread):            # Line 300 - 카메라 연결 및 AI 오버레이 스레드
class Connect_Playback(QThread):          # Line 420 - 녹화 재생 스레드
class Plot_Camera_Viewer(QLabel):         # Line 478 - ROI 그리기 지원 카메라 뷰어
class FadeOutWindow(QWidget):             # Line 575 - 페이드아웃 메시지 위젯
class FadeOutInWindow(QWidget):           # Line 617 - 페이드인/아웃 메시지 위젯
class CustomNotification(QWidget):        # Line 927 - 알림 팝업 위젯
class NotificationManager(QObject):       # Line 1181 - 알림 관리자

# 함수
plot_one_box(x, img, ...)                 # Line 668 - 바운딩 박스 그리기
draw_roi(points, image, ...)              # Line 682 - ROI 폴리곤 그리기
TF_detect_area(detect_info, img_size)     # Line 686 - 감지 영역 변환
TF_bbox(bbox, ori_imsz, target_imsz)      # Line 713 - 바운딩 박스 좌표 변환
plot_detect_info(img, detect_info, ...)   # Line 759 - 감지 정보 시각화
load_info(host, port, file_name)          # Line 842 - 서버에서 설정 로드
save_info(host, port, file_name, info)    # Line 860 - 서버에 설정 저장
Eng2kor(eng)                              # Line 866 - 영문→한글 변환
Kor2eng(kor)                              # Line 875 - 한글→영문 변환
get_datetime_from_path(path)              # Line 888 - 경로에서 날짜 추출
get_datetime_from_list(list)              # Line 897 - 리스트에서 날짜 추출
print_error(e)                            # Line 903 - 에러 출력
check_nvidia_gpu()                        # Line 908 - NVIDIA GPU 확인
```

## 상태 관리

이 애플리케이션은 **중앙 집중식 상태 관리 라이브러리를 사용하지 않습니다**. 대신:

- **Qt Signal/Slot 메커니즘**: 컴포넌트 간 통신
- **QThread + Signal**: 백그라운드 작업 및 UI 업데이트
- **JSON 파일 기반 영구 저장**: 설정 및 서버 정보
- **클래스 인스턴스 변수**: 로컬 상태 관리

## 데이터 저장소

### 설정 파일
- `ai_sever_info.json`: 암호화된 AI 서버 및 NVR 설정
  - NVR IP, 인증 정보
  - AI 서버 엔드포인트
  - 카메라 설정
- `ai_sever_info_init.json`: 초기 설정 템플릿

### 암호화 방식
- **알고리즘**: Fernet (대칭 키 암호화)
- **키**: 하드코딩된 base64 문자열
- **용도**: 민감한 설정 정보 보호

## 비디오 스트리밍 아키텍처

```
RTSP 소스 (NVR)
    ↓
GStreamer Pipeline (rtspsrc → rtph264depay → h264parse → decodebin)
    ↓
Video Buffer (frame buffering, connection monitoring)
    ↓
OpenCV 배열 변환
    ↓
Qt QLabel/QPixmap (UI 렌더링)
```

**주요 특징**:
- **프로토콜**: RTSP over TCP
- **코덱**: H.264
- **버퍼 모드**: Leaky downstream (max 5-10 buffers)
- **동기화**: sync=false (낮은 지연시간)
- **자동 재연결**: 연결 끊김 시 자동 복구

## 네트워크 통신 구조

### NVR 연동
- **프로토콜**: HTTP(S) + RTSP
- **인증**: HTTPBasicAuth
- **용도**:
  - 카메라 이미지 스냅샷 가져오기
  - 실시간 비디오 스트림 (RTSP)

### AI 서버 연동
- **프로토콜**: HTTP REST API
- **데이터 형식**: JSON
- **주요 API** (추정):
  - 알람 이벤트 조회
  - AI 모델 설정
  - 객체 감지 결과 수신

## 멀티스레딩 구조

```
Main UI Thread (QMainWindow)
    │
    ├─ UpdateCameraImageThread (주기적 카메라 이미지 업데이트)
    │   └─ Signal: finished(dict) → UI 업데이트
    │
    ├─ CheckAlarmThread (주기적 알람 체크)
    │   └─ Signal: finished(dict) → 알람 처리
    │
    └─ Video_Buffer (각 카메라마다 GStreamer 스레드)
        └─ GStreamer Bus Message 처리
```

## 핵심 기능

1. **사용자 인증**: LoginWindow를 통한 로그인
2. **멀티 카메라 뷰어**: 여러 NVR 카메라 동시 모니터링
3. **실시간 AI 알람**:
   - 침입, 배회, 쓰러짐, 방화, 싸움, 무단투기 감지
   - 알림 지속 시간 설정 가능
4. **알림 시스템**:
   - 팝업 알림 (FadeOutWindow)
   - SMS/카카오톡 (solapi)
   - 이메일 (SMTP)
5. **설정 관리**:
   - AI 설정 (utils_ai_setting_window)
   - 스케줄 설정 (utils_schedule_window)
   - 객체 감지 설정 (utils_object_setting_window)
   - 서버 설정 (utils_server_setting_window)
6. **검색 및 라벨링**:
   - 이벤트 검색 (utils_search_window)
   - 데이터 라벨링 (utils_labeling_window)

## 빌드 및 배포

- **빌드 도구**: PyInstaller (main.spec)
- **타겟 플랫폼**: Windows (README.md 기준)
- **패키징**: 단일 실행 파일 생성 가능

## 시스템 요구사항

### 필수 패키지 (conda)
```bash
conda install conda-forge::pygobject
conda install conda-forge::cryptography
conda install conda-forge::pyside6
conda install conda-forge::gst-plugins-base
conda install conda-forge::gst-plugins-good
conda install conda-forge::gst-plugins-bad
pip install opencv-python numpy
```

### 선택 사항
- NVIDIA GPU (check_nvidia_gpu 함수 존재)
- 하드웨어 가속 디코딩 지원 (nvh264dec - 주석 처리됨)

## 보안 고려사항

⚠️ **보안 취약점**:
1. **하드코딩된 암호화 키**: Fernet 키가 소스코드에 노출
2. **평문 인증 정보**: HTTPBasicAuth 사용 (HTTPS 필수)
3. **입력 검증 부족**: SQL Injection, XSS 등 검증 필요 (API 연동 부분)

## 다음 단계

이 문서를 기반으로:
1. **컴포넌트 간 데이터 흐름 및 의존성 맵** → UI_COMPONENT_MAP.md 참조
2. **기술 부채 및 개선 포인트** → UI_UPDATE_STRATEGY.md 참조
3. **ui/ 모듈 코드 품질 개선**: 타입 힌팅, 문서화, 중복 코드 제거
