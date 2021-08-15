from django.shortcuts import render, get_object_or_404, redirect # render가 import 되어있다. (views.py기본 세팅)
from .models import * # Question # 모델 import 하기
# from django.utils import timezone # 이 프로젝트에서는 create_date를 자동으로 설정해두었다.
from .forms import QuestionForm, AnswerForm # QuestionForm 클래스 import 하기
from django.core.paginator import Paginator

def hello(request):
  return render(request, 'home/hello.html')

def question_list(request):
  # questions = Question.objects.all() # Question 모델 데이터를 questions라고 한다.
  questions = Question.objects.order_by('-create_date') # Question 모델 데이터를 작성일시의 역순(-)으로 정렬한다.
  # Paging 기능 구현하기
  page = request.GET.get('page', '1') # GET 방식 요청 URL에서 page값을 가져올 때 사용(?page=1). page 파라미터가 없는 URL을 위해 기본값으로 1을 지정한 것
  paginator = Paginator(questions, 5) # Paginator 클래스는 questions를 페이징 객체 paginator로 변환. 페이지당 5개씩 보여주기
  page_obj = paginator.get_page(page) # page_obj 객체에는 여러 속성이 존재
  context = { 'questions_list' : page_obj } # page_obj를 question_list에 저장한다.
  # context = { 'questions_list' : questions } # 위의 questions를 context 변수인 question_list에 저장한다.
  return render(request, 'home/question_list.html', context)

def question_detail(request, question_id):
  # question = Question.objects.get(id=question_id) # urls에 mapping된 question_id와 같은 것
  question = get_object_or_404(Question, pk=question_id) # 404페이지 출력하기
  context = { 'a_question' : question } # 위의 question를 context 변수인 a_question에 저장한다.
  return render(request, 'home/question_detail.html', context)

# 모델 폼 이용하지 않을 경우 필요한 함수
def question_new(request):
  return render(request, 'home/question_new.html')

def question_create(request):
  if request.method == "POST":
    subject=request.POST.get('subject') # HTML의 name과 같아야 한다.
    content=request.POST.get('content')
    Question.objects.create(subject=subject, content=content)
  return redirect('home:question_list')

  # 모델 폼 이용한 코드
  # if request.method == 'POST':
  #   a_form = QuestionForm(request.POST)
  #   if a_form.is_valid():
  #     question = a_form.save(commit=False) # 폼에 없는 필드인 create_date부분을 자동입력으로 모델을 설정하였기 때문에 a_form.save()라고 작성하여도 오류가 발생하지는 않는다.
  #     question.save()
  #     return redirect('home:question_list')
  # else: # request.method == 'GET'인 경우
  #   a_form = QuestionForm() # QuestionForm 클래스로 생성한 객체 a_form을 사용할 것이다.
  # context = {'form' : a_form } # html에서의 form과 같다.
  # return render(request, 'home/question_form.html', context)

def answer_create(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  if request.method == "POST":
    a_form = AnswerForm(request.POST)
    if a_form.is_valid():
      answer = a_form.save(commit=False)
      answer.question = question
      answer.save()
      return redirect('home:question_detail', question_id=question.id) # 두 번째 인수인 question_id = question.id
  else:
    a_form = AnswerForm()
  context = {'a_question': question, 'form': a_form} # HTML에 표시되는 이름은 통일한다. 예를들어 question_detail 함수에서 a_question으로 하였으므로, 여기도 a_question에 저장한다.
  return render(request, 'home/question_detail.html', context)  
  
  # forms.py 사용하지 않은 코드
  # a_question = get_object_or_404(Question, pk=question_id) # 어떤 question 글에 달린 answer?
  # a_content = request.POST.get('content') # 뒤에 content는 html>name이랑 같다
  # Answer.objects.create(question = a_question, content = a_content), # models.py = views.py, Answer 모델에 직접 저장해도 된다.
  # a_question.answer_set.create(content = a_content) # models.py = views.py, answer을 question 모델에 저장하였다.
  # return redirect('home:question_detail', question_id=a_question.id)
