from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post


def home(request):
    posts_list = Post.objects.filter(published=True)

    paginator = Paginator(posts_list, per_page=3)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    context = {
        'posts': posts,
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
