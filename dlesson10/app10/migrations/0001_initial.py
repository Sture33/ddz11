# Generated by Django 4.2.6 on 2023-11-06 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anceta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('hobbies', models.TextField()),
                ('favourite_mosics', models.TextField()),
                ('favourite_movies', models.TextField()),
                ('favourite_books', models.TextField()),
                ('favourite_anime', models.TextField()),
            ],
        ),
    ]
