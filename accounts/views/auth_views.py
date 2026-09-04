import re
import random
import requests

from django.shortcuts import render, redirect
from django.conf import settings

from accounts.models import Student


def validate_password(password):

    if len(password) != 7:
        return "Password must contain exactly 7 characters."

    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    numbers = re.findall(r"[0-9]", password)

    if len(numbers) < 1:
        return "Password must contain at least one number."

    if len(numbers) > 2:
        return "Password can contain maximum two numbers."

    special_characters = re.findall(
        r"[^a-zA-Z0-9]",
        password
    )

    if len(special_characters) != 1:
        return "Password must contain exactly one special character."

    return None


def register(request):

    if request.method == "POST":

        name = request.POST.get(
            "name",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        confirm_password = request.POST.get(
            "confirm_password",
            ""
        )

        phone = request.POST.get(
            "phone",
            ""
        ).strip()

        year = request.POST.get(
            "btech_year",
            ""
        )

        if password != confirm_password:

            return render(
                request,
                "accounts/register.html",
                {
                    "error": "Passwords do not match"
                }
            )

        if Student.objects.filter(
            email=email
        ).exists():

            return render(
                request,
                "accounts/register.html",
                {
                    "error": "Email already exists"
                }
            )

        if not re.fullmatch(
            r"[6-9][0-9]{9}",
            phone
        ):

            return render(
                request,
                "accounts/register.html",
                {
                    "error":
                    "Mobile number must contain exactly 10 digits and start with 6, 7, 8, or 9."
                }
            )

        student = Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=password,
            year=year
        )

        request.session["student_id"] = student.id
        request.session["student_name"] = student.name
        request.session["student_email"] = student.email

        return redirect("/dashboard/")

    return render(
        request,
        "accounts/register.html"
    )


