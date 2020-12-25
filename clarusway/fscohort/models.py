from django.db import models
# from django.db.models import aggregates

# Create your models here.


class Student(models.Model):
    sir_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()
    
    def __str__(self):
        return str(self.number)

    
