from django.db import models

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('financial-accounting', 'Financial Accounting'),
        ('marketing-management', 'Marketing Management'),
        ('strategic-management', 'Strategic Management'),
        ('business-law', 'Business Law'),
        ('international-business', 'International Business'),
    ]
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('standard', 'Standard'),
        ('advanced', 'Advanced'),
    ]
    TIME_CHOICES = [
        ('1hr', '1hr'),
        ('1-3hr', '1-3hr'),
        ('3-6hr', '3-6hr'),
    ]
    SESSION_TIME_CHOICES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Any time', 'Any time'),
    ]

    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=30, choices=DIFFICULTY_CHOICES)
    time_required = models.CharField(max_length=30, choices=TIME_CHOICES)
    session_time = models.CharField(max_length=30, choices=SESSION_TIME_CHOICES)

    # Otros campos según tu modelo

    def __str__(self):
        return f"{self.category} - {self.difficulty}"