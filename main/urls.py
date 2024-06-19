from django.urls import path

from main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("classes/", views.classes, name="classes"),
    path("about/", views.about, name="about"),
    path("subscribe/", views.Subscribe.as_view(), name="subscribe"),
    path("news/", views.NewsList.as_view(), name="news_list"),
    path("news/<slug:slug>/", views.NewsDetail.as_view(), name="news_detail"),
]
