from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return f'Level: {self.name}'