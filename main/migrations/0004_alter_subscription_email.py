# Generated by Django 5.0.6 on 2024-05-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_subscription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
