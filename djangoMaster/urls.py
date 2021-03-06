"""djangoMaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # include 삽입
# from . import views # 모든 경로에서 views를 가져온다.
# from .views import main # 루트 디렉토리의 views에서 main함수를 가져온다.
from .views import * # 루트 디렉토리의 views에서 모든 함수를 가져온다.
# from home.views import * # home의 views에서 모든 함수를 가져온다. include쓰면 필요 없어!

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', main, name="main"), # views.py의 main함수를 의미한다. 이름을 붙여준다.
  # path('go_hello', hello),
  path('home/', include('home.urls')), # home>urls.py에서 관리할거야
  path('users/', include('users.urls')), # users>urls.py에서 관리할거야
]
