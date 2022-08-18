from django.db import models

# Create your models here.

class Action(models.Model):
    action_id = models.IntegerField(primary_key=True)
    fixedDisplaymentAmount = models.DecimalField(max_digits=20)
    percentageDisplaymentAmount = models.DecimalField(max_digits=20)
    maximumDisplaymentAmount = models.DecimalField(max_digits=20)