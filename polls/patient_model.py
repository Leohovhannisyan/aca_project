from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.contrib import admin

class PollPatient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.user.first_name)

@admin.register(PollPatient)
class PollPatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

    def user(self, obj):
        return obj.user.username



