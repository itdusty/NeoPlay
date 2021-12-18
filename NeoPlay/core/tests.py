from django.test import TestCase
from core.models import EventModel, EventUser
from django.contrib.auth.models import User
# Create your tests here.
class EventModelTest(TestCase):
    def test_event_model_create(self):
        user = User.objects.create(username="Test") # Создадим пользователя
        # он будет автором события
        participant1 = User.objects.create(username="Участник события №1")
        participant2 = User.objects.create(username="Участник события №2")
        newEvent = EventModel.objects.create(
            name="Тестовое событие",
            game=1,
            date="2021-12-13 16:20",
            author=user,
            description="Test",
            status=1,
            recording="https://test.com"
        )
        self.assertEqual(newEvent.name, "Тестовое событие")
        eventUser1 = EventUser.objects.create(event=newEvent, user=participant1)
        eventUser2 = EventUser.objects.create(event=newEvent, user=participant2)
        self.assertEqual(newEvent.get_participants()[0].user, participant1) # проверяем что участник 1 является участником события
        self.assertEqual(newEvent.get_participants()[1].user, participant2) # проверяем что участник 2 является участником события