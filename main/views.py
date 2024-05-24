from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main import models


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


class NewsList(ListView):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Article.objects.all().order_by("-published_at")
        return models.Article.objects.filter(published_at__isnull=False).order_by("-published_at")


class NewsDetail(DetailView):
    model = models.Article
