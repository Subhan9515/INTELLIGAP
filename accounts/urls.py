from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("subjects/", views.subjects, name="subjects"),
    path(
        "instructions/<str:subject>/",
        views.quiz_instructions,
        name="quiz_instructions"
    ),

    path("python-quiz/", views.python_quiz, name="python_quiz"),
    path("ml-quiz/", views.ml_quiz, name="ml_quiz"),
    path("dbms-quiz/", views.dbms_quiz, name="dbms_quiz"),
    path("java-quiz/", views.java_quiz, name="java_quiz"),

    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("progress/", views.progress_analysis, name="progress_analysis"),

    path(
        "history/",
        views.quiz_history,
        name="quiz_history"
    ),

    path(
        "history/<int:result_id>/",
        views.quiz_history_detail,
        name="quiz_history_detail"
    ),

    path("forgot-password/", views.forgot_password, name="forgot_password"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
    path("otp-success/", views.otp_success, name="otp_success"),
    path("reset-password/",views.reset_password,name="reset_password"),
    ]