# Generated by Django 4.2.3 on 2024-07-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
