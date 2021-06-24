from django.db import models
from django.core.validators import  RegexValidator
from fcm_django.models import FCMDevice
phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be entered in the format: '9876543210'. Up to 10 digits allowed.")

class VaccineRegisteraton(models.Model):
    name = models.CharField(max_length=250)
    token = models.TextField()
    mobile = models.CharField(validators=[phone_regex], max_length=12, null=True, blank=True)
    under18 = models.BooleanField(default=True) #True means Under 18
    doseType = models.BooleanField(default=True) #True means DOSE 1
    paidType = models.BooleanField(default=True) #True means Free
    pincode = models.IntegerField(null=True, blank=True)
    district_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
        
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            token = self.token
            VaccineRegisteraton.objects.filter(token=token).delete()
            FCMDevice.objects.filter(registration_id=token).delete()
        super(VaccineRegisteraton, self).save(*args, **kwargs)
        obj, created = FCMDevice.objects.get_or_create(
            registration_id= self.token,
            defaults={
                'name': self.name,
                'registration_id': self.token,
                'type': "web",
            },
        )

class Notification(models.Model):
    registerUser = models.ForeignKey(VaccineRegisteraton, on_delete=models.CASCADE, null=False)
    ofDate = models.CharField(max_length=15)
    centerid = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.centerid
    