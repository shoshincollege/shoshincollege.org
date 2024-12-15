from django.urls import path
from django.views.generic.base import RedirectView

from main import views

FEEDBACK_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeWBKJVxev8e4DwWKaHXynqBEt1hkipnEo6Jgdn99m9p_ymOQ/viewform"

urlpatterns = [
    path("", views.index, name="index"),
    path("classes/", RedirectView.as_view(url="/courses/"), name="classes"),
    path(
        "feedback/",
        RedirectView.as_view(url=FEEDBACK_URL),
        name="classes",
    ),
    path("philosophy/", views.philosophy, name="philosophy"),
    path("courses/2024-fall/", views.courses, name="courses_2024_fall"),
    path("courses/2025-spring/", views.courses, name="courses_2025_spring"),
    path("courses/", views.courses, name="courses"),
    path("code-of-conduct/", views.coc, name="coc"),
    path("about/", views.about, name="about"),
    path("news/", views.NewsList.as_view(), name="news_list"),
    path("news/<slug:slug>/", views.NewsDetail.as_view(), name="news_detail"),
]
