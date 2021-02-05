from django.db import models

class GameType(models.Model):

    Label = models.Charfield(max_length=75)
    
