from django.shortcuts import render, get_object_or_404, redirect # render가 import 되어있다. (views.py기본 세팅)
from .models import * # Question # 모델 import 하기
# from django.utils import timezone # 이 프로젝트에서는 create_date를 자동으로 설정해두었다.
from .forms import QuestionForm # QuestionForm 클래스 import 하기

def hello(request):
  return render(request, 'home/hello.html')

def question_list(request):
  # questions = Question.objects.all() # Question 모델 데이터를 questions라고 한다.
  questions = Question.objects.order_by('-create_date') # Question 모델 데이터를 작성일시의 역순(-)으로 정렬한다.
  context = { 'questions_list' : questions } # 위의 questions를 context 변수인 question_list에 저장한다.
  return render(request, 'home/question_list.html', context)

def question_detail(request, question_id):
  # question = Question.objects.get(id=question_id) # urls에 mapping된 question_id와 같은 것
  question = get_object_or_404(Question, pk=question_id) # 404페이지 출력하기
  context = { 'a_question' : question } # 위의 question를 context 변수인 a_question에 저장한다.
  return render(request, 'home/question_detail.html', context)

def question_create(request):
  if request.method == 'POST':
    a_form = QuestionForm(request.POST)
    if a_form.is_valid():
      question = a_form.save(commit=False) # 폼에 없는 필드인 create_date부분을 자동입력으로 모델을 설정하였기 때문에 a_form.save()라고 작성하여도 오류가 발생하지는 않는다.
      question.save()
      return redirect('home:question_list')
  else: # request.method == 'GET'인 경우
    a_form = QuestionForm() # QuestionForm 클래스로 생성한 객체 a_form을 사용할 것이다.
  context = {'form' : a_form } # html에서의 form과 같다.
  return render(request, 'home/question_form.html', context)

def answer_create(request, question_id):
  a_question = get_object_or_404(Question, pk=question_id) # 어떤 question 글에 달린 answer?
  a_content = request.POST.get('content') # 뒤에 content는 html>name이랑 같다
  # Answer.objects.create(question = a_question, content = a_content), # models.py = views.py, Answer 모델에 직접 저장해도 된다.
  a_question.answer_set.create(content = a_content) # models.py = views.py, answer을 question 모델에 저장하였다.
  return redirect('home:question_detail', question_id=a_question.id)
