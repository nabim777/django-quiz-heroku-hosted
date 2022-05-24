from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "home"),
    path('api/get-quiz/',views.get_quiz, name = "get_quiz"),
    path('api/get-category/',views.get_category, name = "get_category"),
    path('api/get-question/',views.get_question, name = "get_question"),
    path('api/get-answer/',views.get_answer, name = "get_answer"),
    path('quiz/',views.quiz, name = "quiz"),
]
