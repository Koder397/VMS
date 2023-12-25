from django.contrib import admin
from .models import Driver, Diesel, Bus_Route_Details, Rc_Book, Fitness_Certificate, Insurance, Tax, Maintainance, \
    BusLog, Permit, Tyre, Fuel, Rto, Electrical, Mechanical, Quotation

# Register your models here.
admin.site.register(Driver)
class DieselAdmin(admin.ModelAdmin):
    model = Diesel
    list_display = ['paid_person_name', 'petrol_bunk_name','starting_KM','closing_KM','total_KM', 'diesel_filled', 'fuel_consumption']
admin.site.register(Diesel, DieselAdmin)
admin.site.register(Bus_Route_Details)
admin.site.register(Rc_Book)
admin.site.register(Fitness_Certificate)
admin.site.register(Insurance)
admin.site.register(Tax)
admin.site.register(Permit)
admin.site.register(Maintainance)
admin.site.register(BusLog)
admin.site.register(Fuel)
admin.site.register(Tyre)
admin.site.register(Rto)
admin.site.register(Electrical)
admin.site.register(Mechanical)
admin.site.register(Quotation)