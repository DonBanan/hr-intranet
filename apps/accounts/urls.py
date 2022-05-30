from django.urls import path

from . import views


urlpatterns = [
    path('accounts/login/', views.LoginPageView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.EditUserProfileView.as_view(), name='profile'),
    path('profile/ses/', views.EditUserSESView.as_view(), name='profile-ses'),
]
