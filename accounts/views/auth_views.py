import re
import random
import requests

from django.shortcuts import render, redirect
from django.conf import settings

from accounts.models import Student


# =========================================================
# PASSWORD VALIDATION
# =========================================================

def validate_password(password):

    # Minimum and maximum length
    if len(password) < 6 or len(password) > 10:
        return "Password must be between 6 and 10 characters."

    # At least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    # At least three numbers
    numbers = re.findall(r"[0-9]", password)

    if len(numbers) < 3:
        return "Password must contain at least three numbers."

    # At least one special character
    special_characters = re.findall(
        r"[^a-zA-Z0-9]",
        password
    )

    if len(special_characters) < 1:
        return "Password must contain at least one special symbol."

    return None


# =========================================================
# STUDENT REGISTER
# =========================================================

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


        # -------------------------------------------------
        # PASSWORD MATCH
        # -------------------------------------------------

        if password != confirm_password:

            return render(
                request,
                "accounts/register.html",
                {
                    "error": "Passwords do not match."
                }
            )


        # -------------------------------------------------
        # PASSWORD VALIDATION
        # -------------------------------------------------

        password_error = validate_password(password)

        if password_error:

            return render(
                request,
                "accounts/register.html",
                {
                    "error": password_error
                }
            )


        # -------------------------------------------------
        # EMAIL DUPLICATE CHECK
        # -------------------------------------------------

        if Student.objects.filter(
            email=email
        ).exists():

            return render(
                request,
                "accounts/register.html",
                {
                    "error":
                    "This email is already registered. Please use another email."
                }
            )


        # -------------------------------------------------
        # PHONE FORMAT CHECK
        # -------------------------------------------------

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


        # -------------------------------------------------
        # PHONE DUPLICATE CHECK
        # -------------------------------------------------

        if Student.objects.filter(
            phone=phone
        ).exists():

            return render(
                request,
                "accounts/register.html",
                {
                    "error":
                    "This mobile number is already registered. Please use another number."
                }
            )


        # -------------------------------------------------
        # CREATE STUDENT
        # -------------------------------------------------

        student = Student.objects.create(

            name=name,

            email=email,

            phone=phone,

            password=password,

            year=year

        )


        # -------------------------------------------------
        # SESSION
        # -------------------------------------------------

        request.session["student_id"] = student.id

        request.session["student_name"] = student.name

        request.session["student_email"] = student.email


        return redirect(
            "/dashboard/"
        )


    return render(
        request,
        "accounts/register.html"
    )


# =========================================================
# STUDENT LOGIN
# =========================================================

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


        # -------------------------------------------------
        # EMAIL FORMAT
        # -------------------------------------------------

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


        # -------------------------------------------------
        # FIND STUDENT
        # -------------------------------------------------

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


        # -------------------------------------------------
        # CHECK PASSWORD
        # -------------------------------------------------

        if password != student.password:

            return render(
                request,
                "accounts/login.html",
                {
                    "error":
                    "Email or password is incorrect."
                }
            )


        # -------------------------------------------------
        # SESSION
        # -------------------------------------------------

        request.session["student_id"] = student.id

        request.session["student_name"] = student.name

        request.session["student_email"] = student.email


        return redirect(
            "/dashboard/"
        )


    return render(
        request,
        "accounts/login.html"
    )


# =========================================================
# FORGOT PASSWORD
# =========================================================

def forgot_password(request):

    if request.method == "POST":

        phone = request.POST.get(
            "phone",
            ""
        ).strip()


        # -------------------------------------------------
        # PHONE VALIDATION
        # -------------------------------------------------

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


        # -------------------------------------------------
        # FIND STUDENT
        # -------------------------------------------------

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


        # -------------------------------------------------
        # GENERATE OTP
        # -------------------------------------------------

        otp = str(
            random.randint(
                100000,
                999999
            )
        )


        # -------------------------------------------------
        # SAVE RESET SESSION
        # -------------------------------------------------

        request.session["reset_student_id"] = student.id

        request.session["reset_phone"] = phone

        request.session["reset_otp"] = otp


        # -------------------------------------------------
        # MSG91
        # -------------------------------------------------

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


        print(
            "-----------------------"
        )

        print(
            "OTP:",
            otp
        )

        print(
            "OTP SMS sent to:",
            phone
        )

        print(
            "------------------------"
        )


        return redirect(
            "/verify-otp/"
        )


    return render(
        request,
        "accounts/forgot_password.html"
    )


# =========================================================
# VERIFY OTP
# =========================================================

def verify_otp(request):

    if request.method == "POST":

        entered_otp = request.POST.get(
            "otp",
            ""
        ).strip()


        # -------------------------------------------------
        # OTP FORMAT
        # -------------------------------------------------

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


        # -------------------------------------------------
        # GET SAVED OTP
        # -------------------------------------------------

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


        # -------------------------------------------------
        # COMPARE OTP
        # -------------------------------------------------

        if entered_otp != saved_otp:

            return render(
                request,
                "accounts/verify_otp.html",
                {
                    "error":
                    "Invalid OTP. Please try again."
                }
            )


        # -------------------------------------------------
        # STUDENT ID
        # -------------------------------------------------

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


        # -------------------------------------------------
        # MARK VERIFIED
        # -------------------------------------------------

        request.session[
            "verified_student_id"
        ] = student_id


        # -------------------------------------------------
        # CLEAR OTP SESSION
        # -------------------------------------------------

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


# =========================================================
# RESET PASSWORD
# =========================================================

def reset_password(request):

    student_id = request.session.get(
        "verified_student_id"
    )


    if not student_id:

        return redirect(
            "/login/"
        )


    # -----------------------------------------------------
    # GET STUDENT
    # -----------------------------------------------------

    try:

        student = Student.objects.get(
            id=student_id
        )

    except Student.DoesNotExist:

        return redirect(
            "/login/"
        )


    # -----------------------------------------------------
    # POST
    # -----------------------------------------------------

    if request.method == "POST":

        new_password = request.POST.get(
            "password",
            ""
        ).strip()

        confirm_password = request.POST.get(
            "confirm_password",
            ""
        ).strip()


        # -------------------------------------------------
        # PASSWORD MATCH
        # -------------------------------------------------

        if new_password != confirm_password:

            return render(
                request,
                "accounts/reset_password.html",
                {
                    "error":
                    "Passwords do not match."
                }
            )


        # -------------------------------------------------
        # PASSWORD VALIDATION
        # -------------------------------------------------

        password_error = validate_password(
            new_password
        )


        if password_error:

            return render(
                request,
                "accounts/reset_password.html",
                {
                    "error":
                    password_error
                }
            )


        # -------------------------------------------------
        # SAVE PASSWORD
        # -------------------------------------------------

        student.password = new_password

        student.save()


        # -------------------------------------------------
        # CLEAR SESSION
        # -------------------------------------------------

        request.session.pop(
            "verified_student_id",
            None
        )


        return redirect(
            "/login/"
        )


    return render(
        request,
        "accounts/reset_password.html"
    )


# =========================================================
# OTP SUCCESS
# =========================================================

def otp_success(request):

    student_id = request.session.get(
        "verified_student_id"
    )


    if not student_id:

        return redirect(
            "/login/"
        )


    try:

        student = Student.objects.get(
            id=student_id
        )

    except Student.DoesNotExist:

        return redirect(
            "/login/"
        )


    request.session["student_id"] = student.id

    request.session["student_name"] = student.name

    request.session["student_email"] = student.email


    request.session.pop(
        "verified_student_id",
        None
    )


    return redirect(
        "/dashboard/"
    )