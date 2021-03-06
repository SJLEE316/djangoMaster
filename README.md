# django master project

## 디렉토리 구조

```
DJANGOMASTER
├─ djangoMaster
│  ├─ templates
│  │  └─ shared
│  │         _navbar.html_
│  │  └─ main.html
│  │  └─ base.html
│  ├─ static
│  │  ├─ css
│  │  │      style.css
│  │  └─ images
│  │         django.PNG
│  ├─ urls.py
│  └─ views.py
├─ home
│  ├─ templates
│  │  └─ home
│  │         hello.html
│  │         question_list.html
│  │         question_new.html
│  │         question_detail.html
│  │         question_form.html
│  ├─ templatetags
│  │  └─ __init__.py
│  │  └─ home_filter.py
│  ├─ urls.py
│  ├─ forms.py
│  ├─ models.py
│  └─ views.py
├─ users
│  ├─ templates
│  │  └─ users
│  │         form_error.html
│  │         login.html
│  ├─ urls.py
│  ├─ models.py

```

## note

### 1. 개발환경 설정

### 2. HTML

- HTML 띄우기
- APP 생성 후 HTML 띄우기
- APP의 URL 분리하기
- 링크 연결하기
- Modeling
- ORM
- Admin
- READ : Admin에서 등록한 데이터 HTML에서 Read하기
- READ : Admin에서 등록한 데이터의 상세보기 페이지 만들고 데이터 Read하기
- CREATE, READ : 각 Question에 답변(Answer) Create하고 Read하기
- base.html 생성하고 상속하기
- Static을 사용하여 style, image 적용하기
- CREATE : Question with ModelForm
- CREATE : Answer with ModelForm
- forms.py에서 빈칸 있을 경우 오류 발생하기
- 부트스트랩 이용해서 화면 꾸미기
- CREATE : Not Using ModelForm
- Navbar를 include 해서 사용하기
- Paginator : 페이징 기능 추가하기
- 질문에 달린 답변 개수 표시하기
- 로그인, 로그아웃 기능 구현하기
