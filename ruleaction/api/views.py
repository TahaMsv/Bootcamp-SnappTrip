from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from ruleaction.views import check_condition


@api_view(['GET', 'POST'])
def calculate_rule(request):
    if request.method == 'POST':
        print(request.data)
        return Response("hi")

    return Response("hist")
