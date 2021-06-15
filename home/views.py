from django.shortcuts import render # render가 import 되어있다. (views.py기본 세팅)
from .models import Question # 모델 import 하기

def hello(request):
  return render(request, 'home/hello.html')

def question_list(request):
  # questions = Question.objects.all() # Question 모델 데이터를 questions라고 한다.
  questions = Question.objects.order_by('-create_date') # Question 모델 데이터를 작성일시의 역순(-)으로 정렬한다.
  context = { 'questions_list' : questions } # 위의 questions를 context 변수인 question_list에 저장한다.
  return render(request, 'home/question_list.html', context)

def question_detail(request, question_id):
  question = Question.objects.get(id=question_id) # urls에 mapping된 question_id와 같은 것
  context = { 'a_question' : question } # 위의 question를 context 변수인 a_question에 저장한다.
  return render(request, 'home/question_detail.html', context)