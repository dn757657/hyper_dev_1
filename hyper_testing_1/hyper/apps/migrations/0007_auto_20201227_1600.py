# Generated by Django 3.0.5 on 2020-12-27 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_auto_20201227_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_tags',
            field=models.ManyToManyField(blank=True, to='apps.Tag'),
        ),
    ]