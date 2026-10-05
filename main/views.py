from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DetailView, ListView

from main import models


def index(request):
    return render(request, "main/index.html")


def nature_of_mind_series(request):
    return render(request, "main/nature_of_mind_series.html")


class ArchiveList(ListView):
    model = models.Course
    template_name = "main/archive.html"

    def get_queryset(self):
        return super().get_queryset().all().order_by("-occured_at")


class CourseList(ListView):
    model = models.Course

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(semester_key="fall-2025")
            .order_by("occured_at")
        )


class CourseDetail(DetailView):
    model = models.Course


def conduct(request):
    return render(request, "main/conduct.html")


def about(request):
    return render(request, "main/about.html")


def theory(request):
    return render(request, "main/theory.html")


def expectations(request):
    return render(request, "main/expectations.html")


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
