from django.shortcuts import render, redirect
from collections import Counter
from .models import Student
from .models import Question
import random
from .models import QuizResult,WrongAnswer


def dashboard(request):
    latest = QuizResult.objects.order_by("-id").first()

    return render(request, "accounts/dashboard.html", {
        "latest": latest
    })
def load_ml_questions():
    questions = [
        {
            "subject": "Machine Learning",
            "topic": "Introduction",
            "question_type": "MCQ",
            "question": "What is Machine Learning?",
            "option1": "A programming language",
            "option2": "A type of AI",
            "option3": "An operating system",
            "option4": "A database",
            "answer": "A type of AI",
        },
        {
            "subject":"Machine Learning",
            "topic":"Introduction",
            "question_type":"MCQ",
            "question":"What is Machine Learning?",
            "option1":"Programming Language",
            "option2":"Artificial Intelligence",
            "option3":"Database",
            "option4":"Operating System",
            "answer":"Artificial Intelligence",
        },

        {
            "subject":"Machine Learning",
            "topic":"Introduction",
            "question_type":"MCQ",
            "question":"Machine Learning is a subset of?",
            "option1":"AI",
            "option2":"DBMS",
            "option3":"Networking",
            "option4":"Cloud",
            "answer":"AI",
        },

        {
            "subject":"Machine Learning",
            "topic":"Supervised Learning",
            "question_type":"MCQ",
            "question":"Which learning uses labeled data?",
            "option1":"Supervised Learning",
            "option2":"Unsupervised Learning",
            "option3":"Reinforcement Learning",
            "option4":"None",
            "answer":"Supervised Learning",
        },

        {
            "subject":"Machine Learning",
            "topic":"Unsupervised Learning",
            "question_type":"MCQ",
            "question":"Which learning uses unlabeled data?",
            "option1":"Supervised Learning",
            "option2":"Unsupervised Learning",
            "option3":"Deep Learning",
            "option4":"Regression",
            "answer":"Unsupervised Learning",
        },

        {
            "subject":"Machine Learning",
            "topic":"Algorithms",
            "question_type":"MCQ",
            "question":"Which algorithm is used for classification?",
            "option1":"Decision Tree",
            "option2":"Bubble Sort",
            "option3":"Quick Sort",
            "option4":"Merge Sort",
            "answer":"Decision Tree",
        },

        {
            "subject":"Machine Learning",
            "topic":"Regression",
            "question_type":"MCQ",
            "question":"Linear Regression is used for?",
            "option1":"Prediction",
            "option2":"Sorting",
            "option3":"Searching",
            "option4":"Compilation",
            "answer":"Prediction",
        },

        {
            "subject":"Machine Learning",
            "topic":"Clustering",
            "question_type":"MCQ",
            "question":"Which algorithm is used for clustering?",
            "option1":"K-Means",
            "option2":"Linear Regression",
            "option3":"Naive Bayes",
            "option4":"SVM",
            "answer":"K-Means",
        },

        {
            "subject":"Machine Learning",
            "topic":"Algorithms",
            "question_type":"MCQ",
            "question":"SVM stands for?",
            "option1":"Support Vector Machine",
            "option2":"System Virtual Machine",
            "option3":"Simple Vector Method",
            "option4":"Software Virtual Machine",
            "answer":"Support Vector Machine",
        },

        {
            "subject":"Machine Learning",
            "topic":"Evaluation",
            "question_type":"MCQ",
            "question":"Accuracy is used to measure?",
            "option1":"Model Performance",
            "option2":"Database Size",
            "option3":"Memory",
            "option4":"Speed",
            "answer":"Model Performance",
        },

        {
            "subject":"Machine Learning",
            "topic":"Deep Learning",
            "question_type":"MCQ",
            "question":"Deep Learning uses?",
            "option1":"Neural Networks",
            "option2":"Stack",
            "option3":"Queue",
            "option4":"Linked List",
            "answer":"Neural Networks",
        },

        {
            "subject":"Machine Learning",
            "topic":"Dataset",
            "question_type":"MCQ",
            "question":"Data used to train a model is called?",
            "option1":"Training Data",
            "option2":"Testing Data",
            "option3":"Validation",
            "option4":"Output",
            "answer":"Training Data",
        },

        {
            "subject":"Machine Learning",
            "topic":"Dataset",
            "question_type":"MCQ",
            "question":"Data used to evaluate a model is called?",
            "option1":"Testing Data",
            "option2":"Training Data",
            "option3":"Input",
            "option4":"Label",
            "answer":"Testing Data",
        },

        {
            "subject":"Machine Learning",
            "topic":"Algorithms",
            "question_type":"MCQ",
            "question":"Which algorithm is used for classification and regression?",
            "option1":"Decision Tree",
            "option2":"K-Means",
            "option3":"Apriori",
            "option4":"PageRank",
            "answer":"Decision Tree",
        },

        {
            "subject":"Machine Learning",
            "topic":"Applications",
            "question_type":"MCQ",
            "question":"Machine Learning is used in?",
            "option1":"Recommendation Systems",
            "option2":"Weather Prediction",
            "option3":"Spam Detection",
            "option4":"All of the Above",
            "answer":"All of the Above",
        },

        {
            "subject":"Machine Learning",
            "topic":"Applications",
            "question_type":"MCQ",
            "question":"Which company widely uses Machine Learning?",
            "option1":"Google",
            "option2":"Microsoft",
            "option3":"Amazon",
            "option4":"All of the Above",
            "answer":"All of the Above",
        },
        {   "subject":"Machine Learning",
            "topic":"Introduction",
"question_type":"FILL",
"question":"Machine Learning is a subset of ________.",
"answer":"Artificial Intelligence",
},

{
"subject":"Machine Learning",
"topic":"Introduction",
"question_type":"FILL",
"question":"The data used to train a model is called ________ data.",
"answer":"Training",
},

{
"subject":"Machine Learning",
"topic":"Introduction",
"question_type":"FILL",
"question":"The data used to test a model is called ________ data.",
"answer":"Testing",
},

{
"subject":"Machine Learning",
"topic":"Supervised Learning",
"question_type":"FILL",
"question":"________ Learning uses labeled data.",
"answer":"Supervised",
},

{
"subject":"Machine Learning",
"topic":"Unsupervised Learning",
"question_type":"FILL",
"question":"________ Learning uses unlabeled data.",
"answer":"Unsupervised",
},

{
"subject":"Machine Learning",
"topic":"Algorithms",
"question_type":"FILL",
"question":"K-Means is a ________ algorithm.",
"answer":"Clustering",
},

{
"subject":"Machine Learning",
"topic":"Algorithms",
"question_type":"FILL",
"question":"SVM stands for Support Vector ________.",
"answer":"Machine",
},

{
"subject":"Machine Learning",
"topic":"Regression",
"question_type":"FILL",
"question":"Linear Regression is used for ________ values.",
"answer":"Predicting",
},

{
"subject":"Machine Learning",
"topic":"Evaluation",
"question_type":"FILL",
"question":"The percentage of correct predictions is called ________.",
"answer":"Accuracy",
},

{
"subject":"Machine Learning",
"topic":"Deep Learning",
"question_type":"FILL",
"question":"Deep Learning mainly uses ________ Networks.",
"answer":"Neural",
},

{
"subject":"Machine Learning",
"topic":"Algorithms",
"question_type":"FILL",
"question":"Decision Tree is mainly used for ________ and regression.",
"answer":"Classification",
},

{
"subject":"Machine Learning",
"topic":"Applications",
"question_type":"FILL",
"question":"Email spam detection is an application of ________ Learning.",
"answer":"Machine",
},

{
"subject":"Machine Learning",
"topic":"Dataset",
"question_type":"FILL",
"question":"The input values of a dataset are called ________.",
"answer":"Features",
},

{
"subject":"Machine Learning",
"topic":"Dataset",
"question_type":"FILL",
"question":"The expected output of a dataset is called the ________.",
"answer":"Label",
},

{
"subject":"Machine Learning",
"topic":"Applications",
"question_type":"FILL",
"question":"Netflix uses Machine Learning for movie ________.",
"answer":"Recommendation",
},
{
"subject":"Machine Learning",
"topic":"Algorithms",
"question_type":"MCQ",
"question":"Which algorithm is used for clustering?",
"option1":"K-Means",
"option2":"Linear Regression",
"option3":"Decision Tree",
"option4":"Naive Bayes",
"answer":"K-Means",
},

{
"subject":"Machine Learning",
"topic":"Algorithms",
"question_type":"MCQ",
"question":"Which algorithm is based on Bayes theorem?",
"option1":"Naive Bayes",
"option2":"KNN",
"option3":"SVM",
"option4":"Random Forest",
"answer":"Naive Bayes",
},

{
"subject":"Machine Learning",
"topic":"Evaluation",
"question_type":"MCQ",
"question":"Which metric measures correct predictions?",
"option1":"Accuracy",
"option2":"Speed",
"option3":"Memory",
"option4":"Bandwidth",
"answer":"Accuracy",
},

{
"subject":"Machine Learning",
"topic":"Algorithms",
"question_type":"MCQ",
"question":"Which algorithm is an ensemble method?",
"option1":"Random Forest",
"option2":"KNN",
"option3":"K-Means",
"option4":"SVM",
"answer":"Random Forest",
},

{
"subject":"Machine Learning",
"topic":"Deep Learning",
"question_type":"MCQ",
"question":"CNN is mainly used for?",
"option1":"Image Processing",
"option2":"Database",
"option3":"Networking",
"option4":"Sorting",
"answer":"Image Processing",
},

{
"subject":"Machine Learning",
"topic":"Deep Learning",
"question_type":"MCQ",
"question":"RNN is mainly used for?",
"option1":"Sequential Data",
"option2":"Sorting",
"option3":"Compression",
"option4":"Searching",
"answer":"Sequential Data",
},

{
"subject":"Machine Learning",
"topic":"Applications",
"question_type":"MCQ",
"question":"Which is an application of Machine Learning?",
"option1":"Spam Detection",
"option2":"Recommendation System",
"option3":"Fraud Detection",
"option4":"All of the Above",
"answer":"All of the Above",
},

{
"subject":"Machine Learning",
"topic":"Evaluation",
"question_type":"MCQ",
"question":"Overfitting means?",
"option1":"Model memorizes training data",
"option2":"Model never trains",
"option3":"Model deletes data",
"option4":"Model compresses files",
"answer":"Model memorizes training data",
},

{
"subject":"Machine Learning",
"topic":"Dataset",
"question_type":"MCQ",
"question":"Which library is widely used for Machine Learning in Python?",
"option1":"Scikit-learn",
"option2":"NumPy",
"option3":"Pandas",
"option4":"All of the Above",
"answer":"Scikit-learn",
},

{
"subject":"Machine Learning",
"topic":"Algorithms",
"question_type":"MCQ",
"question":"Which algorithm is commonly used for classification?",
"option1":"Decision Tree",
"option2":"Bubble Sort",
"option3":"Quick Sort",
"option4":"Merge Sort",
"answer":"Decision Tree",
},
{
"subject":"Machine Learning",
"topic":"Algorithms",
"question_type":"FILL",
"question":"Random Forest is an ________ learning algorithm.",
"answer":"Ensemble",
},

{
"subject":"Machine Learning",
"topic":"Algorithms",
"question_type":"FILL",
"question":"Naive Bayes is based on ________ theorem.",
"answer":"Bayes",
},

{
"subject":"Machine Learning",
"topic":"Evaluation",
"question_type":"FILL",
"question":"A model that performs well on unseen data is said to ________ well.",
"answer":"Generalize",
},

{
"subject":"Machine Learning",
"topic":"Dataset",
"question_type":"FILL",
"question":"The process of cleaning data is called data ________.",
"answer":"Preprocessing",
},

{
"subject":"Machine Learning",
"topic":"Algorithms",
"question_type":"FILL",
"question":"The full form of CNN is Convolutional Neural ________.",
"answer":"Network",
},

{
"subject":"Machine Learning",
"topic":"Algorithms",
"question_type":"FILL",
"question":"The full form of RNN is Recurrent Neural ________.",
"answer":"Network",
},

{
"subject":"Machine Learning",
"topic":"Evaluation",
"question_type":"FILL",
"question":"Overfitting occurs when a model learns the ________ data too well.",
"answer":"Training",
},

{
"subject":"Machine Learning",
"topic":"Evaluation",
"question_type":"FILL",
"question":"The opposite of overfitting is ________.",
"answer":"Underfitting",
},

{
"subject":"Machine Learning",
"topic":"Applications",
"question_type":"FILL",
"question":"Face recognition is an application of ________ Learning.",
"answer":"Machine",
},

{
"subject":"Machine Learning",
"topic":"Applications",
"question_type":"FILL",
"question":"Speech recognition is widely used in virtual ________.",
"answer":"Assistants",
},
{
    "subject": "Java",
    "topic": "Data Types",
    "question_type": "MCQ",
    "question": "Which data type is used to store a single character in Java?",
    "option1": "char",
    "option2": "String",
    "option3": "character",
    "option4": "byte",
    "answer": "char",
},

{
    "subject": "Java",
    "topic": "Data Types",
    "question_type": "MCQ",
    "question": "Which data type is used to store decimal values?",
    "option1": "int",
    "option2": "float",
    "option3": "char",
    "option4": "boolean",
    "answer": "float",
},

{
    "subject": "Java",
    "topic": "OOP",
    "question_type": "MCQ",
    "question": "Which OOP concept hides implementation details?",
    "option1": "Inheritance",
    "option2": "Abstraction",
    "option3": "Polymorphism",
    "option4": "Encapsulation",
    "answer": "Abstraction",
},

{
    "subject": "Java",
    "topic": "OOP",
    "question_type": "MCQ",
    "question": "Which OOP concept binds data and methods together?",
    "option1": "Encapsulation",
    "option2": "Inheritance",
    "option3": "Abstraction",
    "option4": "Compilation",
    "answer": "Encapsulation",
},

{
    "subject": "Java",
    "topic": "Polymorphism",
    "question_type": "MCQ",
    "question": "Method overloading is an example of?",
    "option1": "Compile-time polymorphism",
    "option2": "Run-time polymorphism",
    "option3": "Inheritance",
    "option4": "Abstraction",
    "answer": "Compile-time polymorphism",
},

{
    "subject": "Java",
    "topic": "Polymorphism",
    "question_type": "MCQ",
    "question": "Method overriding is an example of?",
    "option1": "Compile-time polymorphism",
    "option2": "Run-time polymorphism",
    "option3": "Encapsulation",
    "option4": "Compilation",
    "answer": "Run-time polymorphism",
},

{
    "subject": "Java",
    "topic": "Arrays",
    "question_type": "MCQ",
    "question": "Which property is used to find the length of an array?",
    "option1": "length",
    "option2": "size()",
    "option3": "length()",
    "option4": "count()",
    "answer": "length",
},

{
    "subject": "Java",
    "topic": "Strings",
    "question_type": "MCQ",
    "question": "Which method is used to find the length of a String?",
    "option1": "length()",
    "option2": "size()",
    "option3": "count()",
    "option4": "length",
    "answer": "length()",
},

{
    "subject": "Java",
    "topic": "Exception Handling",
    "question_type": "MCQ",
    "question": "Which keyword is used to handle an exception?",
    "option1": "try",
    "option2": "catch",
    "option3": "throw",
    "option4": "error",
    "answer": "catch",
},

{
    "subject": "Java",
    "topic": "Exception Handling",
    "question_type": "MCQ",
    "question": "Which block is executed whether an exception occurs or not?",
    "option1": "try",
    "option2": "catch",
    "option3": "finally",
    "option4": "throw",
    "answer": "finally",
},{
    "subject": "Java",
    "topic": "Basics",
    "question_type": "FILL",
    "question": "Java source code is saved with the ________ extension.",
    "answer": ".java",
},

{
    "subject": "Java",
    "topic": "Data Types",
    "question_type": "FILL",
    "question": "The ________ data type stores true or false values.",
    "answer": "boolean",
},

{
    "subject": "Java",
    "topic": "OOP",
    "question_type": "FILL",
    "question": "The process of wrapping data and methods into a single unit is called ________.",
    "answer": "Encapsulation",
},

{
    "subject": "Java",
    "topic": "OOP",
    "question_type": "FILL",
    "question": "The process of acquiring properties from another class is called ________.",
    "answer": "Inheritance",
},

{
    "subject": "Java",
    "topic": "Polymorphism",
    "question_type": "FILL",
    "question": "The ability of an object to take many forms is called ________.",
    "answer": "Polymorphism",
},

{
    "subject": "Java",
    "topic": "Arrays",
    "question_type": "FILL",
    "question": "An array in Java stores multiple values of the same ________.",
    "answer": "type",
},

{
    "subject": "Java",
    "topic": "Strings",
    "question_type": "FILL",
    "question": "The ________ class is used to create immutable strings in Java.",
    "answer": "String",
},

{
    "subject": "Java",
    "topic": "Exception Handling",
    "question_type": "FILL",
    "question": "The ________ keyword is used to explicitly throw an exception.",
    "answer": "throw",
},

{
    "subject": "Java",
    "topic": "Exception Handling",
    "question_type": "FILL",
    "question": "The ________ keyword is used to declare exceptions that a method may throw.",
    "answer": "throws",
},

{
    "subject": "Java",
    "topic": "OOP",
    "question_type": "FILL",
    "question": "The keyword used to refer to the current object is ________.",
    "answer": "this",
},{
    "subject": "Java",
    "topic": "Access Modifiers",
    "question_type": "MCQ",
    "question": "Which access modifier allows access from anywhere?",
    "option1": "private",
    "option2": "protected",
    "option3": "public",
    "option4": "default",
    "answer": "public",
},

{
    "subject": "Java",
    "topic": "Access Modifiers",
    "question_type": "MCQ",
    "question": "Which access modifier provides the most restricted access?",
    "option1": "public",
    "option2": "protected",
    "option3": "private",
    "option4": "default",
    "answer": "private",
},

{
    "subject": "Java",
    "topic": "Constructors",
    "question_type": "MCQ",
    "question": "Which method is automatically called when an object is created?",
    "option1": "Constructor",
    "option2": "main()",
    "option3": "start()",
    "option4": "execute()",
    "answer": "Constructor",
},

{
    "subject": "Java",
    "topic": "Constructors",
    "question_type": "MCQ",
    "question": "What is the name of a constructor?",
    "option1": "Any name",
    "option2": "Same as the class name",
    "option3": "main",
    "option4": "new",
    "answer": "Same as the class name",
},

{
    "subject": "Java",
    "topic": "Interfaces",
    "question_type": "MCQ",
    "question": "Which keyword is used to declare an interface?",
    "option1": "interface",
    "option2": "implements",
    "option3": "abstract",
    "option4": "class",
    "answer": "interface",
},

{
    "subject": "Java",
    "topic": "Interfaces",
    "question_type": "MCQ",
    "question": "A class uses which keyword to implement an interface?",
    "option1": "extends",
    "option2": "implements",
    "option3": "interface",
    "option4": "inherits",
    "answer": "implements",
},

{
    "subject": "Java",
    "topic": "Keywords",
    "question_type": "MCQ",
    "question": "Which keyword refers to the parent class?",
    "option1": "this",
    "option2": "super",
    "option3": "parent",
    "option4": "base",
    "answer": "super",
},

{
    "subject": "Java",
    "topic": "Keywords",
    "question_type": "MCQ",
    "question": "Which keyword prevents a class from being inherited?",
    "option1": "static",
    "option2": "final",
    "option3": "private",
    "option4": "constant",
    "answer": "final",
},

{
    "subject": "Java",
    "topic": "Collections",
    "question_type": "MCQ",
    "question": "Which collection allows duplicate elements?",
    "option1": "Set",
    "option2": "List",
    "option3": "Map",
    "option4": "None",
    "answer": "List",
},

{
    "subject": "Java",
    "topic": "Collections",
    "question_type": "MCQ",
    "question": "Which collection stores key-value pairs?",
    "option1": "List",
    "option2": "Set",
    "option3": "Map",
    "option4": "Queue",
    "answer": "Map",
},{
    "subject": "Java",
    "topic": "Access Modifiers",
    "question_type": "FILL",
    "question": "The ________ keyword provides access from anywhere.",
    "answer": "public",
},

{
    "subject": "Java",
    "topic": "Access Modifiers",
    "question_type": "FILL",
    "question": "The ________ keyword provides the most restricted access.",
    "answer": "private",
},

{
    "subject": "Java",
    "topic": "Constructors",
    "question_type": "FILL",
    "question": "A constructor has the same name as the ________.",
    "answer": "class",
},

{
    "subject": "Java",
    "topic": "Constructors",
    "question_type": "FILL",
    "question": "A constructor is called automatically when an ________ is created.",
    "answer": "object",
},

{
    "subject": "Java",
    "topic": "Interfaces",
    "question_type": "FILL",
    "question": "The ________ keyword is used to declare an interface.",
    "answer": "interface",
},

{
    "subject": "Java",
    "topic": "Interfaces",
    "question_type": "FILL",
    "question": "The ________ keyword is used when a class implements an interface.",
    "answer": "implements",
},

{
    "subject": "Java",
    "topic": "Keywords",
    "question_type": "FILL",
    "question": "The ________ keyword refers to the parent class.",
    "answer": "super",
},

{
    "subject": "Java",
    "topic": "Keywords",
    "question_type": "FILL",
    "question": "The ________ keyword prevents a class from being inherited.",
    "answer": "final",
},

{
    "subject": "Java",
    "topic": "Collections",
    "question_type": "FILL",
    "question": "A ________ stores elements in key-value pairs.",
    "answer": "Map",
},

{
    "subject": "Java",
    "topic": "Collections",
    "question_type": "FILL",
    "question": "A ________ collection does not allow duplicate elements.",
    "answer": "Set",
}

    ]
    for q in questions:
        Question.objects.get_or_create(
            question=q["question"],
            defaults=q
        )        
