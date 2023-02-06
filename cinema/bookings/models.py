from django.contrib.auth.models import User
from django.db import models

from movies.models import Movie
from rooms.models import Room


class Seat(models.Model):
    row = models.PositiveSmallIntegerField()
    number = models.PositiveSmallIntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room.name} - Row {self.row} Seat {self.number}'


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def __str__(self):
        return f'{self.movie.title} - {self.room.name} - {self.start_at}'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.show.movie.title} - {self.seat.room.name} - Row {self.seat.row} Seat {self.seat.number}'
