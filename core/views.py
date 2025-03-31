from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html', {})


def post(request):
    return render(request, 'core/post.html', {})


def author(request):
    return render(request, 'core/home.html', {})


def category(request):
    return render(request, 'core/home.html', {})


def date(request):
    return render(request, 'core/home.html', {})
