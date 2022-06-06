from django.urls import path

from . import views


urlpatterns = [
    path('knowledge/categories/create/', views.CategoryCreateView.as_view(), name='knowledge-category-create'),
    path('knowledge/categories/', views.KnowledgeCategoryList.as_view(), name='knowledge-category-list'),
    path('knowledge/categories/<slug:slug>/', views.KnowledgeCategoryDetail.as_view(),
         name='knowledge-category-detail'),
    path('knowledge/questions/<int:pk>/', views.QuestionDetail.as_view(), name='knowledge-questions-detail'),
    path('knowledge/questions/search/', views.QuestionSearchPage.as_view(), name='knowledge-questions-search'),
]
