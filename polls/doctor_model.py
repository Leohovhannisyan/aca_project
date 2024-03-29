from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin





class PatientTime(models.Model):
    time = models.CharField(max_length=100)

@admin.register(PatientTime)
class PatientTimeAdmin(admin.ModelAdmin):
    list_display = ["id", "display_time"]
    def display_time(self, obj):
        return obj.time



class Doctor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    patient_times = models.ManyToManyField(PatientTime)
    def __str__(self):
        return "{}, {}".format(self.name,self.surname)



@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display =["id", "doctor"]
    def doctor(self,obj):
        return "{}, {}".format(obj.name,obj.surname)
