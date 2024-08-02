from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DetailView, ListView

from main import models


def index(request):
    return render(request, "main/index.html")


def courses(request):
    return render(request, "main/courses.html")


def coc(request):
    return render(request, "main/code_of_conduct.html")


def about(request):
    return render(request, "main/about.html")


def values(request):
    return render(request, "main/values.html")


class NewsList(ListView):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Article.objects.all().order_by("-published_at")
        today = timezone.now().date()
        return (
            models.Article.objects.filter(published_at__isnull=False)
            .filter(published_at__lte=today)
            .order_by("-published_at")
        )


class NewsDetail(DetailView):
    model = models.Article
