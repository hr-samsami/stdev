from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='movies/posters/')
    duration_min = models.PositiveSmallIntegerField()
    description = models.TextField()
    director = models.CharField(max_length=255)

    def __str__(self):
        return self.title
