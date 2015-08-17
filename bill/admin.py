from django.contrib import admin
from .models import Person, Bill

class PersonAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'flat_no', 'wing')

class BillAdmin(admin.ModelAdmin):
    # ...
    list_display = ('month', 'user', 'due_date')

admin.site.register(Person, PersonAdmin)
admin.site.register(Bill, BillAdmin)
# Register your models here.
