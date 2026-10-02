from django.urls import path

from .views.student_views import (
    dashboard,
    subjects,
    quiz_instructions,
)

from .views.teacher_views import (
    teacher_register,
    teacher_login,
    teacher_dashboard,
    teacher_logout,
    add_question,
    question_bank,
    modify_question,
    delete_question,
)

from .views.quiz_views import (
    python_quiz,
    ml_quiz,
    dbms_quiz,
    java_quiz,
    start_quiz,
)

from .views.history_views import (
    quiz_history,
    quiz_history_detail,
    progress_analysis,
)

from .views.auth_views import (
    register,
    login_view,
    forgot_password,
    verify_otp,
    otp_success,
    reset_password,
)

from .views.knowledge_gap_views import knowledge_gap
from .views.recommendation_views import recommendation


urlpatterns = [

    # ============================================================
    # STUDENT DASHBOARD
    # ============================================================

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


    # ============================================================
    # TEACHER
    # ============================================================

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


    # ============================================================
    # QUIZZES
    # ============================================================

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


    # ============================================================
    # AUTHENTICATION
    # ============================================================

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


    # ============================================================
    # MY PROGRESS
    # ============================================================

    path(
        "progress/",
        progress_analysis,
        name="progress_analysis"
    ),


    # ============================================================
    # QUIZ HISTORY
    # ============================================================

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


    # ============================================================
    # PASSWORD RESET
    # ============================================================

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


    # ============================================================
    # KNOWLEDGE GAP ANALYSIS
    # ============================================================

    path(
        "knowledge-gap/",
        knowledge_gap,
        name="knowledge_gap"
    ),


    # ============================================================
    # STUDY RECOMMENDATION
    # ============================================================

    path(
        "recommendation/",
        recommendation,
        name="recommendation"
    ),

]