from django.urls import path, include
from sample_app import views


urlpatterns = [
    path('user-profiles', views.UserProfileView.as_view()),
    path('user-profiles/<int:pk>', views.UserProfileView.as_view())
    # path('', include(router.urls))
]
