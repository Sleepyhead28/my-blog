from django.shortcuts import render
from .models import Category, Topic, Entry

# Create your views here.

def index(request):
    """博客的主页"""
    return render(request, 'my_blogs/index.html')

def categories(request):
    """显示所有大类"""
    categories = Category.objects.order_by('date_added')
    context = {'categories': categories}
    return render(request, 'my_blogs/categories.html', context)

def topics(request):
    """显示单个大类下文章的主题"""
    topics = Category.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'my_blogs/topics.html', context)


