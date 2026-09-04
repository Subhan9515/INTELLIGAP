from django.urls import path

from .views.student_views import *
from .views.teacher_views import *
from .views.quiz_views import *
from .views.history_views import *
from .views.auth_views import *


urlpatterns = [

    # ================================
    # STUDENT DASHBOARD
    # ================================

    path(
        "dashboard/",
        dashboard,
        name="dashboard"
    ),

    path(
        "subjects/",
        subjects,
        name="subjects"
    ),

    path(
        "instructions/<str:subject>/",
        quiz_instructions,
        name="quiz_instructions"
    ),


    # ================================
    # TEACHER
    # ================================

    path(
        "teacher/register/",
        teacher_register,
        name="teacher_register"
    ),

    path(
        "teacher/login/",
        teacher_login,
        name="teacher_login"
    ),

    path(
        "teacher/dashboard/",
        teacher_dashboard,
        name="teacher_dashboard"
    ),

    path(
        "teacher/logout/",
        teacher_logout,
        name="teacher_logout"
    ),

    path(
        "teacher/add-question/",
        add_question,
        name="add_question"
    ),

    path(
        "teacher/question-bank/",
        question_bank,
        name="question_bank"
    ),

    path(
        "teacher/modify-question/<int:question_id>/",
        modify_question,
        name="modify_question"
    ),

    path(
        "teacher/delete-question/<int:question_id>/",
        delete_question,
        name="delete_question"
    ),


    # ================================
    # QUIZZES
    # ================================

    path(
        "python-quiz/",
        python_quiz,
        name="python_quiz"
    ),

    path(
        "ml-quiz/",
        ml_quiz,
        name="ml_quiz"
    ),

    path(
        "dbms-quiz/",
        dbms_quiz,
        name="dbms_quiz"
    ),

    path(
        "java-quiz/",
        java_quiz,
        name="java_quiz"
    ),

    path(
        "quiz/<str:subject>/",
        start_quiz,
        name="start_quiz"
    ),


    # ================================
    # AUTHENTICATION
    # ================================

    path(
        "register/",
        register,
        name="register"
    ),

    path(
        "login/",
        login_view,
        name="login"
    ),


    # ================================
    # PROGRESS
    # ================================

    path(
        "progress/",
        progress_analysis,
        name="progress_analysis"
    ),


    # ================================
    # HISTORY
    # ================================

    path(
        "history/",
        quiz_history,
        name="quiz_history"
    ),

    path(
        "history/<int:result_id>/",
        quiz_history_detail,
        name="quiz_history_detail"
    ),


    # ================================
    # PASSWORD RESET
    # ================================

    path(
        "forgot-password/",
        forgot_password,
        name="forgot_password"
    ),

    path(
        "verify-otp/",
        verify_otp,
        name="verify_otp"
    ),

    path(
        "otp-success/",
        otp_success,
        name="otp_success"
    ),

    path(
        "reset-password/",
        reset_password,
        name="reset_password"
    ),

]