def load_dbms_questions():
    questions = [
        {
            "subject": "DBMS",
            "topic": "SQL",
            "question_type": "MCQ",
            "question": "What does DBMS stand for?",
            "option1": "Database Management System",
            "option2": "Digital Base Management System",
            "option3": "Data Backup Machine",
            "option4": "None",
            "answer": "Database Management System",
        },
        {
    "subject":"DBMS",
    "topic":"Introduction",
    "question_type":"MCQ",
    "question":"What does DBMS stand for?",
    "option1":"Database Management System",
    "option2":"Data Backup Management System",
    "option3":"Digital Base Management System",
    "option4":"Data Business Management System",
    "answer":"Database Management System"
},

{
    "subject":"DBMS",
    "topic":"Introduction",
    "question_type":"MCQ",
    "question":"Which of the following is a DBMS?",
    "option1":"MySQL",
    "option2":"Python",
    "option3":"HTML",
    "option4":"CSS",
    "answer":"MySQL"
},

{
    "subject":"DBMS",
    "topic":"Keys",
    "question_type":"MCQ",
    "question":"Which key uniquely identifies each record?",
    "option1":"Primary Key",
    "option2":"Foreign Key",
    "option3":"Candidate Key",
    "option4":"Composite Key",
    "answer":"Primary Key"
},

{
    "subject":"DBMS",
    "topic":"SQL",
    "question_type":"MCQ",
    "question":"Which SQL command is used to retrieve data?",
    "option1":"SELECT",
    "option2":"INSERT",
    "option3":"UPDATE",
    "option4":"DELETE",
    "answer":"SELECT"
},

{
    "subject":"DBMS",
    "topic":"SQL",
    "question_type":"MCQ",
    "question":"Which SQL command adds a new record?",
    "option1":"INSERT",
    "option2":"SELECT",
    "option3":"DELETE",
    "option4":"DROP",
    "answer":"INSERT"
},

{
    "subject":"DBMS",
    "topic":"SQL",
    "question_type":"MCQ",
    "question":"Which command removes a table?",
    "option1":"DROP",
    "option2":"DELETE",
    "option3":"UPDATE",
    "option4":"SELECT",
    "answer":"DROP"
},

{
    "subject":"DBMS",
    "topic":"Normalization",
    "question_type":"MCQ",
    "question":"Normalization is used to?",
    "option1":"Reduce redundancy",
    "option2":"Increase duplication",
    "option3":"Delete tables",
    "option4":"Create indexes",
    "answer":"Reduce redundancy"
},

{
    "subject":"DBMS",
    "topic":"ER Model",
    "question_type":"MCQ",
    "question":"ER stands for?",
    "option1":"Entity Relationship",
    "option2":"Entity Record",
    "option3":"External Relation",
    "option4":"Entry Relation",
    "answer":"Entity Relationship"
},

{
    "subject":"DBMS",
    "topic":"Constraints",
    "question_type":"MCQ",
    "question":"Which constraint prevents duplicate values?",
    "option1":"UNIQUE",
    "option2":"CHECK",
    "option3":"DEFAULT",
    "option4":"NOT NULL",
    "answer":"UNIQUE"
},

{
    "subject":"DBMS",
    "topic":"Transactions",
    "question_type":"MCQ",
    "question":"ACID stands for?",
    "option1":"Atomicity, Consistency, Isolation, Durability",
    "option2":"Accuracy, Consistency, Isolation, Data",
    "option3":"Atomicity, Connectivity, Isolation, Durability",
    "option4":"Atomicity, Consistency, Integrity, Data",
    "answer":"Atomicity, Consistency, Isolation, Durability"
},

# ---------- DBMS Fill in the Blank ----------

{
    "subject":"DBMS",
    "topic":"Introduction",
    "question_type":"FILL",
    "question":"DBMS stands for ________ Management System.",
    "answer":"Database"
},

{
    "subject":"DBMS",
    "topic":"Keys",
    "question_type":"FILL",
    "question":"A ________ key uniquely identifies each record.",
    "answer":"Primary"
},

{
    "subject":"DBMS",
    "topic":"SQL",
    "question_type":"FILL",
    "question":"The SQL command used to retrieve data is ________.",
    "answer":"SELECT"
},

{
    "subject":"DBMS",
    "topic":"SQL",
    "question_type":"FILL",
    "question":"The SQL command used to insert data is ________.",
    "answer":"INSERT"
},

{
    "subject":"DBMS",
    "topic":"SQL",
    "question_type":"FILL",
    "question":"The SQL command used to modify records is ________.",
    "answer":"UPDATE"
},

{
    "subject":"DBMS",
    "topic":"SQL",
    "question_type":"FILL",
    "question":"The SQL command used to remove records is ________.",
    "answer":"DELETE"
},

{
    "subject":"DBMS",
    "topic":"Normalization",
    "question_type":"FILL",
    "question":"Normalization reduces data ________.",
    "answer":"Redundancy"
},

{
    "subject":"DBMS",
    "topic":"ER Model",
    "question_type":"FILL",
    "question":"ER diagram represents ________ and relationships.",
    "answer":"Entities"
},

{
    "subject":"DBMS",
    "topic":"Transactions",
    "question_type":"FILL",
    "question":"The letter D in ACID stands for ________.",
    "answer":"Durability"
},

{
    "subject":"DBMS",
    "topic":"Constraints",
    "question_type":"FILL",
    "question":"The ________ constraint prevents duplicate values.",
    "answer":"UNIQUE"
},# ---------- DBMS MCQ Questions ----------

{
    "subject":"DBMS",
    "topic":"Joins",
    "question_type":"MCQ",
    "question":"Which JOIN returns matching records from both tables?",
    "option1":"INNER JOIN",
    "option2":"LEFT JOIN",
    "option3":"RIGHT JOIN",
    "option4":"FULL JOIN",
    "answer":"INNER JOIN"
},

{
    "subject":"DBMS",
    "topic":"Joins",
    "question_type":"MCQ",
    "question":"Which JOIN returns all records from the left table?",
    "option1":"LEFT JOIN",
    "option2":"RIGHT JOIN",
    "option3":"INNER JOIN",
    "option4":"CROSS JOIN",
    "answer":"LEFT JOIN"
},

{
    "subject":"DBMS",
    "topic":"Views",
    "question_type":"MCQ",
    "question":"A View is a?",
    "option1":"Virtual Table",
    "option2":"Physical Table",
    "option3":"Database",
    "option4":"Index",
    "answer":"Virtual Table"
},

{
    "subject":"DBMS",
    "topic":"Indexes",
    "question_type":"MCQ",
    "question":"Indexes are mainly used to?",
    "option1":"Improve search speed",
    "option2":"Delete records",
    "option3":"Create tables",
    "option4":"Reduce storage",
    "answer":"Improve search speed"
},

{
    "subject":"DBMS",
    "topic":"SQL",
    "question_type":"MCQ",
    "question":"Which SQL clause is used to filter rows?",
    "option1":"WHERE",
    "option2":"ORDER BY",
    "option3":"GROUP BY",
    "option4":"HAVING",
    "answer":"WHERE"
},

{
    "subject":"DBMS",
    "topic":"SQL",
    "question_type":"MCQ",
    "question":"Which SQL clause sorts the result?",
    "option1":"ORDER BY",
    "option2":"GROUP BY",
    "option3":"WHERE",
    "option4":"SELECT",
    "answer":"ORDER BY"
},

{
    "subject":"DBMS",
    "topic":"Functions",
    "question_type":"MCQ",
    "question":"Which SQL function returns the number of rows?",
    "option1":"COUNT()",
    "option2":"SUM()",
    "option3":"AVG()",
    "option4":"MAX()",
    "answer":"COUNT()"
},

{
    "subject":"DBMS",
    "topic":"Functions",
    "question_type":"MCQ",
    "question":"Which SQL function returns the highest value?",
    "option1":"MAX()",
    "option2":"MIN()",
    "option3":"COUNT()",
    "option4":"AVG()",
    "answer":"MAX()"
},

{
    "subject":"DBMS",
    "topic":"Transactions",
    "question_type":"MCQ",
    "question":"Which command permanently saves a transaction?",
    "option1":"COMMIT",
    "option2":"ROLLBACK",
    "option3":"SAVEPOINT",
    "option4":"UNDO",
    "answer":"COMMIT"
},

{
    "subject":"DBMS",
    "topic":"Transactions",
    "question_type":"MCQ",
    "question":"Which command cancels a transaction?",
    "option1":"ROLLBACK",
    "option2":"COMMIT",
    "option3":"SAVEPOINT",
    "option4":"SELECT",
    "answer":"ROLLBACK"
},

# ---------- DBMS Fill in the Blank ----------

{
    "subject":"DBMS",
    "topic":"Joins",
    "question_type":"FILL",
    "question":"________ JOIN returns matching records from two tables.",
    "answer":"INNER"
},

{
    "subject":"DBMS",
    "topic":"Joins",
    "question_type":"FILL",
    "question":"________ JOIN returns all rows from the left table.",
    "answer":"LEFT"
},

{
    "subject":"DBMS",
    "topic":"Views",
    "question_type":"FILL",
    "question":"A view is a ________ table.",
    "answer":"Virtual"
},

{
    "subject":"DBMS",
    "topic":"Indexes",
    "question_type":"FILL",
    "question":"Indexes improve data ________ speed.",
    "answer":"Retrieval"
},

{
    "subject":"DBMS",
    "topic":"SQL",
    "question_type":"FILL",
    "question":"The ________ clause filters rows.",
    "answer":"WHERE"
},

{
    "subject":"DBMS",
    "topic":"SQL",
    "question_type":"FILL",
    "question":"The ________ BY clause sorts records.",
    "answer":"ORDER"
},

{
    "subject":"DBMS",
    "topic":"Functions",
    "question_type":"FILL",
    "question":"The SQL function ________() counts records.",
    "answer":"COUNT"
},

{
    "subject":"DBMS",
    "topic":"Functions",
    "question_type":"FILL",
    "question":"The SQL function ________() returns the highest value.",
    "answer":"MAX"
},

{
    "subject":"DBMS",
    "topic":"Transactions",
    "question_type":"FILL",
    "question":"The ________ command permanently saves a transaction.",
    "answer":"COMMIT"
},

{
    "subject":"DBMS",
    "topic":"Transactions",
    "question_type":"FILL",
    "question":"The ________ command cancels a transaction.",
    "answer":"ROLLBACK"
},# ---------- DBMS MCQ Questions ----------

{
    "subject":"DBMS",
    "topic":"Database Models",
    "question_type":"MCQ",
    "question":"Which database model stores data in tables?",
    "option1":"Relational Model",
    "option2":"Hierarchical Model",
    "option3":"Network Model",
    "option4":"Object Model",
    "answer":"Relational Model"
},

{
    "subject":"DBMS",
    "topic":"SQL",
    "question_type":"MCQ",
    "question":"Which SQL statement creates a new table?",
    "option1":"CREATE TABLE",
    "option2":"ALTER TABLE",
    "option3":"DROP TABLE",
    "option4":"TRUNCATE TABLE",
    "answer":"CREATE TABLE"
},

{
    "subject":"DBMS",
    "topic":"Constraints",
    "question_type":"MCQ",
    "question":"Which constraint does not allow NULL values?",
    "option1":"NOT NULL",
    "option2":"UNIQUE",
    "option3":"CHECK",
    "option4":"DEFAULT",
    "answer":"NOT NULL"
},

{
    "subject":"DBMS",
    "topic":"Keys",
    "question_type":"MCQ",
    "question":"A Foreign Key is used to?",
    "option1":"Link two tables",
    "option2":"Delete records",
    "option3":"Create indexes",
    "option4":"Sort data",
    "answer":"Link two tables"
},

{
    "subject":"DBMS",
    "topic":"Normalization",
    "question_type":"MCQ",
    "question":"Which normal form removes partial dependency?",
    "option1":"2NF",
    "option2":"1NF",
    "option3":"3NF",
    "option4":"BCNF",
    "answer":"2NF"
},

# ---------- DBMS Fill in the Blank ----------

{
    "subject":"DBMS",
    "topic":"Database Models",
    "question_type":"FILL",
    "question":"The ________ model stores data in tables.",
    "answer":"Relational"
},

{
    "subject":"DBMS",
    "topic":"SQL",
    "question_type":"FILL",
    "question":"The SQL command used to create a table is ________.",
    "answer":"CREATE TABLE"
},

{
    "subject":"DBMS",
    "topic":"Constraints",
    "question_type":"FILL",
    "question":"The ________ constraint prevents NULL values.",
    "answer":"NOT NULL"
},

{
    "subject":"DBMS",
    "topic":"Keys",
    "question_type":"FILL",
    "question":"A ________ key links two tables.",
    "answer":"Foreign"
},

{
    "subject":"DBMS",
    "topic":"Normalization",
    "question_type":"FILL",
    "question":"Second Normal Form is abbreviated as ________.",
    "answer":"2NF"
},
]  
    for q in questions:
        Question.objects.get_or_create(question=q["question"],defaults=q)      
