# Phase 1 Handoff 문서 - 긴급 수정

## 개요

이 문서는 `UI_UPDATE_STRATEGY.md`의 Phase 1(긴급 수정) 항목을 실행하기 위한 인수인계 문서입니다.
현재 코드베이스 분석 결과를 기반으로 구체적인 작업 명세, 의사결정 사항, 코드 변경 범위를 정리합니다.

**대상 프로젝트**: MS-AI-Viewer v1.7.0
**배포 방식**: PyInstaller (`main.spec`) 기반 데스크톱 배포
**실행 환경**: Linux (Ubuntu), Python 3.x, conda 환경

---

## 확정된 의사결정

| 항목 | 결정 | 근거 |
|------|------|------|
| 환경변수 관리 | `python-dotenv` + `override=False` | OS 환경변수 우선순위 확보, 개발/배포 유연성 |
| `.env` 파일 관리 | 배포 담당자/자동화 스크립트 관리 | PyInstaller 번들 내부 주입 금지 (보안/유연성) |
| 마이그레이션 | 스크립트 제작, 배포 프로세스에 포함 | 기존 암호화 데이터 보존 |
| Solapi API 키 | `.env` 파일로 분리 | 암호화 키와 동일 레벨 보안 적용 |
| 발신번호 | `.env` 파일로 분리 | 현장별 다른 번호 사용 가능 |
| 의존성 관리 | pip 기반 `requirements.txt` 작성 | conda 환경 내에서도 pip 호환, PyInstaller 빌드 기준 |
| Python 버전 | `>=3.10` 명시 | PySide6 최소 요구사항 |
| bare except 처리 | 구체적 예외 타입으로 변경 | 아래 상세 명세 참조 |

---

## 작업 1: 보안 수정

### 1-1. python-dotenv 도입 및 환경변수 이관

#### 설치

```bash
pip install python-dotenv
```

#### .env.example 파일 생성 (프로젝트 루트)

배포 시 참고용 템플릿. 실제 `.env`는 `.gitignore`에 추가합니다.

```env
# === 암호화 ===
MS_AI_ENCRYPTION_KEY=FBRBdZIbc_ULGN_qOlZjdMLDLPPzdRJ2Nb63kX3wuDI=

# === Solapi SMS/카카오톡 ===
SOLAPI_API_KEY=NCSV30HGFAONWEPN
SOLAPI_API_SECRET=KTNWYZVICVQ7XU5AFUZGNC8OQXT9AACT
SOLAPI_KAKAO_PF_ID=KA01PF251028000707180RUlDmOmEIHl
SOLAPI_KAKAO_TEMPLATE_ID=KA01TP251029053533686cVW9f2fory3
SOLAPI_SENDER_NUMBER=01084461617
```

#### main.py 수정 범위

**파일 상단 (Line 1~46 부근)**

현재:
```python
from cryptography.fernet import Fernet

KEY = "FBRBdZIbc_ULGN_qOlZjdMLDLPPzdRJ2Nb63kX3wuDI="
```

변경:
```python
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# .env 파일 로드 (OS 환경변수가 우선)
# PyInstaller 빌드 시 실행 파일과 같은 디렉토리의 .env를 탐색
if getattr(sys, 'frozen', False):
    _base_dir = os.path.dirname(sys.executable)
else:
    _base_dir = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(_base_dir, '.env'), override=False)

KEY = os.environ.get("MS_AI_ENCRYPTION_KEY")
if KEY is None:
    raise RuntimeError("MS_AI_ENCRYPTION_KEY 환경변수가 설정되지 않았습니다. .env 파일을 확인하세요.")
```

> **PyInstaller 호환 포인트**: `sys.frozen` 체크로 빌드 실행 시 `.exe` 위치 기준으로 `.env`를 탐색합니다. `.env` 파일은 빌드 산출물(dist/MS-AI/) 디렉토리에 배포 담당자가 배치합니다.

**Solapi 호출 부분 (Line 599~631 부근)**

현재:
```python
message_service = SolapiMessageService(
    api_key="NCSV30HGFAONWEPN", api_secret="KTNWYZVICVQ7XU5AFUZGNC8OQXT9AACT"
)
kakao_option = KakaoOption(
    pf_id="KA01PF251028000707180RUlDmOmEIHl",
    template_id="KA01TP251029053533686cVW9f2fory3",
    ...
)
message = RequestMessage(
    from_="01084461617",
    ...
)
```

