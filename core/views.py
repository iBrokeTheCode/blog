from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post


def home(request):
    posts_list = Post.objects.filter(published=True)

    paginator = Paginator(posts_list, per_page=3)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    context = {
        'posts': posts,
        'title': 'Home',
    }
    return render(request, 'core/home.html', context)


def post(request, pk):
    post = get_object_or_404(Post, id=pk)

    context = {
        'post': post,
    }
    return render(request, 'core/post.html', context)


def author(request):
    context = {
        'title': 'Author',
    }

    return render(request, 'core/home.html', context)


def category(request):
    context = {
        'title': 'Category',
    }

    return render(request, 'core/home.html', context)


def date(request):
    context = {
        'title': 'Date',
    }

    return render(request, 'core/home.html', context)
