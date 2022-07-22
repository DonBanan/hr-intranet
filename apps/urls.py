from django.contrib import admin
from django.urls import path, include

from .views import IndexView, HistoricalRecordsList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('historical-records/', HistoricalRecordsList.as_view(), name='historical-records'),
    path('', include('apps.accounts.urls')),
    path('', include('apps.knowledge.urls')),
    path('', include('apps.mood_practice.urls')),
]
