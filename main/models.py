import uuid

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
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=300, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
        if self.published_at and self.published_at <= today:
            return True
        return False

    @property
    def body_as_html(self):
        markdown = mistune.create_markdown(plugins=["task_lists", "footnotes"])
        return markdown(self.body)

    def get_absolute_url(self):
        path = reverse("news_detail", kwargs={"slug": self.slug})
        return f"{settings.CANONICAL_URL}{path}"

    def __str__(self):
        return f"{self.id}: {self.title}"


class Subscription(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    unsubscribe_key = models.UUIDField(default=uuid.uuid4, unique=True)

    def get_unsubscribe_url(self):
        path = reverse("unsubscribe_key", args={self.unsubscribe_key})
        return f"{settings.CANONICAL_URL}{path}"

    def __str__(self):
        return f"{self.id}: {self.email}"
