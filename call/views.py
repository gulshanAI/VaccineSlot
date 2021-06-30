from django.shortcuts import render
from django.http import HttpResponse
from .Vaccine import Vaccine
from .models import VaccineRegisteraton
from django.utils.timezone import datetime

def vaccineApi(request):
    regUser = VaccineRegisteraton.objects.all()
    # regUser = VaccineRegisteraton.objects.filter(id=3)
    if regUser:
        today = datetime.today().strftime('%d-%m-%Y')
        data = []
        for reg in regUser:
            vac = Vaccine(today, reg)
            found = vac.getVaccineDetail()
            result = {
                'name' : reg.name,
                'today' : today,
                'found' : found,
            }
            data.append(result)
        return render(request,'showDetail.html', context={'data' : data, 'today' : today})
            # return HttpResponse("finding.. for "+str(today))
    return HttpResponse("No Registeration")


from fcm_django.models import FCMDevice
def noti(request):
    device = FCMDevice.objects.all()
    msg = "Hello {name}, according to your need we have found vaccine, Center Id {center}, Place {place}, Pincode {pincode}, Vaccine {vaccine},  ".format(name="Gulshan", center="18938938", place="Pune", pincode="411041", vaccine="COVID", )
    sendData = {
        "id" : 1,
        "text" : "new Symulti update !",
        "link" : "href://www.symulti.com"
    }
    device.send_message(title="Vaccine Related to you need found", body=msg, icon="https://www.touchmediaads.com/img/logo1.png", data=sendData)
    print("sended")
    return HttpResponse("No Registeration")


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