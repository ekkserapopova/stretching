# Generated by Django 5.1.1 on 2024-09-29 19:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fitness_studio", "0003_remove_activities_goals"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="record",
            name="coach",
        ),
    ]
