import requests
from fcm_django.models import FCMDevice
from .models import Notification

class Vaccine:
    def __init__(self, today, regUser):
        self.URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/"
        self.TODAY = today
        self.regUser = regUser
        
    def getVaccineDetail(self):
        district = self.regUser.district_id
        addUrl = "calendarByDistrict"
        params = {"district_id" : district}
        if self.regUser.pincode:
            addUrl = "calendarByPin"
            pincode = self.regUser.pincode
            params = {"pincode" : pincode}
        data = self.callAPI(addUrl, params)
        found = self.checkSeatFound(data)
        if found:
            self.send(found)
        else:
            print("not found")
        return found

    def send(self, found):
        regUser = self.regUser
        token = regUser.token
        device = FCMDevice.objects.filter(registration_id=token)
        for vac in found:
            centerid = vac["center"]
            obj, created = Notification.objects.get_or_create(
                registerUser=regUser,
                ofDate=self.TODAY,
                centerid=centerid,
                defaults={
                    'registerUser': regUser,
                    'ofDate': self.TODAY,
                    'centerid': centerid,
                },
            )
            if created:
                msg = "Hello {name}, according to your need we have found vaccine, Center Id {center}, Place {place}, Pincode {pincode}, Vaccine {vaccine},  ".format(name=regUser.name, center=centerid, place=vac["place"], pincode=vac["pincode"], vaccine=vac["vaccine"], )
                device.send_message(title="Vaccine Related to you need found", body=msg, icon="https://www.touchmediaads.com/img/logo1.png")
                print("sended")
        print("Vaccine Found")
        print(found)
    
    def dataReturn(self, sess, dt):
        return  {
                    'dose1': sess["available_capacity_dose1"],
                    'dose2': sess["available_capacity_dose2"],
                    'age': sess["min_age_limit"],
                    'center': dt["center_id"],
                    'place': dt["name"],
                    'address': dt["address"],
                    'pincode': dt["pincode"],
                    'fee': dt["fee_type"],
                    'vaccine': sess["vaccine"],
                }

    def checkSeatFound(self, data):
        if data:
            toSend = []
            userReg = self.regUser
            data = data['centers']
            if data:
                for dt in data:
                    sessions = dt["sessions"]
                    for sess in sessions:
                        capacity = sess["available_capacity"]
                        if capacity:
                            getDemandData = self.returnByUserDemand(sess, dt["fee_type"])
                            if getDemandData:
                                toSend.append(self.dataReturn(getDemandData, dt))
            return toSend

    def callAPI(self, addUrl, params):
        url = self.URL + str(addUrl)
        district = self.regUser.district_id
        params['date'] = self.TODAY
        response = requests.get(url, params)
        print(response.url)
        if response.status_code == 200:
            return response.json()
        else:
            print(str(response.status_code) + " Error occur")
            return False

    def returnByUserDemand(self, data, fee):
        ageis = int(data["min_age_limit"])
        userReg = self.regUser
        if userReg.under18:
            if ageis >= 45:
                return False
        else:
            if ageis >= 18 and ageis < 45:
                return False

        if userReg.doseType:
            if not data["available_capacity_dose1"]:
                return False
        else:
            if not data["available_capacity_dose2"]:
                return False

        if userReg.paidType:
            if fee != "Free":
                return False
        else:
            if fee != "Paid":
                return False
        return data