from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('post/<int:pk>', views.post_view, name='post'),
    path('category/<int:pk>', views.category_view, name='category'),
    path('author/', views.author_view, name='author'),
    path('date/', views.date_view, name='date'),
]
