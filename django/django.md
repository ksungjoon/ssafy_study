#DJANGO
___

##1. 가상환경 만들기

####1. 가상환경을 모아두기위해 ~ 위치에 venv 폴더 만들기
    - cd ~
    - mkdir venv
####2. venv 폴더안에 first라는 가상환경 만들기
    - cd ~/venv 에서 mkdir first 
####3. first 폴더 가상환경화 시키기 
    - python -m venv ~/venv/first
####4. first 가상환경 활성화 
    - source ~/venv/first/Script/activate
####5. 가상환경 비활성화
    - deactivate
####6. 가상 환경 pip 설치하기
    - pip install django==3.2.18 장고 설치
####7. 가상 환경 pip 리스트 requiremnets 텍스트 형식으로 만들기
    - pip freeze > requirements.txt
####8. requirements 텍스트 가상 환경 pip 현재 가상 환경에 설치하기
    - requirements 텍스트 위치에서 pip install -r requirements.txt

___

##2. project, app 만들기

####1. 바탕화면에 project 생성 project 이름은 PJT
    - django-admin startproject PJT
####2. 해당 프로젝트파일로 들어가서 app생성 app 이름은 articles app_name은 보통 복수
    - python manage.py startapp articles
####3. 해당 프로젝트에서 app 등록하기
    - 해당 프로젝트 파일에서 settings.py 들어가기
    - INSTALLED_APPS 리스트에 반드시  APP 추가
    - ***반드시 쉼표 추가 !!***

####4. 해당 프로젝트 실행하기
    - python manage.py runserver

___

##3. 데이터의 흐름

1. URL 에서 path 작성
2. view 에서 사용함수 작성
3. template 에서 html 작성

___

##4. templates 폴더 작성
- 실제 내용을 보여주는데 사용되는 파일
- 파일의 구조나 레이아웃을 정의
- Template 파일의 기본경로
    - app 폴더 안의 templates폴더
    - app_name/templates/app_name
    - ***템플릿 폴더 이름은 반드시 templates라고 지정해야함***
    
___

##5. view.py 함수 render 
    render(request, template_name,context)
- 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 <br> 렌더링 된 텍스트와 함께 HttpResponse(응답)객체를 반환하는 함수
1. request
    - 응답을 생성하는데 사용되는 요청 객체
2. template_name
    - 템플릿의 전체 이름 또는 템플릿 이름의 경로
3. context
    _ 템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)
