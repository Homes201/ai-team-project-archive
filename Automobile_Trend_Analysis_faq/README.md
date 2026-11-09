# 👑SK네트웍스 4기_6조👑

> **2026-11 실행 안내:** 아래 본문은 2024년 팀 프로젝트 기록입니다. 로컬에서는 Python 3.11 환경에 `pip install -r requirements.txt`를 실행하고, `streamlit/.streamlit/secrets.example.toml`을 참고해 **본인 DB 정보**를 `streamlit/.streamlit/secrets.toml`에 저장한 뒤 `cd streamlit; streamlit run main.py`로 화면을 엽니다. DB가 없으면 첫 화면과 설정 안내를 볼 수 있으며 실제 차량·FAQ 조회는 할 수 없습니다. 수집을 다시 실행하면 테이블이 교체되므로 환경 변수 `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`을 설정한 뒤 `python crawling/runner.py --replace`를 명시적으로 실행하세요. 예전 사이트 구조와 수집 API가 바뀌었을 수 있어 수집 성공은 보장하지 않습니다. 저장소에서 과거 DB 설정 파일을 제거했으며 재사용한 비밀번호가 있다면 교체해야 합니다.

<hr>

### 😇 팀 소개

### 팀명 : 일단커밋해

### 팀원 소개
<p align="center">
	<img src="https://avatars.githubusercontent.com/말랑곰" width="150" height="150"/>
	<img src="https://avatars.githubusercontent.com/sunblockisneeded" width="150" height="150"/>
	<img src="https://avatars.githubusercontent.com/Homes201" width="150" height="150"/>
	<img src="https://avatars.githubusercontent.com/dydwns123123" width="150" height="150"/>
</p>

<div align="center">
	
|   &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;  &nbsp;  &nbsp;🐶 이호재 &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;  &nbsp;  &nbsp;    |      &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;  &nbsp;  &nbsp;🐱오창준  &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;  &nbsp;  &nbsp;    |      &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;  &nbsp;  &nbsp;🐕하상집  &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;  &nbsp;  &nbsp;    |     &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;  &nbsp;  &nbsp;🐲안준용  &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;  &nbsp;  &nbsp;   | 
|:------------------------------------------:|:--------------------------------------:|:------------------------------------------:|:-----------------------------------:|
|DB 및 총괄|크롤링 / streamlit|크롤링 / streamlit|크롤링 / streamlit|
</div>



###  🚩 프로젝트 개요 
> 
<hr>
  
- 프로젝트 명 : 전국 자동자 트랜드 분석 & 현대&기아 FAQ 확인 시스템

- 개발 기간: 2024-08-22 ~ 2024-08-23

- 프로젝트 핵심 기능

  - 자동차 등록 현황 조회 : 전국 자동차 등록대수와 차종,용도별 등록 대수를 날짜 기준으로 **시각화** 
  >
  - 자동차 제조사별 질문 통합 : 현대와 기아차의 대표적인 질문들과 그 답변을 통합 **확인**
  >
  - 제조사별 질문에 대한 검색 : 각 자동차의 질문과 답변에 대한 **검색**


### 👩‍🏫 서비스 목표 
>
<hr>

  - 사용자로 하여금 다양한 형태로 자동차 등록 대수를 확인하고 추이 분석하여 트랜드 확인
>
  - 한 페이지에서 다양한 제조사의 질문과 답변을 확인으로 편의성 향상
>
  - 제목과 그 답변의 키워드로 검색 지원으로 인한 편의성 향상 


### 🔨 기술 스택
<hr>
<div>
<img src="https://img.shields.io/badge/postgres-4479A1?style=for-the-badge&logo=postgres&logoColor=white">
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/dbeaver-382923?style=for-the-badge&logo=dbeaver&logoColor=white"> 
<img src="https://img.shields.io/badge/streamlit-%23FF0000?style=for-the-badge&logo=streamlit&logoColor=white">
</div>

### 🐝 프로시저
- pip install -r requirement.txt  : 프로젝트에 설치되는 필수 패키지 설치
>
- crawling > runnner.py 실행 완료 후 streamlit > streamlit run main.py 실행

### 💻 ERD 화면 설계서
<hr>

<p align="center"><img src="image/ERD.png"/></p>

### 🧪 테스트 케이스 -자동차 등록 조회 & 자동차 FAQ
<hr>

<details>
<summary><b>자동차 등록현황(월별)</b></summary>
<img src="./image/image(1).png">
</details>

<details>
<summary><b>자동차 등록현황(차종)</b></summary>
<img src="./image/image(2).png">
</details>

<details>
<summary><b>자동차 등록현황(용도)</b></summary>
<img src="./image/image(3).png">
</details>



<details>
<summary><b>자동차FAQ 메인 화면</b></summary>
<img src="./image/FAQ_2.png">
</details>

<details>
<summary><b>자동차FAQ 검색/질문조회 기본화면</b></summary>
<img src="./image/FAQ_3.png">
</details>

<details>
<summary><b>자동차FAQ 검색/질문조회 검색후 질문조회</b></summary>
<img src="./image/FAQ_4.png">
</details>
<hr>

<br><br><br>
