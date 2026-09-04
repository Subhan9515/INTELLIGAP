from collections import Counter
from datetime import timedelta

from django.shortcuts import render, redirect
from django.utils import timezone

from accounts.models import Student, Question, QuizResult, WrongAnswer


def dashboard(request):
    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/login/")

    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        request.session.flush()
        return redirect("/login/")

    results = QuizResult.objects.filter(
        student=student
    ).order_by("-id")

    latest = results.first()
    total_quizzes = results.count()

    overall_score = 0

    if total_quizzes > 0:
        total_score = sum(result.score for result in results)
        total_questions = sum(result.total_questions for result in results)

        if total_questions > 0:
            overall_score = round(
                (total_score / total_questions) * 100
            )

    wrong_answers = WrongAnswer.objects.filter(
        student=student
    )

    weak_counter = Counter(
        wrong_answers.values_list("topic", flat=True)
    )

    weak_topics = [
        topic
        for topic, count in weak_counter.most_common(5)
    ]

    attempted_question_ids = set()

    for result in results:
        pass

    student_wrong_questions = set(
        wrong_answers.values_list(
            "question_id",
            flat=True
        )
    )

    all_student_questions = set(
        QuizResult.objects.filter(
            student=student
        ).values_list(
            "id",
            flat=True
        )
    )

    strong_topics = []

    if total_quizzes > 0:

        attempted_topics = Counter()

        for result in results:
            questions = Question.objects.filter(
                subject=result.subject
            )

            for question in questions:
                attempted_topics[question.topic] += 1

        for topic in attempted_topics.keys():

            wrong_count = weak_counter.get(topic, 0)

            if wrong_count == 0:
                strong_topics.append(topic)

    return render(
        request,
        "accounts/dashboard.html",
        {
            "student": student,
            "latest": latest,
            "total_quizzes": total_quizzes,
            "overall_score": overall_score,
            "weak_topics": weak_topics,
            "strong_topics": strong_topics[:5],
        }
    )


def subjects(request):
    return render(
        request,
        "accounts/subjects.html"
    )


def quiz_instructions(request, subject):

    return render(
        request,
        "accounts/quiz_instructions.html",
        {
            "subject": subject,
            "number_of_questions": 15,
            "time_limit": 5,
        }
    )


def progress_analysis(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/login/")

    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        request.session.flush()
        return redirect("/login/")

    results = QuizResult.objects.filter(
        student=student
    ).order_by("id")

    progress_data = []

    for index, result in enumerate(results, start=1):

        percentage = 0

        if result.total_questions > 0:
            percentage = round(
                (result.score / result.total_questions) * 100
            )

        progress_data.append({
            "quiz": index,
            "score": percentage
        })

    return render(
        request,
        "accounts/progress.html",
        {
            "student": student,
            "progress_data": progress_data,
        }
    )