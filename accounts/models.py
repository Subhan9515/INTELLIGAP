from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True
    )
    password = models.CharField(max_length=128)
    year = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Question(models.Model):
    SUBJECTS = [
        ("Python", "Python"),
        ("Machine Learning", "Machine Learning"),
        ("DBMS", "DBMS"),
        ("Java", "Java"),
    ]

    QUESTION_TYPES = [
        ("MCQ", "MCQ"),
        ("FILL", "Fill in the Blank"),
        ("TEXT", "One Line Answer"),
    ]

    subject = models.CharField(
        max_length=50,
        choices=SUBJECTS
    )

    topic = models.CharField(max_length=100)

    question_type = models.CharField(
        max_length=10,
        choices=QUESTION_TYPES
    )

    question = models.TextField()

    option1 = models.CharField(
        max_length=200,
        blank=True
    )

    option2 = models.CharField(
        max_length=200,
        blank=True
    )

    option3 = models.CharField(
        max_length=200,
        blank=True
    )

    option4 = models.CharField(
        max_length=200,
        blank=True
    )

    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class QuizResult(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    subject = models.CharField(max_length=50)

    score = models.IntegerField(default=0)

    total_questions = models.IntegerField(default=0)

    correct_answers = models.IntegerField(default=0)

    wrong_answers = models.IntegerField(default=0)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.name} - {self.subject}"


class WrongAnswer(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    user_answer = models.CharField(
        max_length=200
    )

    correct_answer = models.CharField(
        max_length=200
    )

    topic = models.CharField(
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.question.question


class QuizAnswer(models.Model):
    quiz_result = models.ForeignKey(
        QuizResult,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    user_answer = models.CharField(
        max_length=200,
        blank=True
    )

    correct_answer = models.CharField(
        max_length=200
    )

    is_correct = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.quiz_result.subject} - {self.question.question}"