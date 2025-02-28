import mistune
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone


class User(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(
        blank=True,
        null=True,
        unique=True,
    )


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=300, unique=True)
    body = models.TextField()
    published_at = models.DateField(
        default=timezone.now,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["-published_at", "-created_at"]

    @property
    def is_published(self):
        today = timezone.now().date()
        return bool(self.published_at and self.published_at <= today)

    @property
    def body_as_html(self):
        markdown = mistune.create_markdown(plugins=["task_lists", "footnotes"])
        return markdown(self.body)

    def get_absolute_url(self):
        path = reverse("news_detail", kwargs={"slug": self.slug})
        return f"{settings.CANONICAL_URL}{path}"

    def __str__(self):
        return f"{self.id}: {self.title}"


class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    occured_at = models.DateField()  # date of first session
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=300, unique=True)
    overview = models.TextField()
    body = models.TextField()
    teacher = models.TextField()
    semester_key = models.CharField(max_length=50, default="spring-2025")
    apply_url = models.URLField(null=True, blank=True)

    @property
    def overview_as_html(self):
        markdown = mistune.create_markdown(plugins=["task_lists", "footnotes"])
        return markdown(self.overview)

    @property
    def body_as_html(self):
        markdown = mistune.create_markdown(plugins=["task_lists", "footnotes"])
        return markdown(self.body)

    @property
    def teacher_as_html(self):
        markdown = mistune.create_markdown(plugins=["task_lists", "footnotes"])
        return markdown(self.teacher)

    @property
    def semester_key_display(self):
        if not self.semester_key:
            return ""
        parts = self.semester_key.split("-")
        if len(parts) != 2:
            return self.semester_key
        season, year = parts
        return f"{season.capitalize()} {year}"

    def __str__(self):
        return f"{self.id}: {self.title}"
