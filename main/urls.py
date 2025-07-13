from django.urls import path
from django.views.generic.base import RedirectView

from main import views

FEEDBACK_URL = "https://docs.google.com/forms/d/1WmH1FCbbpcLzABt2WgxMVhKbotpS_s9EsL_-Z1mSAwI/viewform"

urlpatterns = [
    path("", views.index, name="index"),
    path("classes/", RedirectView.as_view(url="/courses/"), name="classes"),
    path(
        "feedback/",
        RedirectView.as_view(url=FEEDBACK_URL),
        name="classes",
    ),
    path("philosophy/", views.philosophy, name="philosophy"),
    path("courses/", views.CourseList.as_view(), name="course_list"),
    path("courses/<slug:slug>/", views.CourseDetail.as_view(), name="course_detail"),
    path("archive/", views.ArchiveList.as_view(), name="archive"),
    path("conduct/", views.conduct, name="conduct"),
    path("expectations/", views.expectations, name="expectations"),
    path("about/", views.about, name="about"),
    path("news/", views.NewsList.as_view(), name="news_list"),
    path("news/<slug:slug>/", views.NewsDetail.as_view(), name="news_detail"),
]
