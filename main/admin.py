from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjUserAdmin

from main import models

admin.site.site_header = "Shoshin College admin"


@admin.register(models.User)
class UserAdmin(DjUserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "date_joined",
        "last_login",
    )
    list_display_links = ("id", "username")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email", "plan")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    search_fields = ("username", "email")

    ordering = ["-id"]


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "published_at",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "title", "slug")
    ordering = ["-id"]


@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "created_at",
    )
    list_display_links = ("id", "email")
    ordering = ["-id"]
