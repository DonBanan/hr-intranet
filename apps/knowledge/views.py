from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import CategoryForm

from .models import Category, Question


class KnowledgeCategoryList(LoginRequiredMixin, ListView):
    context_object_name = "categories"
    template_name = "knowledge/category/categories_list.html"

    def get_queryset(self):
        return Category.objects.exclude(parent__isnull=False)


class KnowledgeCategoryDetail(LoginRequiredMixin, DetailView):
    model = Category
    context_object_name = "category"
    template_name = "knowledge/category/categories_detail.html"


class QuestionDetail(LoginRequiredMixin, DetailView):
    model = Question
    context_object_name = "question"
    template_name = "knowledge/questions/questions_detail.html"


class QuestionSearchPage(LoginRequiredMixin, ListView):

    template_name = 'knowledge/questions/questions_search_page.html'
    context_object_name = "questions"

    def get_queryset(self):
        search = self.request.GET.get('text', None)
        questions = Question.objects.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )
        return questions

    def get_context_data(self,**kwargs):
        context = super(QuestionSearchPage, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('text', None)
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = '/thanks/'
    template_name = "knowledge/category/categories_create.html"


class FilmUpdateView(LoginRequiredMixin, UpdateView):
    """View to update a film"""


class FilmDeleteView(LoginRequiredMixin, DeleteView):
    """View to delete a film"""
