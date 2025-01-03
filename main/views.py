from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import DetailView, ListView

from main import models


def index(request):
    return render(request, "main/index.html")


def courses(request):
    if request.path == "/courses/2024-fall/":
        return render(request, "main/courses_2024_fall.html")
    elif request.path == "/courses/2025-spring/":
        return render(request, "main/courses_2025_spring.html")
    else:
        return redirect("courses_2025_spring")


def conduct(request):
    return render(request, "main/conduct.html")


def about(request):
    return render(request, "main/about.html")


def philosophy(request):
    return render(request, "main/philosophy.html")


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
