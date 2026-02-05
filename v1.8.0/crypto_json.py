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

file_name = "ai_sever_info_ori"

# JSON 파일 읽기
with open(f"./{file_name}.json", "rb") as file:
    # file_data = json.load(file)
    file_data = file.read()

# 파일 데이터 암호화
encrypted_data = fernet.encrypt(file_data)

# 암호화된 데이터를 파일에 저장
with open(f"./{file_name[:-4]}.json", "wb") as file:
    file.write(encrypted_data)
