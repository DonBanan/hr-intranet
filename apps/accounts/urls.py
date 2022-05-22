from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('accounts/login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html', next_page=None),
         name='logout'),
]