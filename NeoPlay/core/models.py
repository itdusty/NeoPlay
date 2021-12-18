from django.db import models
from django.contrib.auth.models import User # Модель базового пользователя джанго
# Create your models here.


class EventModel(models.Model):
    name = models.CharField(max_length=150, unique=True)
    game = models.PositiveSmallIntegerField()
    date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=2000)
    status = models.PositiveSmallIntegerField()
    recording = models.URLField()

    def get_participants(self):
        return EventUser.objects.filter(event=self)

class EventUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)






