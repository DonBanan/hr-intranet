from django.shortcuts import render, redirect
from django.views.generic import View, RedirectView
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm


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
                return redirect('/')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


class LogoutView(RedirectView):
    url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)