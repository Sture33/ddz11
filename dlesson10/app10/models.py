from django.db import models
from django.urls import reverse


# Create your models here.
class Anceta(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    hobbies = models.TextField()
    favourite_mosics = models.TextField()
    favourite_movies = models.TextField()
    favourite_books = models.TextField()
    favourite_anime = models.TextField()

    def __str__(self):
        return f"{self.pk}-{self.name}, {self.surname}"

    # def get_absolute_url(self):
    #     return f'profile_detail/{self.pk}/'


    def get_absolute_url(self):
        return reverse('profile-detail', args=(self.pk,))
