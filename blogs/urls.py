from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Домашняя страница
    path('', views.posts, name='posts'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('add_post/', views.add_post, name='add_post')
]