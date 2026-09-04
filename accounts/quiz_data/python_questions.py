from accounts.models import Question


def load_python_questions():
    questions = [
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
        Question.objects.get_or_create(
            question=q["question"],
            defaults=q
        )
