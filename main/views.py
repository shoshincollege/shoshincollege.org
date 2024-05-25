from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView

from main import forms, models


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


class NewsList(ListView):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Article.objects.all().order_by("-published_at")
        return models.Article.objects.filter(published_at__isnull=False).order_by(
            "-published_at"
        )


class NewsDetail(DetailView):
    model = models.Article


class Subscribe(SuccessMessageMixin, FormView):
    form_class = forms.Subscription
    template_name = "main/subscribe.html"
    success_url = reverse_lazy("index")
    success_message = "thanks! we've noted down your email address"

    def form_valid(self, form):
        # Handle case: already subscribed
        if models.Subscription.objects.filter(
            email=form.cleaned_data.get("email")
        ).exists():
            self.success_message = "thanks! you are already subscribed but whatever"
            return super().form_valid(form)

        # Handle happy path: email is new
        self.object = form.save()
        return super().form_valid(form)
