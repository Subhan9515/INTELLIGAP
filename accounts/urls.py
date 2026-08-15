from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("subjects/", views.subjects, name="subjects"),
    path("instructions/<str:subject>/", views.quiz_instructions, name="quiz_instructions"),

    path("python-quiz/", views.python_quiz, name="python_quiz"),
    path("ml-quiz/", views.ml_quiz, name="ml_quiz"),
    path("dbms-quiz/", views.dbms_quiz, name="dbms_quiz"),
    path("java-quiz/", views.java_quiz, name="java_quiz"),

    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("progress/", views.progress_analysis, name="progress_analysis"),
]