def load_java_questions():
    questions = [
        {
            "subject": "Java",
            "topic": "Basics",
            "question_type": "MCQ",
            "question": "Who developed Java?",
            "option1": "Microsoft",
            "option2": "Sun Microsystems",
            "option3": "Google",
            "option4": "IBM",
            "answer": "Sun Microsystems",
        },
        # ---------- JAVA MCQ QUESTIONS ----------

{
    "subject":"Java",
    "topic":"Basics",
    "question_type":"MCQ",
    "question":"Who developed Java?",
    "option1":"James Gosling",
    "option2":"Dennis Ritchie",
    "option3":"Guido van Rossum",
    "option4":"Bjarne Stroustrup",
    "answer":"James Gosling"
},

{
    "subject":"Java",
    "topic":"Basics",
    "question_type":"MCQ",
    "question":"Which company originally developed Java?",
    "option1":"Sun Microsystems",
    "option2":"Microsoft",
    "option3":"Google",
    "option4":"IBM",
    "answer":"Sun Microsystems"
},

{
    "subject":"Java",
    "topic":"Basics",
    "question_type":"MCQ",
    "question":"Which extension is used for a Java source file?",
    "option1":".java",
    "option2":".class",
    "option3":".js",
    "option4":".jav",
    "answer":".java"
},

{
    "subject":"Java",
    "topic":"Basics",
    "question_type":"MCQ",
    "question":"Which method is the starting point of a Java program?",
    "option1":"main()",
    "option2":"start()",
    "option3":"run()",
    "option4":"execute()",
    "answer":"main()"
},

{
    "subject":"Java",
    "topic":"Basics",
    "question_type":"MCQ",
    "question":"Which keyword is used to create an object?",
    "option1":"new",
    "option2":"class",
    "option3":"object",
    "option4":"create",
    "answer":"new"
},

{
    "subject":"Java",
    "topic":"OOP",
    "question_type":"MCQ",
    "question":"Which concept hides internal implementation details?",
    "option1":"Abstraction",
    "option2":"Inheritance",
    "option3":"Polymorphism",
    "option4":"Compilation",
    "answer":"Abstraction"
},

{
    "subject":"Java",
    "topic":"OOP",
    "question_type":"MCQ",
    "question":"Which concept allows a class to acquire properties of another class?",
    "option1":"Inheritance",
    "option2":"Encapsulation",
    "option3":"Abstraction",
    "option4":"Compilation",
    "answer":"Inheritance"
},

{
    "subject":"Java",
    "topic":"OOP",
    "question_type":"MCQ",
    "question":"Which keyword is used to inherit a class?",
    "option1":"extends",
    "option2":"implements",
    "option3":"inherits",
    "option4":"super",
    "answer":"extends"
},

{
    "subject":"Java",
    "topic":"OOP",
    "question_type":"MCQ",
    "question":"Which keyword is used to implement an interface?",
    "option1":"implements",
    "option2":"extends",
    "option3":"interface",
    "option4":"inherit",
    "answer":"implements"
},

{
    "subject":"Java",
    "topic":"Data Types",
    "question_type":"MCQ",
    "question":"Which data type is used to store whole numbers?",
    "option1":"int",
    "option2":"float",
    "option3":"char",
    "option4":"boolean",
    "answer":"int"
},

{
    "subject":"Java",
    "topic":"Basics",
    "question_type":"FILL",
    "question":"Java was developed by ________ Gosling.",
    "answer":"James"
},

{
    "subject":"Java",
    "topic":"Basics",
    "question_type":"FILL",
    "question":"The file extension of a Java source file is ________.",
    "answer":".java"
},

{
    "subject":"Java",
    "topic":"Basics",
    "question_type":"FILL",
    "question":"The ________ method is the starting point of a Java program.",
    "answer":"main()"
},

{
    "subject":"Java",
    "topic":"Basics",
    "question_type":"FILL",
    "question":"The ________ keyword is used to create an object.",
    "answer":"new"
},

{
    "subject":"Java",
    "topic":"OOP",
    "question_type":"FILL",
    "question":"The process of acquiring properties from another class is called ________.",
    "answer":"Inheritance"
},

{
    "subject":"Java",
    "topic":"OOP",
    "question_type":"FILL",
    "question":"The ________ keyword is used to inherit a class.",
    "answer":"extends"
},

{
    "subject":"Java",
    "topic":"OOP",
    "question_type":"FILL",
    "question":"The ________ keyword is used to implement an interface.",
    "answer":"implements"
},

{
    "subject":"Java",
    "topic":"OOP",
    "question_type":"FILL",
    "question":"The process of hiding implementation details is called ________.",
    "answer":"Abstraction"
},

{
    "subject":"Java",
    "topic":"Data Types",
    "question_type":"FILL",
    "question":"The ________ data type is used to store whole numbers.",
    "answer":"int"
},

{
    "subject":"Java",
    "topic":"Data Types",
    "question_type":"FILL",
    "question":"The ________ data type is used to store true or false values.",
    "answer":"boolean"
},
        # Add 14 more questions
    ]

    for q in questions:
        Question.objects.get_or_create(
            question=q["question"],
            defaults=q
        )                
