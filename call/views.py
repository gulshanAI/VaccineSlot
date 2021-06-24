from django.shortcuts import render
from django.http import HttpResponse
from .Vaccine import Vaccine
from .models import VaccineRegisteraton
from django.utils.timezone import datetime

def vaccineApi(request):
    regUser = VaccineRegisteraton.objects.all()
    if regUser:
        today = datetime.today().strftime('%d-%m-%Y')
        for reg in regUser:
            vac = Vaccine(today, reg)
            vac.getVaccineDetail()
            return HttpResponse("finding..")
    return HttpResponse("hello..")


def getDate(request):
    today = datetime.today().strftime('%d-%m-%Y')
    return HttpResponse(today)

from rest_framework.response import Response
from .models import VaccineRegisteraton
from .serializers import VaccineRegisteratonSerializer
from rest_framework import status
from rest_framework import viewsets

class RegisterForVaccine(viewsets.ViewSet):
    def create(self, request):
        serializer = VaccineRegisteratonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)