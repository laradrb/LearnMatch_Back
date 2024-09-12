from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return f'Course: {self.name}'