def login_view(request):

    if request.method == "POST":

        email = request.POST.get(
            "email",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        email_pattern = r"^[a-z0-9#]+@intell\.com$"

        if not re.fullmatch(
            email_pattern,
            email
        ):

            return render(
                request,
                "accounts/login.html",
                {
                    "error":
                    "Invalid email. Use lowercase letters, numbers or # and @intell.com"
                }
            )

        password_error = validate_password(
            password
        )

        if password_error:

            return render(
                request,
                "accounts/login.html",
                {
                    "error": password_error,
                    "email": email
                }
            )

        try:

            student = Student.objects.get(
                email=email
            )

        except Student.DoesNotExist:

            return render(
                request,
                "accounts/login.html",
                {
                    "error":
                    "Email or password is incorrect."
                }
            )

        if password != student.password:

            return render(
                request,
                "accounts/login.html",
                {
                    "error":
                    "Email or password is incorrect."
                }
            )

        request.session["student_id"] = student.id
        request.session["student_name"] = student.name
        request.session["student_email"] = student.email

        return redirect("/dashboard/")

    return render(
        request,
        "accounts/login.html"
    )


def forgot_password(request):

    if request.method == "POST":

        phone = request.POST.get(
            "phone",
            ""
        ).strip()

        if not phone.isdigit() or len(phone) != 10:

            return render(
                request,
                "accounts/forgot_password.html",
                {
                    "error":
                    "Enter a valid 10-digit mobile number."
                }
            )

        if phone[0] not in "6789":

            return render(
                request,
                "accounts/forgot_password.html",
                {
                    "error":
                    "Mobile number must start with 6, 7, 8 or 9."
                }
            )

        try:

            student = Student.objects.get(
                phone=phone
            )

        except Student.DoesNotExist:

            return render(
                request,
                "accounts/forgot_password.html",
                {
                    "error":
                    "This phone number is not registered."
                }
            )

        otp = str(
            random.randint(
                100000,
                999999
            )
        )

        request.session["reset_student_id"] = student.id
        request.session["reset_phone"] = phone
        request.session["reset_otp"] = otp

        mobile = "91" + phone

        url = "https://control.msg91.com/api/v5/otp"

        params = {
            "template_id":
            settings.MSG91_TEMPLATE_ID,

            "mobile":
            mobile,

            "authkey":
            settings.MSG91_AUTHKEY
        }

        data = {
            "OTP": otp
        }

        headers = {
            "Content-Type":
            "application/json"
        }

        try:

            response = requests.post(
                url,
                params=params,
                json=data,
                headers=headers,
                timeout=10
            )

            result = response.json()

            print(
                "MSG91 RESPONSE:",
                result
            )

            if result.get("type") != "success":

                request.session.pop(
                    "reset_otp",
                    None
                )

                request.session.pop(
                    "reset_student_id",
                    None
                )

                request.session.pop(
                    "reset_phone",
                    None
                )

                return render(
                    request,
                    "accounts/forgot_password.html",
                    {
                        "error":
                        "Unable to send OTP. Please try again."
                    }
                )

        except requests.RequestException as e:

            print(
                "SMS ERROR:",
                e
            )

            request.session.pop(
                "reset_otp",
                None
            )

            request.session.pop(
                "reset_student_id",
                None
            )

            request.session.pop(
                "reset_phone",
                None
            )

            return render(
                request,
                "accounts/forgot_password.html",
                {
                    "error":
                    "SMS service is unavailable. Please try again."
                }
            )

        print("-----------------------")
        print("OTP:", otp)
        print(
            "OTP SMS sent to:",
            phone
        )
        print("------------------------")

        return redirect(
            "/verify-otp/"
        )

    return render(
        request,
        "accounts/forgot_password.html"
    )


def verify_otp(request):

    if request.method == "POST":

        entered_otp = request.POST.get(
            "otp",
            ""
        ).strip()

        if (
            len(entered_otp) != 6
            or not entered_otp.isdigit()
        ):

            return render(
                request,
                "accounts/verify_otp.html",
                {
                    "error":
                    "OTP must contain exactly 6 digits."
                }
            )

        saved_otp = request.session.get(
            "reset_otp"
        )

        if not saved_otp:

            return render(
                request,
                "accounts/verify_otp.html",
                {
                    "error":
                    "OTP expired or invalid. Please request a new OTP."
                }
            )

        if entered_otp != saved_otp:

            return render(
                request,
                "accounts/verify_otp.html",
                {
                    "error":
                    "Invalid OTP. Please try again."
                }
            )

        student_id = request.session.get(
            "reset_student_id"
        )

        if not student_id:

            return render(
                request,
                "accounts/verify_otp.html",
                {
                    "error":
                    "Session expired. Please request a new OTP."
                }
            )

        request.session[
            "verified_student_id"
        ] = student_id

        request.session.pop(
            "reset_otp",
            None
        )

        request.session.pop(
            "reset_student_id",
            None
        )

        request.session.pop(
            "reset_phone",
            None
        )

        return redirect(
            "/reset-password/"
        )

    return render(
        request,
        "accounts/verify_otp.html"
    )


def reset_password(request):

    student_id = request.session.get(
        "verified_student_id"
    )

    if not student_id:
        return redirect("/login/")

    try:

        student = Student.objects.get(
            id=student_id
        )

    except Student.DoesNotExist:

        return redirect("/login/")

    if request.method == "POST":

        new_password = request.POST.get(
            "password",
            ""
        ).strip()

        confirm_password = request.POST.get(
            "confirm_password",
            ""
        ).strip()

        if new_password != confirm_password:

            return render(
                request,
                "accounts/reset_password.html",
                {
                    "error":
                    "Passwords do not match."
                }
            )

        if len(new_password) != 7:

            return render(
                request,
                "accounts/reset_password.html",
                {
                    "error":
                    "Password must contain exactly 7 characters."
                }
            )

        if not any(
            c.isupper()
            for c in new_password
        ):

            return render(
                request,
                "accounts/reset_password.html",
                {
                    "error":
                    "Password must contain at least one uppercase letter."
                }
            )

        numbers = sum(
            c.isdigit()
            for c in new_password
        )

        if numbers < 1 or numbers > 2:

            return render(
                request,
                "accounts/reset_password.html",
                {
                    "error":
                    "Password must contain 1 or 2 numbers."
                }
            )

        special = sum(
            not c.isalnum()
            for c in new_password
        )

        if special != 1:

            return render(
                request,
                "accounts/reset_password.html",
                {
                    "error":
                    "Password must contain exactly one special character."
                }
            )

        student.password = new_password
        student.save()

        request.session.pop(
            "verified_student_id",
            None
        )

        return redirect("/login/")

    return render(
        request,
        "accounts/reset_password.html"
    )


def otp_success(request):

    student_id = request.session.get(
        "verified_student_id"
    )

    if not student_id:
        return redirect("/login/")

    try:

        student = Student.objects.get(
            id=student_id
        )

    except Student.DoesNotExist:

        return redirect("/login/")

    request.session["student_id"] = student.id
    request.session["student_name"] = student.name
    request.session["student_email"] = student.email

    request.session.pop(
        "verified_student_id",
        None
    )

    return redirect("/dashboard/")