변경:
```python
message_service = SolapiMessageService(
    api_key=os.environ.get("SOLAPI_API_KEY", ""),
    api_secret=os.environ.get("SOLAPI_API_SECRET", "")
)
kakao_option = KakaoOption(
    pf_id=os.environ.get("SOLAPI_KAKAO_PF_ID", ""),
    template_id=os.environ.get("SOLAPI_KAKAO_TEMPLATE_ID", ""),
    variables={
        "#{detect_type}": str(ai_type),
        "#{camare_name}": str(camera_name),
        "#{current_time}": str(current_time)
    }
)
message = RequestMessage(
    from_=os.environ.get("SOLAPI_SENDER_NUMBER", ""),
    to=phone_num,
    kakao_options=kakao_option,
)
```

#### crypto_json.py, uncrypto_json.py 수정 범위

이 두 파일은 유틸리티 스크립트(수동 암/복호화)입니다. 동일하게 `dotenv` 적용합니다.

현재 (양쪽 공통):
```python
KEY = "FBRBdZIbc_ULGN_qOlZjdMLDLPPzdRJ2Nb63kX3wuDI="
```

변경:
```python
import os
from dotenv import load_dotenv

load_dotenv(override=False)
KEY = os.environ.get("MS_AI_ENCRYPTION_KEY")
if KEY is None:
    raise RuntimeError("MS_AI_ENCRYPTION_KEY 환경변수가 설정되지 않았습니다.")
```

---

### 1-2. Bare except 제거

4곳 모두 구체적 예외 타입으로 교체합니다.

#### (1) Line 362 - IP 조회 실패

```python
# 현재
except :
    self.client_ip = "127.0.0.1"
    self.local_ip = "127.0.0.1"
```

```python
# 변경
except (requests.RequestException, socket.error, OSError) as e:
    print_error(e)
    self.client_ip = "127.0.0.1"
    self.local_ip = "127.0.0.1"
```

**근거**: `requests.get()` → `requests.RequestException`, `socket.connect()` → `socket.error`/`OSError`. 네트워크 미연결 시 정상적으로 폴백해야 하는 의도된 동작입니다.

#### (2) Line 1533 - 카메라 뷰어 리셋

```python
# 현재
try:
    self.ui_main.camera_page_viewer.reset()
except :
    pass
```

```python
# 변경
try:
    self.ui_main.camera_page_viewer.reset()
except (AttributeError, RuntimeError):
    pass
```

**근거**: `camera_page_viewer`가 초기화 전이면 `AttributeError`, Qt 위젯 삭제 후 접근이면 `RuntimeError`. 둘 다 무시해도 안전한 상황입니다.

#### (3) Line 1802 - NVR 이름 조회

```python
# 현재
try:
    item4 = QTableWidgetItem(self.ai_server_info_dict["NVR"][nvr_ip]["name"])
    item4.setTextAlignment(Qt.AlignCenter)
except:
    item4 = QTableWidgetItem("알 수 없음")
    item4.setTextAlignment(Qt.AlignCenter)
```

```python
# 변경
except (KeyError, TypeError):
    item4 = QTableWidgetItem("알 수 없음")
    item4.setTextAlignment(Qt.AlignCenter)
```

**근거**: 딕셔너리 키 부재 시 `KeyError`, 값이 `None`일 때 `TypeError`.

#### (4) Line 1810 - NVR IP 표시

```python
# 현재
try:
    item5 = QTableWidgetItem(nvr_ip)
    item5.setTextAlignment(Qt.AlignCenter)
except:
    item5 = QTableWidgetItem("알 수 없음")
    item5.setTextAlignment(Qt.AlignCenter)
```

```python
# 변경
except (TypeError, ValueError):
    item5 = QTableWidgetItem("알 수 없음")
    item5.setTextAlignment(Qt.AlignCenter)
```

**근거**: `nvr_ip`가 `None`이면 `TypeError`. `QTableWidgetItem`에 부적절한 값이면 `ValueError`.

---

### 1-3. 마이그레이션 스크립트

기존에 하드코딩된 키로 암호화된 `ai_sever_info.json`을 새 키(환경변수 기반)로 재암호화하는 스크립트입니다. 배포 프로세스에 1회 실행 단계로 포함합니다.

#### 파일: `migrate_encryption_key.py` (신규 생성)

