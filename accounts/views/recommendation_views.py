from django.shortcuts import render, redirect

from accounts.models import Student, QuizAnswer


def recommendation(request):

    # ==========================================
    # CHECK STUDENT LOGIN
    # ==========================================

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/login/")

    try:
        student = Student.objects.get(id=student_id)

    except Student.DoesNotExist:
        request.session.flush()
        return redirect("/login/")


    # ==========================================
    # SUBJECTS
    # ==========================================

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


    # ==========================================
    # SELECTED SUBJECT
    # ==========================================

    selected_subject = request.GET.get(
        "subject",
        ""
    )


    # ==========================================
    # GET STUDENT ANSWERS
    # ==========================================

    answers = QuizAnswer.objects.filter(
        quiz_result__student=student
    ).select_related(
        "question",
        "quiz_result"
    )


    # ==========================================
    # GROUP ANSWERS BY SUBJECT + TOPIC
    # ==========================================

    grouped_topics = {}


    for answer in answers:

        subject = answer.quiz_result.subject
        topic = answer.question.topic

        key = (
            subject,
            topic
        )


        if key not in grouped_topics:

            grouped_topics[key] = {
                "subject": subject,
                "topic": topic,
                "total": 0,
                "correct": 0
            }


        grouped_topics[key]["total"] += 1


        if answer.is_correct:

            grouped_topics[key]["correct"] += 1


    # ==========================================
    # CREATE TOPIC PERFORMANCE
    # ==========================================

    topic_data = []


    for data in grouped_topics.values():

        total = data["total"]
        correct = data["correct"]

        if total == 0:

            accuracy = 0

        else:

            accuracy = round(
                (correct / total) * 100,
                1
            )


        wrong = total - correct


        # ======================================
        # CLASSIFY PERFORMANCE
        # ======================================

        if accuracy < 50:

            level = "weak"

            priority = "High"

        elif accuracy < 75:

            level = "moderate"

            priority = "Medium"

        else:

            level = "strong"

            priority = "Low"


        # ======================================
        # CREATE STUDY RECOMMENDATION
        # ======================================

        recommendation_text = ""


        if level == "weak":

            recommendation_text = (
                f"Focus strongly on {data['topic']}. "
                f"Review the basic concepts first, "
                f"then practice questions related to "
                f"{data['topic']}."
            )

        elif level == "moderate":

            recommendation_text = (
                f"Revise the important concepts of "
                f"{data['topic']} and solve additional "
                f"practice questions to improve accuracy."
            )

        else:

            recommendation_text = (
                f"You are performing well in "
                f"{data['topic']}. "
                f"Continue practicing to maintain "
                f"your understanding."
            )


        # ======================================
        # STUDY TIME
        # ======================================

        if level == "weak":

            study_time = "30 minutes"

        elif level == "moderate":

            study_time = "20 minutes"

        else:

            study_time = "10 minutes"


        topic_data.append(
            {
                "subject": data["subject"],

                "topic": data["topic"],

                "total": total,

                "correct": correct,

                "wrong": wrong,

                "accuracy": accuracy,

                "level": level,

                "priority": priority,

                "recommendation": recommendation_text,

                "study_time": study_time,
            }
        )


    # ==========================================
    # FILTER SELECTED SUBJECT
    # ==========================================

    subject_topics = []


    if selected_subject:

        subject_topics = [

            item

            for item in topic_data

            if item["subject"] == selected_subject

        ]


    # ==========================================
    # SORT BY PRIORITY
    # ==========================================

    priority_order = {

        "High": 1,

        "Medium": 2,

        "Low": 3

    }


    subject_topics.sort(

        key=lambda item:
        priority_order[item["priority"]]

    )


    # ==========================================
    # SEPARATE TOPICS
    # ==========================================

    weak_topics = [

        item

        for item in subject_topics

        if item["level"] == "weak"

    ]


    moderate_topics = [

        item

        for item in subject_topics

        if item["level"] == "moderate"

    ]


    strong_topics = [

        item

        for item in subject_topics

        if item["level"] == "strong"

    ]


    # ==========================================
    # CHECK DATA
    # ==========================================

    has_data = answers.exists()


    # ==========================================
    # CONTEXT
    # ==========================================

    context = {

        "student": student,

        "subjects": subjects,

        "has_data": has_data,

        "selected_subject": selected_subject,

        "subject_topics": subject_topics,

        "weak_topics": weak_topics,

        "moderate_topics": moderate_topics,

        "strong_topics": strong_topics,

    }


    return render(

        request,

        "accounts/recommendation.html",

        context

    )