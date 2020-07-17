from django.urls import path
from calc import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="Add"),
    path('add-post', views.addPost, name='Add Post'),
]