```python
"""
마이그레이션 스크립트: 하드코딩 키 → 환경변수 키 전환

사용법:
  1. .env 파일에 새 MS_AI_ENCRYPTION_KEY 설정
  2. python migrate_encryption_key.py

동작:
  - 기존 키로 ai_sever_info.json 복호화
  - 새 키로 재암호화
  - 원본 백업 후 교체
"""
import os
import sys
import json
import shutil
from datetime import datetime
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv(override=False)

# 기존 하드코딩 키 (마이그레이션 전용, 이후 제거)
OLD_KEY = "FBRBdZIbc_ULGN_qOlZjdMLDLPPzdRJ2Nb63kX3wuDI="

# 새 키 (환경변수)
NEW_KEY = os.environ.get("MS_AI_ENCRYPTION_KEY")
if NEW_KEY is None:
    print("[ERROR] MS_AI_ENCRYPTION_KEY 환경변수가 설정되지 않았습니다.")
    sys.exit(1)

TARGET_FILES = ["ai_sever_info.json", "ai_sever_info_init.json"]

def migrate(file_path):
    if not os.path.exists(file_path):
        print(f"[SKIP] {file_path} 파일 없음")
        return

    # 1. 기존 키로 복호화
    old_fernet = Fernet(OLD_KEY)
    with open(file_path, "rb") as f:
        encrypted_data = f.read()

    try:
        decrypted = old_fernet.decrypt(encrypted_data)
        data = json.loads(decrypted.decode("utf-8"))
    except Exception as e:
        print(f"[ERROR] {file_path} 복호화 실패: {e}")
        return

    # 2. 백업 생성
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{file_path}.backup_{timestamp}"
    shutil.copy2(file_path, backup_path)
    print(f"[BACKUP] {backup_path}")

    # 3. 새 키로 재암호화
    new_fernet = Fernet(NEW_KEY)
    new_encrypted = new_fernet.encrypt(json.dumps(data).encode("utf-8"))

    with open(file_path, "wb") as f:
        f.write(new_encrypted)

    print(f"[OK] {file_path} 마이그레이션 완료")

if __name__ == "__main__":
    if OLD_KEY == NEW_KEY:
        print("[INFO] 기존 키와 새 키가 동일합니다. 키 변경 없이 환경변수 전환만 적용됩니다.")
        sys.exit(0)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    for target in TARGET_FILES:
        migrate(os.path.join(base_dir, target))

    print("\n[완료] 마이그레이션이 완료되었습니다.")
    print("  - 백업 파일을 확인한 후, 정상 동작 검증 뒤 삭제하세요.")
    print("  - OLD_KEY는 마이그레이션 후 이 스크립트에서도 제거하세요.")
```

#### 실행 조건

| 시나리오 | 동작 |
|----------|------|
| 키 변경 없이 환경변수 전환만 | `.env`에 기존 키 설정 → 스크립트 실행 → "키 동일" 메시지 후 종료 |
| 새 키로 교체 | `.env`에 새 키 설정 → 스크립트 실행 → 복호화 → 백업 → 재암호화 |

---

## 작업 2: 의존성 문서화

### 2-1. requirements.txt 생성

```txt
# Python >= 3.10

# === UI 프레임워크 ===
PySide6>=6.5.0

# === 영상 처리 ===
opencv-python>=4.8.0
numpy>=1.24.0

# === 네트워크 ===
requests>=2.31.0

# === 보안/암호화 ===
cryptography>=41.0.0

# === 환경변수 ===
python-dotenv>=1.0.0

# === SMS/카카오톡 알림 ===
solapi>=1.0.0

# === GStreamer (시스템 패키지 - pip 설치 불가) ===
# 아래 패키지는 conda 또는 OS 패키지 매니저로 설치 필요:
#   conda install conda-forge::pygobject
#   conda install conda-forge::gst-plugins-base
#   conda install conda-forge::gst-plugins-good
#   conda install conda-forge::gst-plugins-bad
PyGObject>=3.46.0
```

### 2-2. .gitignore 추가 항목

```gitignore
# 환경변수 (민감 정보)
.env
.env.local

# 마이그레이션 백업
*.backup_*

# PyInstaller 빌드 산출물
build/
dist/
*.spec.bak
```

---

## 작업 3: main.spec 수정

PyInstaller 빌드에 `.env`를 포함하지 않도록 확인합니다. 현재 `main.spec`는 `.env`를 포함하지 않으므로 수정 불필요하지만, `python-dotenv`가 `hiddenimports`에 포함되어야 합니다.

