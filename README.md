
## 📌 프로젝트 개요
- **목적:**  
  사용자가 “오늘 하루 어땠나요?”라는 간단한 질문에 답하며  
  공감과 위로를 받을 수 있도록 돕는 웹 애플리케이션

## 🔍 상세 기능

1. **기분 기록**  
   - “오늘 하루 어땠나요?” 질문에 대답  
   - 5단계 버튼 중 하나 선택  
2. **응원 메시지**  
   - 선택된 기분별로 사전 정의된 응원 문구 목록에서 랜덤 메시지 제공  
3. **UI/UX 전환**  
   - 기분 단계마다 배경색·아이콘·폰트 색상 자동 변경  
4. **반복 기록**  
   - “오늘 또 기록하기” 버튼 클릭 시 초기 화면으로 돌아가기  
5. **로컬 기록(Optional)**  
   - 브라우저 로컬 스토리지에 오늘의 기록 저장 후 새로고침에도 유지  

## 👤 사용자 시나리오

1. 사용자가 `http://127.0.0.1:5000` 에 접속  
2. “오늘 하루 어땠나요?” 문구와 함께 5개의 감정 버튼(`very_good`, …, `very_bad`) 표시  
3. 버튼 클릭 → `POST /process` 호출  
4. 서버에서 감정값을 받아 응원 메시지 생성  
5. 클라이언트에 메시지 전송 → `response.html` 또는 JavaScript로 화면 업데이트  
6. “오늘 또 기록하기” 클릭 시 초기 상태로 리셋


- **입출력 형태:**  
  - **Input:** 버튼 클릭 (`very_good`, `good`, `neutral`, `bad`, `very_bad`)  
  - **Output:** 해당 감정에 맞는 위로·격려 문구

    
## 🛠️ 기술 스택

- **Frontend**  
  - HTML5, CSS3 (반응형 레이아웃)  
  - JavaScript (Fetch API)  
- **Backend**  
  - Python 3.8+  
  - Flask 2.x  
  - Jinja2 템플릿 엔진  
- **Dependencies** (requirement.txt)  
  ```text
  Flask==2.3.2
  python-dotenv==1.0.0

  ## 필요한 환경설정
  1. python 3.8이상
  2. 가상환경 설정
  3. requirement.txt
  Flask==2.3.2
  python-dotenv==1.0.0

  pip install -r requirement.txt 명령으로 설치
  4. 터미널에 python app.py입력 또는 flask run 으로 실행
