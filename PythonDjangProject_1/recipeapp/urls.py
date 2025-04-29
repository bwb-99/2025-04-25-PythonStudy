'''
    django-admin startproject : 장고 프로젝트 생성 명령
    startapp : 프로젝트의 기능설정
    migrate : 데이터베이스 설정
    runserver : 서버구동
    models.pu = 데이터베이스 연동 (DAO)
    views.py = 데이터를 HTML전송
    urls.pu = 화면 이동
    templete
    manage.py => 파이썬 명령어 사용시
    settings => 데이터베이스 설정,
'''
from django.urls import path

from recipeapp import views
"""
    1. models : 데이터베이스 연동
    2. views : HTML로 전송할 파일 전송
    3. urls : views가 가지고 있는 함수 호출
"""
# @RequestMapping
urlpatterns=[
    path('',views.index,name="index"),
    path('recipe_list/',views.recipeList,name="recipe_list")
]