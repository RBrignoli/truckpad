from django.contrib import admin
from operations import models

# Register your models here.


@admin.register(models.DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(models.DriverReport)
class DriverReportAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id',)