def load_python_questions():
    questions=[
        {
    "subject": "Python",
    "topic": "Functions",
    "question_type": "MCQ",
    "question": "Which keyword is used to define a function in Python?",
    "option1": "def",
    "option2": "function",
    "option3": "create",
    "option4": "fun",
    "answer": "def"
},
{
    "subject": "Python",
    "topic": "Basics",
    "question_type": "MCQ",
    "question": "Which symbol is used for comments in Python?",
    "option1": "#",
    "option2": "//",
    "option3": "/* */",
    "option4": "--",
    "answer": "#"
},
{
    "subject": "Python",
    "topic": "Variables",
    "question_type": "FILL",
    "question": "Python is a ______ typed programming language.",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "dynamically"
},
{
    "subject": "Python",
    "topic": "Data Types",
    "question_type": "MCQ",
    "question": "Which data type stores True or False values?",
    "option1": "int",
    "option2": "bool",
    "option3": "float",
    "option4": "str",
    "answer": "bool"
},
{
    "subject": "Python",
    "topic": "Lists",
    "question_type": "MCQ",
    "question": "Which brackets are used to create a list?",
    "option1": "()",
    "option2": "[]",
    "option3": "{}",
    "option4": "<>",
    "answer": "[]"
},
{
    "subject": "Python",
    "topic": "Tuples",
    "question_type": "MCQ",
    "question": "Tuples in Python are ______.",
    "option1": "Mutable",
    "option2": "Immutable",
    "option3": "Dynamic",
    "option4": "Empty",
    "answer": "Immutable"
},
{
    "subject": "Python",
    "topic": "Dictionary",
    "question_type": "MCQ",
    "question": "A dictionary stores data as ______ pairs.",
    "option1": "Key-Value",
    "option2": "Index",
    "option3": "Row",
    "option4": "Column",
    "answer": "Key-Value"
},
{
    "subject": "Python",
    "topic": "Loops",
    "question_type": "TEXT",
    "question": "Which loop is mainly used to iterate over a sequence?",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "for"
},
{
    "subject": "Python",
    "topic": "Loops",
    "question_type": "MCQ",
    "question": "Which keyword is used to exit a loop?",
    "option1": "stop",
    "option2": "break",
    "option3": "exit",
    "option4": "continue",
    "answer": "break"
},
{
    "subject": "Python",
    "topic": "Loops",
    "question_type": "MCQ",
    "question": "Which keyword skips the current iteration of a loop?",
    "option1": "skip",
    "option2": "continue",
    "option3": "break",
    "option4": "next",
    "answer": "continue"
},
{
    "subject": "Python",
    "topic": "Operators",
    "question_type": "MCQ",
    "question": "Which operator is used for exponentiation in Python?",
    "option1": "^",
    "option2": "**",
    "option3": "//",
    "option4": "%",
    "answer": "**"
},
{
    "subject": "Python",
    "topic": "Operators",
    "question_type": "MCQ",
    "question": "Which operator returns the remainder after division?",
    "option1": "/",
    "option2": "//",
    "option3": "%",
    "option4": "*",
    "answer": "%"
},
{
    "subject": "Python",
    "topic": "Functions",
    "question_type": "FILL",
    "question": "The ______ keyword is used to return a value from a function.",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "return"
},
{
    "subject": "Python",
    "topic": "Strings",
    "question_type": "MCQ",
    "question": "Which method converts a string to uppercase?",
    "option1": "upper()",
    "option2": "uppercase()",
    "option3": "capital()",
    "option4": "up()",
    "answer": "upper()"
},
{
    "subject": "Python",
    "topic": "Strings",
    "question_type": "TEXT",
    "question": "Which function returns the length of a string?",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "len()"
},
{
    "subject": "Python",
    "topic": "Lists",
    "question_type": "MCQ",
    "question": "Which method adds an element to the end of a list?",
    "option1": "insert()",
    "option2": "append()",
    "option3": "extend()",
    "option4": "add()",
    "answer": "append()"
},
{
    "subject": "Python",
    "topic": "Lists",
    "question_type": "MCQ",
    "question": "Which method removes the last element from a list?",
    "option1": "remove()",
    "option2": "delete()",
    "option3": "pop()",
    "option4": "clear()",
    "answer": "pop()"
},
{
    "subject": "Python",
    "topic": "OOP",
    "question_type": "MCQ",
    "question": "Which keyword is used to define a class?",
    "option1": "object",
    "option2": "class",
    "option3": "new",
    "option4": "define",
    "answer": "class"
},
{
    "subject": "Python",
    "topic": "OOP",
    "question_type": "FILL",
    "question": "The constructor method in Python is called ______.",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "__init__"
},
{
    "subject": "Python",
    "topic": "Files",
    "question_type": "MCQ",
    "question": "Which function is used to open a file in Python?",
    "option1": "open()",
    "option2": "file()",
    "option3": "read()",
    "option4": "write()",
    "answer": "open()"
},
{
    "subject": "Python",
    "topic": "Dictionary",
    "question_type": "MCQ",
    "question": "Which data type stores key-value pairs?",
    "option1": "List",
    "option2": "Tuple",
    "option3": "Dictionary",
    "option4": "Set",
    "answer": "Dictionary"
},
{
    "subject": "Python",
    "topic": "Dictionary",
    "question_type": "TEXT",
    "question": "Which method returns all keys of a dictionary?",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "keys()"
},
{
    "subject": "Python",
    "topic": "Tuple",
    "question_type": "MCQ",
    "question": "Which collection is immutable?",
    "option1": "List",
    "option2": "Dictionary",
    "option3": "Tuple",
    "option4": "Set",
    "answer": "Tuple"
},
{
    "subject": "Python",
    "topic": "Set",
    "question_type": "MCQ",
    "question": "Which collection stores only unique values?",
    "option1": "Tuple",
    "option2": "List",
    "option3": "Dictionary",
    "option4": "Set",
    "answer": "Set"
},
{
    "subject": "Python",
    "topic": "Exception Handling",
    "question_type": "MCQ",
    "question": "Which keyword is used to handle exceptions?",
    "option1": "catch",
    "option2": "except",
    "option3": "error",
    "option4": "finally",
    "answer": "except"
},
{
    "subject": "Python",
    "topic": "Exception Handling",
    "question_type": "FILL",
    "question": "The ______ block is always executed whether an exception occurs or not.",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "finally"
},
{
    "subject": "Python",
    "topic": "Modules",
    "question_type": "MCQ",
    "question": "Which keyword is used to include a module?",
    "option1": "include",
    "option2": "using",
    "option3": "import",
    "option4": "package",
    "answer": "import"
},
{
    "subject": "Python",
    "topic": "Built-in Functions",
    "question_type": "MCQ",
    "question": "Which function converts a string into an integer?",
    "option1": "str()",
    "option2": "int()",
    "option3": "float()",
    "option4": "bool()",
    "answer": "int()"
},
{
    "subject": "Python",
    "topic": "Built-in Functions",
    "question_type": "TEXT",
    "question": "Which function displays output on the screen?",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "print()"
},
{
    "subject": "Python",
    "topic": "Basics",
    "question_type": "MCQ",
    "question": "Python is a ______ programming language.",
    "option1": "Compiled only",
    "option2": "Interpreted",
    "option3": "Machine",
    "option4": "Assembly",
    "answer": "Interpreted"
},
{
    "subject": "Python",
    "topic": "Operators",
    "question_type": "MCQ",
    "question": "Which operator is used for exponentiation in Python?",
    "option1": "^",
    "option2": "**",
    "option3": "//",
    "option4": "%",
    "answer": "**"
},
{
    "subject": "Python",
    "topic": "Operators",
    "question_type": "FILL",
    "question": "The ______ operator is used for floor division.",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "//"
},
{
    "subject": "Python",
    "topic": "Strings",
    "question_type": "MCQ",
    "question": "Which function returns the length of a string?",
    "option1": "size()",
    "option2": "count()",
    "option3": "len()",
    "option4": "length()",
    "answer": "len()"
},
{
    "subject": "Python",
    "topic": "Strings",
    "question_type": "TEXT",
    "question": "Which method converts a string to uppercase?",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "upper()"
},
{
    "subject": "Python",
    "topic": "Lists",
    "question_type": "MCQ",
    "question": "Which method removes the last element from a list?",
    "option1": "remove()",
    "option2": "delete()",
    "option3": "pop()",
    "option4": "clear()",
    "answer": "pop()"
},
{
    "subject": "Python",
    "topic": "Lists",
    "question_type": "FILL",
    "question": "The ______ method adds an item at the end of a list.",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "append"
},
{
    "subject": "Python",
    "topic": "Functions",
    "question_type": "MCQ",
    "question": "Which keyword returns a value from a function?",
    "option1": "break",
    "option2": "yield",
    "option3": "return",
    "option4": "pass",
    "answer": "return"
},
{
    "subject": "Python",
    "topic": "Loops",
    "question_type": "MCQ",
    "question": "Which loop executes as long as a condition is True?",
    "option1": "for",
    "option2": "repeat",
    "option3": "while",
    "option4": "loop",
    "answer": "while"
},
{
    "subject": "Python",
    "topic": "Boolean",
    "question_type": "TEXT",
    "question": "What are the two Boolean values in Python?",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "True, False"
},
{
    "subject": "Python",
    "topic": "Basics",
    "question_type": "MCQ",
    "question": "Which of the following is a valid Python file extension?",
    "option1": ".java",
    "option2": ".cpp",
    "option3": ".py",
    "option4": ".html",
    "answer": ".py"
},
{
    "subject": "Python",
    "topic": "Input Output",
    "question_type": "MCQ",
    "question": "Which function is used to take input from the user?",
    "option1": "read()",
    "option2": "scan()",
    "option3": "input()",
    "option4": "get()",
    "answer": "input()"
},
{
    "subject": "Python",
    "topic": "Data Types",
    "question_type": "FILL",
    "question": "The ______ data type stores decimal numbers.",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "float"
},
{
    "subject": "Python",
    "topic": "Conditional Statements",
    "question_type": "MCQ",
    "question": "Which keyword is used for an alternative condition?",
    "option1": "else if",
    "option2": "elseif",
    "option3": "elif",
    "option4": "otherwise",
    "answer": "elif"
},
{
    "subject": "Python",
    "topic": "Lists",
    "question_type": "MCQ",
    "question": "Which method removes all elements from a list?",
    "option1": "delete()",
    "option2": "remove()",
    "option3": "pop()",
    "option4": "clear()",
    "answer": "clear()"
},
{
    "subject": "Python",
    "topic": "Strings",
    "question_type": "TEXT",
    "question": "Which method converts a string to lowercase?",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "lower()"
},
{
    "subject": "Python",
    "topic": "Functions",
    "question_type": "MCQ",
    "question": "Which keyword is used to define an anonymous function?",
    "option1": "func",
    "option2": "lambda",
    "option3": "anonymous",
    "option4": "def",
    "answer": "lambda"
},
{
    "subject": "Python",
    "topic": "File Handling",
    "question_type": "MCQ",
    "question": "Which function is used to open a file?",
    "option1": "open()",
    "option2": "file()",
    "option3": "read()",
    "option4": "load()",
    "answer": "open()"
},
{
    "subject": "Python",
    "topic": "File Handling",
    "question_type": "FILL",
    "question": "The ______ mode is used to append data to a file.",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "a"
},
{
    "subject": "Python",
    "topic": "Object Oriented Programming",
    "question_type": "MCQ",
    "question": "Which keyword is used to create a class in Python?",
    "option1": "object",
    "option2": "class",
    "option3": "struct",
    "option4": "define",
    "answer": "class"
},
{
    "subject": "Python",
    "topic": "Basics",
    "question_type": "TEXT",
    "question": "Who created Python?",
    "option1": "",
    "option2": "",
    "option3": "",
    "option4": "",
    "answer": "Guido van Rossum"
}
]
    for q in questions:
        Question.objects.get_or_create(question=q["question"],defaults=q)
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

    special_characters = re.findall(r"[^a-zA-Z0-9]", password)

    if len(special_characters) != 1:
        return "Password must contain exactly one special character."

    return None        
