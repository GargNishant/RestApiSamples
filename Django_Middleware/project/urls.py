from django.urls import path, include
from user_manage import views

urlpatterns = [
    path('dummy', views.dummy_api,)
]