from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from blogs.forms import PostForm
from blogs.models import BlogPost


def blogs_page(request):
    """Домашняя страница приложения Learning Log"""
    return render(request, 'blogs/blogs_page.html')

def posts(request):
    """Выводит список тем."""
    post = BlogPost.objects.order_by('date_added')
    context = {'posts': post, 'current_user': request.user}
    return render(request, 'blogs/blogs_page.html', context)

@login_required
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:posts')
    context = {'posts': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

@login_required
def add_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:posts')
    context = {'form': form}
    return render(request, 'blogs/add_post.html', context)


