from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
class MyAdminSite(admin.AdminSite):
    site_header= "Users Administration"

admin_site = MyAdminSite(name="myadmin")

class UserAdmin(admin.ModelAdmin):
    list_display=["id","first_name","last_name","username","email"]
    search_fields= ['email','first_name','last_name','username']

admin_site.register(User,UserAdmin)