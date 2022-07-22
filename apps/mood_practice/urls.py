from django.urls import path

from . import views


urlpatterns = [
    path('niko-niko/create/', views.NikoCreateView.as_view(), name='niko-create'),
]
