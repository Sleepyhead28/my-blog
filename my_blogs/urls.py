from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('categories/(?P\d+)/', views.topics, name='topics'),
]
app_name = 'my_blogs'