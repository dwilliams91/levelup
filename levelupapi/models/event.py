from django.db import models

class Event(models.Model):

    schduler = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    event_time=models.CharField(auto_now=False, )
    location = models.Charfield(max_length=50)
