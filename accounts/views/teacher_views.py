from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Teacher, Question


# =========================================================
# TEACHER REGISTER
# =========================================================

def teacher_register(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if Teacher.objects.filter(email=email).exists():

            return render(
                request,
                "accounts/teacher_register.html",
                {
                    "error": "Teacher with this email already exists."
                }
            )

        Teacher.objects.create(
            name=name,
            email=email,
            password=password
        )

        return redirect("teacher_login")

    return render(
        request,
        "accounts/teacher_register.html"
    )


# =========================================================
# TEACHER LOGIN
# =========================================================

def teacher_login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:

            teacher = Teacher.objects.get(
                email=email,
                password=password
            )

            request.session["teacher_id"] = teacher.id

            return redirect("teacher_dashboard")

        except Teacher.DoesNotExist:

            return render(
                request,
                "accounts/student_login.html",
                {
                    "error": "Invalid teacher email or password.",
                    "email": email
                }
            )

    return redirect("login")


# =========================================================
# TEACHER DASHBOARD
# =========================================================

def teacher_dashboard(request):

    teacher_id = request.session.get("teacher_id")

    if not teacher_id:

        return redirect("teacher_login")

    try:

        teacher = Teacher.objects.get(
            id=teacher_id
        )

    except Teacher.DoesNotExist:

        request.session.pop(
            "teacher_id",
            None
        )

        return redirect("teacher_login")

    return render(
        request,
        "accounts/teacher_dashboard.html",
        {
            "teacher": teacher
        }
    )


# =========================================================
# ADD QUESTION
# =========================================================

def add_question(request):

    teacher_id = request.session.get("teacher_id")

    if not teacher_id:

        return redirect("teacher_login")

    if request.method == "POST":

        subject = request.POST.get("subject")

        topic = request.POST.get("topic")

        question_type = request.POST.get(
            "question_type"
        )

        question = request.POST.get(
            "question"
        )

        option1 = request.POST.get(
            "option1",
            ""
        )

        option2 = request.POST.get(
            "option2",
            ""
        )

        option3 = request.POST.get(
            "option3",
            ""
        )

        option4 = request.POST.get(
            "option4",
            ""
        )

        answer = request.POST.get(
            "answer"
        )

        Question.objects.create(

            subject=subject,

            topic=topic,

            question_type=question_type,

            question=question,

            option1=option1,

            option2=option2,

            option3=option3,

            option4=option4,

            answer=answer

        )

        return redirect(
            "question_bank"
        )

    return render(
        request,
        "accounts/add_question.html"
    )


# =========================================================
# QUESTION BANK
# =========================================================

def question_bank(request):

    teacher_id = request.session.get(
        "teacher_id"
    )

    if not teacher_id:

        return redirect(
            "teacher_login"
        )

    # Selected subject

    selected_subject = request.GET.get(
        "subject",
        ""
    )

    # Get all questions

    questions = Question.objects.all().order_by(

        "subject",

        "topic",

        "id"

    )

    # Filter by subject

    if selected_subject:

        questions = questions.filter(

            subject=selected_subject

        )

    return render(

        request,

        "accounts/question_bank.html",

        {
            "questions": questions,

            "selected_subject": selected_subject
        }

    )


# =========================================================
# MODIFY QUESTION
# =========================================================

def modify_question(
    request,
    question_id
):

    teacher_id = request.session.get(
        "teacher_id"
    )

    if not teacher_id:

        return redirect(
            "teacher_login"
        )

    question = get_object_or_404(

        Question,

        id=question_id

    )

    if request.method == "POST":

        question.subject = request.POST.get(
            "subject"
        )

        question.topic = request.POST.get(
            "topic"
        )

        question.question_type = request.POST.get(
            "question_type"
        )

        question.question = request.POST.get(
            "question"
        )

        question.option1 = request.POST.get(
            "option1",
            ""
        )

        question.option2 = request.POST.get(
            "option2",
            ""
        )

        question.option3 = request.POST.get(
            "option3",
            ""
        )

        question.option4 = request.POST.get(
            "option4",
            ""
        )

        question.answer = request.POST.get(
            "answer"
        )

        question.save()

        return redirect(
            "question_bank"
        )

    return render(

        request,

        "accounts/modify_question.html",

        {
            "question": question
        }

    )


# =========================================================
# DELETE QUESTION
# =========================================================

def delete_question(
    request,
    question_id
):

    teacher_id = request.session.get(
        "teacher_id"
    )

    if not teacher_id:

        return redirect(
            "teacher_login"
        )

    question = get_object_or_404(

        Question,

        id=question_id

    )

    if request.method == "POST":

        question.delete()

    return redirect(
        "question_bank"
    )


# =========================================================
# TEACHER LOGOUT
# =========================================================

def teacher_logout(request):

    request.session.pop(
        "teacher_id",
        None
    )

    return redirect(
        "teacher_login"
    )