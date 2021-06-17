from django.urls import path
from .views import * # home>views에서 모든 함수를 가져온다.

app_name = "home"
urlpatterns = [
  path('go_hello', hello, name="hello"), # home>views.py의 hello함수를 의미한다. 이름을 붙여준다.
  path('question_list', question_list, name="question_list"), # 경로, 함수, 경로 이름
  path('<int:question_id>', question_detail, name="question_detail"), # question_id에 숫자가 mapping되었다.
  path('answer/create/<int:question_id>', answer_create, name="answer_create"), # question_id에 숫자가 mapping되었다. 
  path('question_create', question_create, name="question_create"),
]