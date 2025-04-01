from django.shortcuts import render

from .models import Post


def home(request):
    context = {
        'posts': Post.objects.filter(published=True)
    }
    return render(request, 'core/home.html', context)


def post(request):
    return render(request, 'core/post.html', {})


def author(request):
    return render(request, 'core/home.html', {})


def category(request):
    return render(request, 'core/home.html', {})


def date(request):
    return render(request, 'core/home.html', {})
