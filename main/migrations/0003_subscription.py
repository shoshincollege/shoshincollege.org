# Generated by Django 5.0.6 on 2024-05-25 11:02

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_article"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("unsubscribe_key", models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
        ),
    ]
