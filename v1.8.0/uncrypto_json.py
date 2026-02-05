import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import json

load_dotenv(override=False)
KEY = os.environ.get("MS_AI_ENCRYPTION_KEY")
if KEY is None:
    raise RuntimeError("MS_AI_ENCRYPTION_KEY 환경변수가 설정되지 않았습니다.")

# 암호화 엔진 생성
fernet = Fernet(KEY)

file_name = "AI_info"

# JSON 파일 읽기
with open(f"../{file_name}.json", "rb") as f:
    file = f.read()
    file_tran = fernet.decrypt(file)
    uncrypted_data = json.loads(file_tran.decode())

# 암호화된 데이터를 파일에 저장
with open(f"./{file_name}.json", "w", encoding="UTF-8") as f:
    f.write(json.dumps(uncrypted_data, indent=4))
