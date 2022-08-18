from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post, User
from .utils import get_paginator


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    context.update(get_paginator(posts, request))
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    context = {
        'group': group,
    }
    context.update(get_paginator(posts, request))
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author)
    count_posts = posts.count()
    context = {
        'count_posts': count_posts,
        'author': author,
    }
    context.update(get_paginator(posts, request))
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    count_post = Post.objects.filter(author_id=post.author.id).count()
    context = {
        'count_post': count_post,
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    context = {
        'form': form,
        'is_edit': False
    }

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', post.author)

    return render(request, 'posts/post_create.html', context)


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=post)
    context = {
        'form': form,
        'is_edit': True,
    }

    if request.user != post.author:
        return redirect('posts:post_detail', post.id)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post.id)
    return render(request, 'posts/post_create.html', context)
