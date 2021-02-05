from django.db import models

class Event(models.Model):

    schduler = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    event_time=models.DateTimeField()
    location = models.CharField(max_length=50)
