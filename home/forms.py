from django import forms
from home.models import Question, Answer

class QuestionForm(forms.ModelForm): # 모델 폼을 상속받은 QuestionForm 클래스
  class Meta: # 내부 Meta 클래스
    model = Question
    fields = ['subject', 'content']
    labels = {
      'subject' : '제목',
      'content' : '내용',
    }

class AnswerForm(forms.ModelForm):
  class Meta:
    model = Answer
    fields = ['content']
    labels = {
      'content': '답변내용',
    }    