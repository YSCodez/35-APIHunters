from django.contrib import admin

from build.views import register

# Register your models here.
from django.contrib import admin
from build.models import personaldet

class PersonaldetAdmin(admin.ModelAdmin):
    pass
admin.site.register(personaldet, PersonaldetAdmin)