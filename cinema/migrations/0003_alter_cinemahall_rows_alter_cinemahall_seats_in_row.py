# Generated by Django 4.1 on 2024-05-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_actor_cinemahall_genre_movie_actors_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemahall',
            name='rows',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cinemahall',
            name='seats_in_row',
            field=models.IntegerField(default=0),
        ),
    ]