def register(request):
    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        phone = request.POST.get("phone", "").strip()
        year = request.POST.get("btech_year", "")

        # Password confirmation
        if password != confirm_password:
            return render(request, "accounts/register.html", {
                "error": "Passwords do not match"
            })

        # Check email already exists
        if Student.objects.filter(email=email).exists():
            return render(request, "accounts/register.html", {
                "error": "Email already exists"
            })

        # Create student
        student = Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=password,
            year=year
        )

        # Store login information in session
        request.session["student_id"] = student.id
        request.session["student_name"] = student.name
        request.session["student_email"] = student.email

        return redirect("/dashboard/")

    return render(request, "accounts/register.html")
import random
import re

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password

from .models import Student


# --------------------------------------------------
# LOGIN PAGE
# --------------------------------------------------

def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        # -------------------------------
        # EMAIL VALIDATION
        # -------------------------------

        email_pattern = r"^[a-z0-9#]+@intell\.com$"

        if not re.fullmatch(email_pattern, email):
            return render(
                request,
                "accounts/login.html",
                {
                    "error":
                    "Invalid email. Use lowercase letters, numbers or # and @intell.com"
                }
            )

        # -------------------------------
        # PASSWORD VALIDATION
        # -------------------------------

        password_error = validate_password(password)

        if password_error:
            return render(
                request,
                "accounts/login.html",
                {
                    "error": password_error,
                    "email": email
                }
            )

        # -------------------------------
        # FIND STUDENT
        # -------------------------------

        try:
            student = Student.objects.get(email=email)

        except Student.DoesNotExist:

            return render(
                request,
                "accounts/login.html",
                {
                    "error": "Email or password is incorrect."
                }
            )

        # -------------------------------
        # CHECK PASSWORD
        # -------------------------------

        if password != student.password:
            return render(
                request,
                "accounts/login.html",
                {
                    "error": "Email or password is incorrect."
                }
            )

        # -------------------------------
        # LOGIN SUCCESS
        # -------------------------------

        request.session["student_id"] = student.id
        request.session["student_name"] = student.name
        request.session["student_email"] = student.email

        return redirect("/dashboard/")

    return render(request, "accounts/login.html")


# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------

def validate_password(password):

    # Exactly 7 characters
    if len(password) != 7:
        return "Password must contain exactly 7 characters."

    # At least one uppercase
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    # Numbers
    numbers = re.findall(r"[0-9]", password)

    if len(numbers) < 1:
        return "Password must contain at least one number."

    if len(numbers) > 2:
        return "Password can contain maximum two numbers."

    # Special characters
    special_characters = re.findall(
        r"[^a-zA-Z0-9]",
        password
    )

    if len(special_characters) != 1:
        return "Password must contain exactly one special character."

    return None


# --------------------------------------------------
# FORGOT PASSWORD PAGE
# --------------------------------------------------

def forgot_password(request):

    if request.method == "POST":

        phone = request.POST.get("phone", "").strip()

        try:
            student = Student.objects.get(phone=phone)

        except Student.DoesNotExist:

            return render(
                request,
                "accounts/forgot_password.html",
                {
                    "error":
                    "This phone number is not registered."
                }
            )

        # Generate 6 digit OTP
        otp = str(random.randint(100000, 999999))

        # Store OTP in session
        request.session["reset_student_id"] = student.id
        request.session["reset_otp"] = otp

        # ------------------------------------------------
        # DEVELOPMENT ONLY
        # ------------------------------------------------
        # This prints OTP in terminal.
        # Later we will connect SMS service.
        print("--------------------------------")
        print("OTP:", otp)
        print("--------------------------------")

        return redirect("/verify-otp/")

    return render(
        request,
        "accounts/forgot_password.html"
    )


