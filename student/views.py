from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dashboard(request):
    return render(request, "student/dashboard.html")


# def profile(request):
#     return render(request)


# def groups(request):
#     return render(request)


# def subject(request):
#     return render(request)

# def calendar(request):
#     return render(request)

# def grades(request):
#     return render(request)


# def settings(request):
#     return render(request)


# Prof views
'''
def dashboard(request):
    return render(request, "teacher_backend/profmain.html")


def profile(request):
    return render(request)


def groups(request):
    return render(request)


def subject(request):
    return render(request)


def calendar(request):
    return render(request)


def grades(request):
    return render(request)


def settings(request):
    return render(request)

'''
