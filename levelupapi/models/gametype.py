from django.db import models

class GameType(models.Model):

    Label = models.CharField(max_length=50)
    
