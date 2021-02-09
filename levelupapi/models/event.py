from django.db import models

class Event(models.Model):

    scheduler = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    event_time=models.DateTimeField()
    location = models.CharField(max_length=50)
