from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, RedirectView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

from simple_history.utils import update_change_reason

from .forms import LoginForm, EditProfileForm, EditUserSESForm

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
                if user.seen_welcome is False:
                    return redirect('/')
                else:
                    return redirect('/')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        update_change_reason(request.user, 'Logout')
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class EditUserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = "profiles/user_profile.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        update_change_reason(self.request.user, 'Update profile')
        return reverse('index')


class EditUserSESView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditUserSESForm
    template_name = "profiles/user_ses.html"

    def get_object(self, queryset=None):
        if self.request.user.is_ses:
            raise Http404
        return self.request.user

    def get_success_url(self):
        update_change_reason(self.request.user, 'Permission granted to generate Simple Electronic Signature')
        return reverse('index')
