from django.contrib import admin

# Register your models here.
from donators.models import Donator

class DonatorAdmin(admin.ModelAdmin):
    model = Donator
    list_display = ('name', 'phone', 'address', 'blood_type', 'registered', 'updated')
    prepopulated_fields = {'slug':('name','blood_type',)}

admin.site.register(Donator, DonatorAdmin)