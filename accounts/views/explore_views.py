from django.shortcuts import render


def explore(request):

    explore_items = [
        {
            "icon": "📚",
            "title": "Explore Subjects",
            "description": "Browse your available subjects and start a quiz.",
            "url": "subjects",
            "button": "Explore Subjects",
        },
        {
            "icon": "🎯",
            "title": "Knowledge Gap",
            "description": "Identify your weak topics and find areas that need improvement.",
            "url": "knowledge_gap",
            "button": "Analyze Knowledge Gap",
        },
        {
            "icon": "📖",
            "title": "Study Recommendation",
            "description": "Get personalized study suggestions based on your performance.",
            "url": "recommendation",
            "button": "View Recommendations",
        },
        {
            "icon": "📊",
            "title": "My Progress",
            "description": "Track your quiz scores, performance and learning progress.",
            "url": "progress_analysis",
            "button": "View Progress",
        },
        {
            "icon": "📝",
            "title": "Quiz History",
            "description": "Review your previous quizzes, scores and answers.",
            "url": "quiz_history",
            "button": "View History",
        },
        {
            "icon": "🤖",
            "title": "AI Chat Assistant",
            "description": "Ask questions and get instant help with your learning.",
            "url": "chat",
            "button": "Ask AI",
        },
    ]

    return render(
        request,
        "accounts/explore.html",
        {
            "explore_items": explore_items
        }
    )