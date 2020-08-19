from django.urls import path
from sample_app import views


urlpatterns = [
    path('user-profiles', views.UserProfileView.as_view()),
    path('user-profiles/<int:mobile>', views.UserProfileView.as_view()),
    path('user-profiles/<str:username>', views.UserProfileView.as_view()),
    path('user-profiles/<int:pk>', views.UserProfileView.as_view()),
    path('sessions', views.SessionView.as_view())
]
