from django.contrib import admin

from user.models import User, Fullname, Address

# Register your models here.
admin.site.register(User)
admin.site.register(Fullname)
admin.site.register(Address)
