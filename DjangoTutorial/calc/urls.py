from django.urls import path
from calc import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="Add"),
    path('add-post', views.add_post, name='Add Post'),
    path('add-form', views.addPostForm, name="Add Form")
]
