from django.shortcuts import render, redirect

from accounts.models import Student


def profile(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/login/")

    try:
        student = Student.objects.get(id=student_id)

    except Student.DoesNotExist:
        request.session.flush()
        return redirect("/login/")

    if request.method == "POST":

        if "profile_photo" in request.FILES:

            student.profile_photo = request.FILES["profile_photo"]
            student.save()

        return redirect("profile")

    return render(
        request,
        "accounts/profile.html",
        {
            "student": student,
        }
    )