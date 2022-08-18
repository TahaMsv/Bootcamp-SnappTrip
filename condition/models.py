from django.db import models

# Create your models here.

class Condition(models.Model):
    condiotion = models.CharField(max_length=255, primary_key=True)
    id = models.IntegerField(unique=True)
    name= models.CharField(max_length=255)
    operator= models.CharField(max_length=7)
    value = models.CharField(max_length=255)

    def __str__(self) -> str:
        return ' '.join(self.condiotion.split('-')) 


