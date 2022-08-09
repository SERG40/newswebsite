from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from news.forms import CreateNewsForm, CommentForm
from .models import News, Comment


def index(request):
    """Главная страница."""
    news = News.objects.all()
    comment = Comment.objects.all().count()
    paginator = Paginator(news, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    liked = False
    if news.filter(id=request.user.id).exists():
        liked = True
    context = {
        'page_obj': page_obj,
        'comment': comment,
        'liked': liked,
    }
    return render(request, 'index.html', context)


@login_required
def create_news(request):
    """Создание новости."""
    form = CreateNewsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'create_news.html', context={'form': form})


def post_detail(request, post_id):
    """Новость подробно."""
    post = get_object_or_404(News, pk=post_id)
    news = News.objects.all()
    form = CommentForm()
    comment = Paginator(Comment.objects.filter(post=post_id), 10)
    page_number = request.GET.get('page')
    page_obj = comment.get_page(page_number)
    context = {
        'news': news,
        'post': post,
        'form': form,
        'comments': comment,
        'page_obj': page_obj,
    }
    return render(request, 'post_detail.html', context)


@login_required
def edit(request, id):
    """Редектирование новости."""
    post = get_object_or_404(News, id=id)
    if post.author == request.user:
        form = CreateNewsForm(
            request.POST or None,
            instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id)

        return render(request, 'edit.html',
                      context={'form': form,
                               'is_edit': True,
                               'post': post})
    return redirect('post_detail', id)


@login_required
def delete(request, id):
    """Удаление новости."""
    obj = News.objects.get(id=id)
    if obj.author == request.user:
        obj.delete()
        return redirect("/")
    return redirect('/')


def DeleteComment(request, id):
    """Удаление коментария."""
    obj = Comment.objects.get(id=id)
    if obj.author == request.user:
        obj.delete()
        return redirect('/')
    return redirect('/')


@login_required
def add_comment(request, id):
    """Добавить коментарий."""
    post = get_object_or_404(News, id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('post_detail', id)


def like(request, pk):
    """Лайки."""
    post = get_object_or_404(News, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('/')
