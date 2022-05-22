from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import View, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

from simple_history.utils import update_change_reason

from .forms import LoginForm, EditProfileForm

from .models import User


class LoginPageView(View):
    template_name = 'authentication/login.html'
    form_class = LoginForm

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('/')
        else:
            form = self.form_class()
            message = ''
            return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                update_change_reason(user, 'Login')
                return redirect('/')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


class LogoutView(RedirectView):
    url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class EditUserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = "profiles/user_profile.html"
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        update_change_reason(self.request.user, 'Update profile')
        return reverse('index')
