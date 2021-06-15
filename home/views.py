from django.shortcuts import render

def hello(request):
  return render(request, 'home/hello.html')

def question_list(request):
  return render(request, 'home/question_list.html')