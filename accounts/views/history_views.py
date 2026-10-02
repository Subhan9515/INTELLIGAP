from django.shortcuts import render, redirect

from accounts.models import (
    Student,
    QuizResult,
    QuizAnswer
)


# ============================================================
# QUIZ HISTORY
# ============================================================

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


# ============================================================
# QUIZ HISTORY DETAIL
# ============================================================

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


# ============================================================
# MY PROGRESS
# ============================================================

def progress_analysis(request):

    # --------------------------------------------------------
    # Check login
    # --------------------------------------------------------

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/login/")


    # --------------------------------------------------------
    # Get student
    # --------------------------------------------------------

    try:

        student = Student.objects.get(
            id=student_id
        )

    except Student.DoesNotExist:

        request.session.flush()

        return redirect("/login/")


    # --------------------------------------------------------
    # Subjects
    # --------------------------------------------------------

    subjects = [
        {
            "name": "Python",
            "icon": "🐍"
        },
        {
            "name": "Machine Learning",
            "icon": "🧠"
        },
        {
            "name": "DBMS",
            "icon": "🗄️"
        },
        {
            "name": "Java",
            "icon": "☕"
        }
    ]


    # --------------------------------------------------------
    # Selected subject
    # --------------------------------------------------------

    selected_subject = request.GET.get(
        "subject",
        ""
    )


    # --------------------------------------------------------
    # Get quiz attempts
    # --------------------------------------------------------

    results = QuizResult.objects.filter(
        student=student
    ).order_by("created_at")


    # --------------------------------------------------------
    # Prepare graph data
    # --------------------------------------------------------

    progress_data = []


    for result in results:

        # Show only selected subject
        if (
            selected_subject
            and result.subject != selected_subject
        ):
            continue


        # Calculate percentage
        if result.total_questions > 0:

            percentage = round(
                (
                    result.score
                    / result.total_questions
                ) * 100
            )

        else:

            percentage = 0


        # Date
        exam_date = result.created_at.strftime(
            "%d %b %Y"
        )


        # Time
        exam_time = result.created_at.strftime(
            "%I:%M %p"
        )


        progress_data.append(
            {
                "subject": result.subject,
                "percentage": percentage,
                "score": result.score,
                "total_questions": result.total_questions,
                "date": exam_date,
                "time": exam_time,
            }
        )


    # --------------------------------------------------------
    # Check whether selected subject has attempts
    # --------------------------------------------------------

    has_progress = len(progress_data) > 0


    # --------------------------------------------------------
    # Send data to template
    # --------------------------------------------------------

    context = {

        "student": student,

        "subjects": subjects,

        "selected_subject": selected_subject,

        "progress_data": progress_data,

        "has_progress": has_progress,

    }


    return render(
        request,
        "accounts/progress.html",
        context
    )