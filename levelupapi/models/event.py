from django.db import models

class Event(models.Model):

    schduler = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    event_time=models.models.DateTimeField(_(""), auto_now=False, auto_now_add=False)
    location = models.Charfield(max_length=50)
