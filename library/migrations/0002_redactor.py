# Generated by Django 5.1.2 on 2024-10-21 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Redactor",
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
                ("name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                (
                    "created_at",
                    models.DateField(
                        auto_now_add=True,
                        help_text="Введите дату создания редактора",
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        auto_now=True,
                        help_text="Введите дату изменения редактора",
                        verbose_name="Дата изменения",
                    ),
                ),
            ],
        ),
    ]
