# Generated by Django 4.2.3 on 2023-11-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0004_alter_project_visibility"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(blank=True, max_length=256, null=True),
        ),
    ]
