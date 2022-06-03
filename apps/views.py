from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        return context


class HistoricalRecordsList(LoginRequiredMixin, ListView):
    paginate_by = 20
    context_object_name = "records"
    template_name = "historical_records_list.html"

    def get_queryset(self):
        return self.request.user.history.all()
