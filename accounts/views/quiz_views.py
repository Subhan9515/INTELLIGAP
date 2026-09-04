import random

from django.shortcuts import render, redirect
from django.utils import timezone

from accounts.models import (
    Student,
    Question,
    QuizResult,
    WrongAnswer,
    QuizAnswer
)

from accounts.quiz_data.python_questions import load_python_questions
from accounts.quiz_data.ml_questions import load_ml_questions
from accounts.quiz_data.dbms_questions import load_dbms_questions
from accounts.quiz_data.java_questions import load_java_questions


def load_all_questions():

    load_python_questions()
    load_ml_questions()
    load_dbms_questions()
    load_java_questions()


def start_quiz(request, subject):

    load_all_questions()

    questions = list(
        Question.objects.filter(
            subject=subject
        )
    )

    if not questions:

        return render(
            request,
            "accounts/no_questions.html",
            {
                "subject": subject
            }
        )

    number_of_questions = min(
        15,
        len(questions)
    )

    selected_questions = random.sample(
        questions,
        number_of_questions
    )

    request.session[
        "last_quiz_question_ids"
    ] = [
        question.id
        for question in selected_questions
    ]

    request.session[
        "quiz_subject"
    ] = subject

    request.session[
        "quiz_start_time"
    ] = timezone.now().isoformat()

    return render(
        request,
        "accounts/quiz.html",
        {
            "questions":
            selected_questions,

            "subject":
            subject
        }
    )


def process_quiz(
    request,
    subject,
    template_name,
    loader_function
):

    loader_function()

    student_id = request.session.get(
        "student_id"
    )

    if not student_id:

        return redirect("/login/")

    try:

        student = Student.objects.get(
            id=student_id
        )

    except Student.DoesNotExist:

        request.session.flush()

        return redirect("/login/")

    if request.method == "GET":

        questions = list(
            Question.objects.filter(
                subject=subject
            ).order_by("?")[:15]
        )

        request.session[
            "last_quiz_question_ids"
        ] = [
            q.id
            for q in questions
        ]

    else:

        question_ids = request.session.get(
            "last_quiz_question_ids",
            []
        )

        questions = list(
            Question.objects.filter(
                id__in=question_ids,
                subject=subject
            )
        )

    if request.method == "POST":

        score = 0

        quiz_result = QuizResult.objects.create(
            student=student,
            subject=subject,
            total_questions=len(questions)
        )

        for q in questions:

            user_answer = request.POST.get(
                str(q.id),
                ""
            ).strip()

            correct_answer = q.answer.strip()

            is_correct = (
                user_answer.lower()
                ==
                correct_answer.lower()
            )

            if is_correct:

                score += 1

            else:

                WrongAnswer.objects.create(
                    student=student,
                    question=q,
                    user_answer=user_answer,
                    correct_answer=correct_answer,
                    topic=q.topic
                )

            QuizAnswer.objects.create(
                quiz_result=quiz_result,
                question=q,
                user_answer=user_answer,
                correct_answer=correct_answer,
                is_correct=is_correct
            )

        quiz_result.score = score

        quiz_result.correct_answers = score

        quiz_result.wrong_answers = (
            len(questions) - score
        )

        quiz_result.save()

        return redirect(
            "/dashboard/"
        )

    return render(
        request,
        template_name,
        {
            "questions":
            questions
        }
    )


def python_quiz(request):

    return process_quiz(
        request,
        "Python",
        "accounts/python_quiz.html",
        load_python_questions
    )


def ml_quiz(request):

    return process_quiz(
        request,
        "Machine Learning",
        "accounts/ml_quiz.html",
        load_ml_questions
    )


def dbms_quiz(request):

    return process_quiz(
        request,
        "DBMS",
        "accounts/dbms_quiz.html",
        load_dbms_questions
    )


def java_quiz(request):

    return process_quiz(
        request,
        "Java",
        "accounts/java_quiz.html",
        load_java_questions
    )