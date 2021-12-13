from django.db import models

# Create your models here.


class UserModel (models.Model):
    id: models.PositiveIntegerField(unique=True, primary_key=True)
    user_name: models.CharField(max_length=50, unique=True)
    name: models.CharField(max_length=50)
    surname: models.CharField(max_length=50, blank=True)
    email: models.EmailField(unique=True)
    password: models.CharField(max_length=30)


class EventModel (models.Model):
    id: models.PositiveIntegerField(unique=True, primary_key=True)
    name: models.CharField(max_length=150, unique=True)
    game_id: models.PositiveSmallIntegerField()
    date: models.DateTimeField()
    author_id: UserModel.id()
    description: models.TextField(max_length=2000)
    status: models.PositiveSmallIntegerField()
    recording: models.URLField()


class UserEvent (models.Model):
    user_id: UserModel.id
    event_id: EventModel.id