from django.shortcuts import render, redirect

from accounts.models import (
    Student,
    QuizResult,
    QuizAnswer
)


def quiz_history(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/login/")

    try:

        student = Student.objects.get(
            id=student_id
        )

    except Student.DoesNotExist:

        request.session.flush()

        return redirect("/login/")

    history = QuizResult.objects.filter(
        student=student
    ).order_by("-created_at")

    return render(
        request,
        "accounts/quiz_history.html",
        {
            "history": history
        }
    )


def quiz_history_detail(request, result_id):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/login/")

    try:

        student = Student.objects.get(
            id=student_id
        )

    except Student.DoesNotExist:

        request.session.flush()

        return redirect("/login/")

    try:

        result = QuizResult.objects.get(
            id=result_id,
            student=student
        )

    except QuizResult.DoesNotExist:

        return redirect("/history/")

    answers = QuizAnswer.objects.filter(
        quiz_result=result
    ).select_related("question")

    return render(
        request,
        "accounts/quiz_history_detail.html",
        {
            "result": result,
            "answers": answers
        }
    )