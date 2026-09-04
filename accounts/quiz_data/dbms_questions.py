from accounts.models import Question


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
        },

        # ---------- DBMS MCQ Questions ----------

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
        },

        # ---------- DBMS MCQ Questions ----------

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
        Question.objects.get_or_create(
            question=q["question"],
            defaults=q
        )
