from django.db import models

# Create your models here.

class Question(models.Model):
  subject = models.CharField(max_length=200, null = False) # 글자 수를 제한하고 싶은 데이터는 CharField를 사용해야 한다.
  content = models.TextField() # 긴 문자열 데이터타입, 글자 수 제한이 없는 데이터는 TextField를 사용해야 한다.
  create_date = models.DateTimeField(auto_now = True) # 시간, 날짜 데이터를 자동으로 넣어준다.

# shell에서 데이터 조회할 때 subject로 볼 수 있게 한다. -> 가독성을 높여주지
  def __str__(self):
    return self.subject