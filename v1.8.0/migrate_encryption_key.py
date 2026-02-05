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
