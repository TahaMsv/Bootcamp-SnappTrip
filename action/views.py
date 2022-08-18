from argparse import Action
from django.shortcuts import render


# Create your views here.
def apply_rule(rule_type, old_price, action):
    new_price = 0
    if rule_type == 'D':
        new_price = old_price - min(action.f + old_price * (action.p / 100), action.m)
    elif rule_type == 'M':
        new_price = old_price + min(action.f + old_price * (action.p / 100), action.m)
    return new_price

# def addData():
#     data = Action(0, 10000, 10 , 2000)
#     data.save()
