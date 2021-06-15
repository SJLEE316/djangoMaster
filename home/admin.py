from django.contrib import admin
from .models import Question # Question 모델 import 해준다.

# Register your models here.

# 방법 1.
@admin.register(Question)

class QuestionAdmin(admin.ModelAdmin) :
  list_display = ( # 목록에서 보여줄 column
    'subject',
    'content',
    'create_date',
  )
  search_fields = [ # 검색이 가능한 column
    'subject',
  ]

# 방법 2.
# class QuestionAdmin(admin.ModelAdmin) : # QuestionAdmin 클래스를 추가
#   search_fields = [ # 검색이 가능한 column
#     'subject',
#   ]

# admin.site.register(Question, QuestionAdmin) # class 밑에 입력해야한다.