from django.contrib import admin
from django.urls import path
import myapp.views #from . import views 라고 해도 됨. 이때 6열에 있는 myapp. 도 지워줘야 함

urlpatterns = [
    path('', myapp.views.home, name = "home"),
    path('profile/', myapp.views.profile, name = "profile")
]