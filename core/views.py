from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.models import User

from .models import Post, Category


def home_view(request):
    posts_list = Post.objects.filter(published=True)

    paginator = Paginator(posts_list, per_page=1)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    context = {
        'posts': posts,
        'title': 'Home',  # TODO: Remove title property if dates has its own template
    }
    return render(request, 'core/home.html', context)


def post_view(request, pk):
    try:
        post = get_object_or_404(Post, id=pk)
    except:  # Http404
        return render(request, 'core/404.html')

    context = {
        'post': post,
    }
    return render(request, 'core/post.html', context)


def author_view(request, pk):
    author = User.objects.get(id=pk)
    author_posts = Post.objects.filter(author=author)
    paginator = Paginator(author_posts, per_page=1)
    page = request.GET.get('page', 1)

    context = {
        'author': author,
        'posts': paginator.get_page(page),
    }

    return render(request, 'core/posts_by_author.html', context)


def category_view(request, pk):
    category = Category.objects.get(id=pk)
    category_posts = Post.objects.filter(category=category)
    paginator = Paginator(category_posts, per_page=1)
    page = request.GET.get('page', 1)

    context = {
        'category': category,
        'posts': paginator.get_page(page),
    }

    return render(request, 'core/posts_by_category.html', context)


def date_view(request):
    context = {
        'title': 'Date',
    }

    return render(request, 'core/posts_by_date.html', context)
