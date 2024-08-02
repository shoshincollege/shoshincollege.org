from django.urls import path
from django.views.generic.base import RedirectView

from main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("classes/", RedirectView.as_view(url="/courses/"), name="classes"),
    path("values/", views.values, name="values"),
    path("courses/", views.courses, name="courses"),
    path("code-of-conduct/", views.coc, name="coc"),
    path("about/", views.about, name="about"),
    path("subscribe/", views.Subscribe.as_view(), name="subscribe"),
    path("news/", views.NewsList.as_view(), name="news_list"),
    path("news/<slug:slug>/", views.NewsDetail.as_view(), name="news_detail"),
]
