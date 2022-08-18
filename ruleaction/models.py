from django.db import models
from action.models import Action


class Rule(models.Model):
    RULE_TYPES = (
        ('D', 'DISCOUNT'),
        ('M', 'MARKUP')
    )

    rule_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    rule_type = models.CharField(max_length=1, choices=RULE_TYPES)
    sensitive_condition_list = models.CharField(max_length=1000)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
