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

# import telebot
# from telethon.sync import TelegramClient
# from telethon.tl.types import InputPeerUser, InputPeerChannel
# from telethon import TelegramClient, sync, events
import requests
def viewNoti(request):
    api_id = '6522894'
    api_hash = 'baf05e197269ebf7446da65707b5b325'
    token = 'bot token'
    message = "Working..."

    # your phone number
    phone = '+919834125105'

    bot_token = '1689691086:AAGRk8t-StVRxmm6FHfMzCYv0cDKv2Zmx9g'
    bot_chatID = 'touchmediaads_bot'
    bot_message = 'hello'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    print(response.url)

    print(response)
    # return response.json()
    
    # creating a telegram session and assigning
    # it to a variable client
    # client = TelegramClient('session', api_id, api_hash)

    # # connecting and building the session
    # client.connect()
    # print("connecting")
    # in case of script ran first time it will
    # ask either to input token or otp sent to
    # number or sent or your telegram id
    # if not client.is_user_authorized():
    #     client.send_code_request(phone)
    #     # signing in the client
    #     client.sign_in(phone, input('Enter the code: '))
    # try:
    #     # receiver user_id and access_hash, use
    #     # my user_id and access_hash for reference
    #     receiver = InputPeerUser('user_id', 'user_hash')

    #     # sending message using telegram client
    #     client.send_message(receiver, message, parse_mode='html')
    # except Exception as e:
        
    #     # there may be many error coming in while like peer
    #     # error, wwrong access_hash, flood_error, etc
    #     print(e)

    # # disconnecting the telegram session
    # client.disconnect()



    return HttpResponse("hello..")
    # return render(request, "viewNoti.html", context={})
    

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