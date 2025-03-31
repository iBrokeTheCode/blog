from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('author/', views.author, name='author'),
    path('category/', views.category, name='category'),
    path('date/', views.date, name='date'),
]
