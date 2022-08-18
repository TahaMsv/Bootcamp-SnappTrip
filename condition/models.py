from django.db import models

# Create your models here.

class Condition(models.Model):
    condiotion = models.CharField(max_length=255, primary_key=True)
    id = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return ' '.join(self.condiotion.split('-')) 