```python
# main.spec 수정
hiddenimports=['cv2', 'numpy', 'resourece_rc', 'dotenv'],
```

---

## 변경 파일 요약

| 파일 | 작업 | 변경 유형 |
|------|------|-----------|
| `main.py` | 환경변수 전환, bare except 제거 | 수정 |
| `crypto_json.py` | 환경변수 전환 | 수정 |
| `uncrypto_json.py` | 환경변수 전환 | 수정 |
| `main.spec` | hiddenimports에 dotenv 추가 | 수정 |
| `.env.example` | 환경변수 템플릿 | 신규 |
| `.gitignore` | .env 제외 규칙 | 신규 또는 수정 |
| `requirements.txt` | 의존성 목록 | 신규 |
| `migrate_encryption_key.py` | 키 마이그레이션 스크립트 | 신규 |

---

## 배포 프로세스 변경사항

### 기존 배포 플로우

```
소스코드 → PyInstaller 빌드 → dist/MS-AI/ 배포 → 실행
```

### 변경 후 배포 플로우

```
소스코드 → PyInstaller 빌드 → dist/MS-AI/ 생성
                                    ↓
                          배포 담당자가 .env 파일 배치
                                    ↓
                          (키 변경 시) migrate_encryption_key.py 실행
                                    ↓
                                  배포 완료
```

### 배포 체크리스트

```
□ .env 파일이 dist/MS-AI/ 디렉토리에 배치되었는가?
□ MS_AI_ENCRYPTION_KEY 값이 설정되었는가?
□ SOLAPI_* 값이 모두 설정되었는가?
□ SOLAPI_SENDER_NUMBER가 실제 등록된 발신번호인가?
□ (키 변경 시) migrate_encryption_key.py 실행 완료?
□ (키 변경 시) ai_sever_info.json 정상 로드 확인?
□ .env 파일 권한이 적절한가? (chmod 600 권장)
```

---

## 검증 방법

### 1. 환경변수 로드 확인

```bash
# .env 없이 OS 환경변수로 실행
MS_AI_ENCRYPTION_KEY="test_key" python -c "
from dotenv import load_dotenv
import os, sys
sys.path.insert(0, '.')
load_dotenv(override=False)
print('KEY:', os.environ.get('MS_AI_ENCRYPTION_KEY'))
"
# 출력: KEY: test_key (OS 변수 우선)
```

### 2. 기존 데이터 복호화 확인

```bash
# .env에 기존 키 설정 후
python -c "
from main import load_crypography_json
data = load_crypography_json('ai_sever_info.json')
print('USER keys:', list(data.get('USER', {}).keys()))
"
```

### 3. Bare except 제거 확인

```bash
# 프로젝트 내 bare except 검색 (0건이어야 함)
grep -rn "except\s*:" main.py
```

### 4. 하드코딩된 민감 정보 검색

```bash
# 아래 검색 결과가 migrate 스크립트 외에 없어야 함
grep -rn "FBRBdZIbc\|NCSV30HGFAONWEPN\|KTNWYZVICVQ7XU5AFUZGNC8OQXT9AACT\|01084461617" \
  --include="*.py" --exclude="migrate_encryption_key.py"
```

---

## 위험 요소 및 대응

| 위험 | 영향 | 대응 |
|------|------|------|
| `.env` 파일 누락 상태로 실행 | 앱 시작 시 `RuntimeError` 발생 | 에러 메시지에 `.env` 확인 안내 포함 |
| 마이그레이션 중 전원 차단 | 암호화 파일 손상 | 백업 파일에서 복구 가능 |
| `.env` 파일 권한 미설정 | 다른 사용자가 키 열람 가능 | 배포 체크리스트에 `chmod 600` 포함 |
| PyInstaller 빌드 시 dotenv 누락 | import 에러 | `hiddenimports`에 dotenv 추가 |

---

## 작업 순서 (권장)

```
1. python-dotenv 설치
2. .env.example 작성
3. .gitignore 수정
4. requirements.txt 작성
5. main.py 수정 (환경변수 전환 + bare except 제거)
6. crypto_json.py, uncrypto_json.py 수정
7. main.spec 수정 (hiddenimports)
8. migrate_encryption_key.py 작성
9. 검증 (위 4가지 테스트)
10. 기존 환경에서 통합 테스트 (로그인 → 카메라 연결 → 알람 → SMS)
```
