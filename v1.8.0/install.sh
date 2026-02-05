#!/bin/bash

mkdir ~/workspace/MS-AI-Viewer/install

cd ~/workspace/MS-AI-Viewer/install

# sh 기반 파일을 생성합니다.
echo "cd /home/$USER/workspace/MS-AI-Viewer
python3 /home/$USER/workspace/MS-AI-Viewer/main.py" > main.sh

chmod +x main.sh

# 생성한 sh 파일을 실행하는 .desktop 파일을 생성합니다.
echo "[Desktop Entry]
Encoding=UTF-8
Name=MS-AI-Viewer
Type=Application
Path=/home/$USER/workspace/MS-AI-Viewer/install
Icon=/home/$USER/workspace/MS-AI-Viewer/ui/images/icon2.png
Exec=/home/$USER/workspace/MS-AI-Viewer/install/main.sh
Terminal=false" > ms-ai.desktop

# 생성한 .desktop 파일을 /usr/share/applications 경로로 복사합니다.
sudo cp ms-ai.desktop /usr/share/applications/
