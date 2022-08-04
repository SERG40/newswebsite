from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from news.forms import CreateNews
from .models import News



def index(request):
    news = News.objects.all()
    paginator = Paginator(news, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context)

@login_required
def create_news(request):
    form = CreateNews(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'create_news.html', context={'form': form})
