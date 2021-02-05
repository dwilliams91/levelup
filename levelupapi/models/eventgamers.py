from django.db import models

class EventGamers(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)