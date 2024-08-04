from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

import joblib  #for ML incorporation to webapp

# Create your views here.
# This is Toluwalase and he is right here and he is making waves by the Grace

@api_view(["POST"])
def depressionPredictor(request):
    try:
        info = request.data
        age = info["age"]
        number_of_children = info["number_of_children"]
        income = info["income"]
        employment_status = info["employment_status"]
        history_of_mental_illness = info["history_of_mental_illness"]

        infolist = [[age, number_of_children, income, employment_status, history_of_mental_illness]]
        predictor_model = joblib.load("predictor.joblib")
        predicted_value = predictor_model.predict(infolist)[0]
        print(predicted_value)
        return Response({"message": "Success", "payload":{"result": predicted_value}}, status=status.HTTP_200_OK)

    except Exception as ex:
        print(ex)
        return Response({"message": 'error'}, status=status.HTTP_400_BAD_REQUEST)