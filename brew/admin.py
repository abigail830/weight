from django.contrib import admin

# Register your models here.
from .models import BrewInfo

class MyAdminSite(admin.AdminSite):
    site_title = 'Brew Recording'
    site_header = 'Brew Info Mgr'

admin_site = MyAdminSite()

admin_site.register(BrewInfo)