# --------------------------------------------------
# OTP VERIFICATION
# --------------------------------------------------

def verify_otp(request):

    if "reset_student_id" not in request.session:
        return redirect("/login/")

    if request.method == "POST":

        entered_otp = request.POST.get("otp", "").strip()

        stored_otp = request.session.get("reset_otp")

        if entered_otp == stored_otp:

            student_id = request.session.get(
                "reset_student_id"
            )

            request.session["verified_student_id"] = student_id

            # Remove OTP
            request.session.pop("reset_otp", None)

            return redirect("/otp-success/")

        else:

            return render(
                request,
                "accounts/verify_otp.html",
                {
                    "error": "Invalid OTP. Please try again."
                }
            )

    return render(
        request,
        "accounts/verify_otp.html"
    )


# --------------------------------------------------
# OTP SUCCESS
# --------------------------------------------------

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

    # Open student's account
    request.session["student_id"] = student.id
    request.session["student_name"] = student.name
    request.session["student_email"] = student.email

    request.session.pop(
        "verified_student_id",
        None
    )

    return redirect("/dashboard/")
from collections import Counter

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

    if subject.lower() == "python":
        questions = load_python_questions() or []
    elif subject.lower() == "machine learning":
        questions = load_ml_questions() or []
    elif subject.lower() == "dbms":
        questions = load_dbms_questions() or []
    else:
        questions = []

    return render(
        request,
        "accounts/quiz_instructions.html",
        {
            "subject": subject,
            "number_of_questions":15,
            "time_limit": 5,
        }
    )
