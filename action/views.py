from django.shortcuts import render


# Create your views here.
def applyRule(ruleType, oldPrice, f, p, m):
    newPrice = 0
    if ruleType == 'D':
        newPrice = oldPrice - max(f + oldPrice * (p / 100), m)
    elif ruleType == 'M':
        newPrice = oldPrice + max(f + oldPrice * (p / 100), m)
    return newPrice
