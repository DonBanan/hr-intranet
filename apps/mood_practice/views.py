from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View

from simple_history.utils import update_change_reason

from .forms import NikoModelForm

from .models import Niko


class NikoCreateView(LoginRequiredMixin, View):
    model = Niko
    form_class = NikoModelForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_mood = form.save(commit=False)
            new_mood.user = self.request.user
            new_mood.save()
            update_change_reason(self.request.user, 'Set moods')
            return HttpResponseRedirect('/')