def process_quiz(request, subject, template_name, loader_function):
    loader_function()

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/login/")

    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        request.session.flush()
        return redirect("/login/")

    if request.method == "GET":

        questions = list(
            Question.objects.filter(
                subject=subject
            ).order_by("?")[:15]
        )

        request.session["last_quiz_question_ids"] = [
            q.id for q in questions
        ]

    else:

        question_ids = request.session.get(
            "last_quiz_question_ids", []
        )

        questions = list(
            Question.objects.filter(
                id__in=question_ids,
                subject=subject
            )
        )

    if request.method == "POST":

        score = 0

        for q in questions:

            user_answer = request.POST.get(
                str(q.id),
                ""
            ).strip()

            correct_answer = q.answer.strip()

            if user_answer.lower() == correct_answer.lower():
                score += 1
            else:
                WrongAnswer.objects.create(
                    student=student,
                    question=q,
                    user_answer=user_answer,
                    correct_answer=correct_answer,
                    topic=q.topic
                )

        QuizResult.objects.create(
            student=student,
            subject=subject,
            score=score,
            total_questions=len(questions),
            correct_answers=score,
            wrong_answers=len(questions) - score
        )

        return redirect("/dashboard/")

    return render(
        request,
        template_name,
        {
            "questions": questions
        }
    )

def python_quiz(request):
    return process_quiz(
        request,
        "Python",
        "accounts/python_quiz.html",
        load_python_questions
    )


def ml_quiz(request):
    return process_quiz(
        request,
        "Machine Learning",
        "accounts/ml_quiz.html",
        load_ml_questions
    )


def dbms_quiz(request):
    return process_quiz(
        request,
        "DBMS",
        "accounts/dbms_quiz.html",
        load_dbms_questions
    )


def java_quiz(request):
    return process_quiz(
        request,
        "Java",
        "accounts/java_quiz.html",
        load_java_questions
    )
from datetime import timedelta
from django.utils import timezone
def progress(request):
    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/login/")

    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        request.session.flush()
        return redirect("/login/")

    now = timezone.now()

    week_start = now - timedelta(days=7)
    month_start = now - timedelta(days=30)

    weekly_results = QuizResult.objects.filter(
        student=student,
        created_at__gte=week_start
    )

    monthly_results = QuizResult.objects.filter(
        student=student,
        created_at__gte=month_start
    )

    weekly_quizzes = weekly_results.count()
    monthly_quizzes = monthly_results.count()

    weekly_score = 0
    monthly_score = 0

    weekly_questions = sum(
        result.total_questions
        for result in weekly_results
    )

    weekly_correct = sum(
        result.correct_answers
        for result in weekly_results
    )

    monthly_questions = sum(
        result.total_questions
        for result in monthly_results
    )

    monthly_correct = sum(
        result.correct_answers
        for result in monthly_results
    )

    if weekly_questions > 0:
        weekly_score = round(
            (weekly_correct / weekly_questions) * 100
        )

    if monthly_questions > 0:
        monthly_score = round(
            (monthly_correct / monthly_questions) * 100
        )

    return render(
        request,
        "accounts/progress.html",
        {
            "student": student,
            "weekly_quizzes": weekly_quizzes,
            "weekly_score": weekly_score,
            "monthly_quizzes": monthly_quizzes,
            "monthly_score": monthly_score,
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