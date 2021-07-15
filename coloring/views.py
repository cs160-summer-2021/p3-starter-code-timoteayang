from django.shortcuts import render

def demo(request):
    return render(request, 'coloring/demo.html')

def index(request):
    return render(request, 'coloring/index.html')

def home(request):
    return render(request, 'coloring/home.html')

def artboard(request):
    return render(request, 'coloring/artboard.html')

def login(request):
    return render(request, 'coloring/index.html')

def signup(request):
    return render(request, 'coloring/signup.html')

def profile(request):
    return render(request, 'coloring/profile.html')

def clashes(request):
    return render(request, 'coloring/clashes.html')

def leaderboard(request):
    return render(request, 'coloring/leaderboard.html') 