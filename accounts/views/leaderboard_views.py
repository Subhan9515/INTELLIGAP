from django.shortcuts import render

from ..models import Student, QuizResult


def leaderboard(request):

    students = Student.objects.all()

    leaderboard_data = []

    for student in students:

        results = QuizResult.objects.filter(
            student=student
        )

        total_score = 0
        total_questions = 0

        for result in results:

            total_score += result.score
            total_questions += result.total_questions

        if total_questions > 0:

            percentage = (
                total_score / total_questions
            ) * 100

        else:

            percentage = 0

        leaderboard_data.append({
            "student": student,
            "score": round(percentage, 2),
            "quizzes": results.count(),
        })


    leaderboard_data.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    for index, item in enumerate(
        leaderboard_data,
        start=1
    ):

        item["rank"] = index


    return render(
        request,
        "accounts/leaderboard.html",
        {
            "leaderboard": leaderboard_data,
        }
    )