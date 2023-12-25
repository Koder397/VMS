from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from backend.forms import DriverForm, Rc_bookForm, Fitness_CertificateForm, InsuranceForm, TaxForm, PermitForm, \
    Bus_Route_DetailsForm, BusLogForm, DieselForm, MaintainanceForm, FuelForm, TyreForm, PaintingForm, ElectricalForm, \
    MechanicalForm, RtoForm, QuotationForm
from backend.models import Driver, Rc_Book, Fitness_Certificate, Insurance, Tax, Permit, Bus_Route_Details, BusLog, \
    Diesel, Maintainance, Fuel, Tyre, Painting, Electrical, Mechanical, Rto, Quotation


class Dashboard(TemplateView):

    template_name = "dashboard.html"
#
    def get_context_data(self,*args, **kwargs):
        context = super(Dashboard, self).get_context_data(*args, **kwargs)
        context['title'] = "Dashboard"

        return context

class DriverList(ListView):

    model = Driver
    template_name = 'backend/driver/list.html'

class DriverCreate(CreateView):

    model = Driver
    template_name = 'backend/driver/create.html'
    form_class = DriverForm
    success_url = '/driver'


class DriverUpdate(UpdateView):

    model = Driver
    template_name = 'backend/driver/update.html'
    form_class = DriverForm
    success_url = '/'

class DriverDelete(DeleteView):

    model = Driver
    template_name = 'backend/driver/delete.html'
    success_url = '/'

class Rc_BookList(ListView):

    model = Rc_Book
    template_name = 'backend/Rc_Book/list.html'

class Rc_BookCreate(CreateView):

    model = Rc_Book
    template_name = 'backend/Rc_Book/create.html'
    form_class = Rc_bookForm
    success_url = '/'

class Rc_BookUpdate(UpdateView):

    model = Rc_Book
    template_name = 'backend/Rc_Book/update.html'
    form_class = Rc_bookForm
    success_url = '/'

class Rc_BookDelete(DeleteView):

    model = Rc_Book
    template_name = 'backend/Rc_Book/delete.html'
    success_url = '/'

class Fitness_CertificateList(ListView):

    model = Fitness_Certificate
    template_name = 'backend/Fitness_Certificate/list.html'

class Fitness_CertificateCreate(CreateView):

    model = Fitness_Certificate
    template_name = 'backend/Fitness_Certificate/create.html'
    form_class = Fitness_CertificateForm
    success_url = '/'

class Fitness_CertificateUpdate(UpdateView):

    model = Fitness_Certificate
    template_name = 'backend/Fitness_Certificate/update.html'
    form_class = Fitness_CertificateForm
    success_url = '/'

class Fitness_CertificateDelete(DeleteView):

    model = Fitness_Certificate
    template_name = 'backend/Fitness_Certificate/delete.html'
    success_url = '/'

class InsuranceList(ListView):

    model = Insurance
    template_name = 'backend/Insurance/list.html'

class InsuranceCreate(CreateView):

    model = Insurance
    template_name = 'backend/Insurance/create.html'
    form_class = InsuranceForm
    success_url = '/'

class InsuranceUpdate(UpdateView):

    model = Insurance
    template_name = 'backend/Insurance/update.html'
    form_class = InsuranceForm
    success_url = '/'

class InsuranceDelete(DeleteView):

    model = Insurance
    template_name = 'backend/Insurance/delete.html'
    success_url = '/'

class TaxList(ListView):

    model = Tax
    template_name = 'backend/Tax/list.html'

class TaxCreate(CreateView):

    model = Tax
    template_name = 'backend/Tax/create.html'
    form_class = TaxForm
    success_url = '/'

class TaxUpdate(UpdateView):

    model = Tax
    template_name = 'backend/Tax/update.html'
    form_class = TaxForm
    success_url = '/'

class TaxDelete(DeleteView):

    model = Tax
    success_url = '/'

class PermitList(ListView):

    model = Permit
    template_name = 'backend/Permit/list.html'

class PermitCreate(CreateView):

    model = Permit
    template_name = 'backend/Permit/create.html'
    form_class = PermitForm
    success_url = '/'

class PermitUpdate(UpdateView):

    model = Permit
    template_name = 'backend/Permit/update.html'
    form_class = PermitForm
    success_url = '/'

class PermitDelete(DeleteView):

    model = Permit
    success_url = '/'

class Bus_Route_DetailsList(ListView):

    model = Bus_Route_Details
    template_name = 'backend/Bus_Route_Details/list.html'

class Bus_Route_DetailsCreate(CreateView):

    model = Bus_Route_Details
    template_name = 'backend/Bus_Route_Details/create.html'
    form_class = Bus_Route_DetailsForm
    success_url = '/'

class Bus_Route_DetailsUpdate(UpdateView):

    model = Bus_Route_Details
    template_name = 'backend/Bus_Route_Details/update.html'
    form_class = Bus_Route_DetailsForm
    success_url = '/'

class Bus_Route_DetailsDelete(DeleteView):

    model = Bus_Route_Details
    success_url = '/'

class BusLogList(ListView):

    model = Bus_Route_Details
    template_name = 'backend/BusLog/list.html'

class BusLogCreate(CreateView):

    model = Bus_Route_Details
    template_name = 'backend/BusLog/create.html'
    form_class = BusLogForm
    success_url = '/'

class BusLogUpdate(UpdateView):

    model = BusLog
    template_name = 'backend/BusLog/update.html'
    form_class = BusLogForm
    success_url = '/'

class BusLogDelete(DeleteView):

    model = BusLog
    success_url = '/'

class DieselList(ListView):

    model = Diesel
    template_name = 'backend/Diesel/list.html'

class DieselCreate(CreateView):

    model = Diesel
    template_name = 'backend/Diesel/create.html'
    form_class = DieselForm
    success_url = '/'

class DieselUpdate(UpdateView):

    model = Diesel
    template_name = 'backend/BusLog/update.html'
    form_class = DieselForm
    success_url = '/'

class DieselDelete(DeleteView):

    model = Diesel
    success_url = '/'

class MaintainanceList(ListView):

    model = Maintainance
    template_name = 'backend/Maintainance/list.html'

class MaintainanceCreate(CreateView):

    model = Maintainance
    template_name = 'backend/Maintainance/create.html'
    form_class = MaintainanceForm
    success_url = '/'

class MaintainanceUpdate(UpdateView):

    model = Maintainance
    template_name = 'backend/Maintainance/update.html'
    form_class = MaintainanceForm
    success_url = '/'

class MaintainanceDelete(DeleteView):

    model = Maintainance
    success_url = '/'

class FuelList(ListView):

    model = Fuel
    template_name = 'backend/oil/list.html'

class FuelCreate(CreateView):

    model = Fuel
    template_name = 'backend/fuel/create.html'
    form_class = FuelForm
    success_url = '/'

class FuelUpdate(UpdateView):

    model = Fuel
    template_name = 'backend/fuel/update.html'
    form_class = FuelForm
    success_url = '/'

class FuelDelete(DeleteView):

    model = Fuel
    success_url = '/'

class TyreList(ListView):

    model = Tyre
    template_name = 'backend/Tyre/list.html'

class TyreCreate(CreateView):

    model = Tyre
    template_name = 'backend/Tyre/create.html'
    form_class = TyreForm
    success_url = '/'

class TyreUpdate(UpdateView):

    model = Tyre
    template_name = 'backend/Tyre/update.html'
    form_class = TyreForm
    success_url = '/'

class TyreDelete(DeleteView):

    model = Tyre
    success_url = '/'

class PaintingList(ListView):

    model = Painting
    template_name = 'backend/Painting/list.html'

class PaintingCreate(CreateView):

    model = Painting
    template_name = 'backend/Painting/create.html'
    form_class = PaintingForm
    success_url = '/'

class PaintingUpdate(UpdateView):

    model = Painting
    template_name = 'backend/Painting/update.html'
    form_class = PaintingForm
    success_url = '/'

class PaintingDelete(DeleteView):

    model = Painting
    success_url = '/'

class ElectricalList(ListView):

    model = Electrical
    template_name = 'backend/Electrical/list.html'

class ElectricalCreate(CreateView):

    model = Electrical
    template_name = 'backend/Electrical/create.html'
    form_class = ElectricalForm
    success_url = '/'

class ElectricalUpdate(UpdateView):

    model = Electrical
    template_name = 'backend/Electrical/update.html'
    form_class = ElectricalForm
    success_url = '/'

class ElectricalDelete(DeleteView):

    model = Electrical
    success_url = '/'

class MechanicalList(ListView):

    model = Mechanical
    template_name = 'backend/Mechanical/list.html'

class MechanicalCreate(CreateView):

    model = Mechanical
    template_name = 'backend/Mechanical/create.html'
    form_class = MechanicalForm
    success_url = '/'

class MechanicalUpdate(UpdateView):

    model = Mechanical
    template_name = 'backend/Mechanical/update.html'
    form_class = MechanicalForm
    success_url = '/'

class MechanicalDelete(DeleteView):

    model = Mechanical
    success_url = '/'

class RtoList(ListView):

    model = Rto
    template_name = 'backend/Rto/list.html'

class RtoCreate(CreateView):

    model = Rto
    template_name = 'backend/Rto/create.html'
    form_class = RtoForm
    success_url = '/'

class RtoUpdate(UpdateView):

    model = Mechanical
    template_name = 'backend/Rto/update.html'
    form_class = RtoForm
    success_url = '/'

class RtoDelete(DeleteView):

    model = Rto
    success_url = '/'

class QuotationList(ListView):

    model = Quotation
    template_name = 'backend/Quotation/list.html'

class QuotationCreate(CreateView):

    model = Quotation
    template_name = 'backend/Quotation/create.html'
    form_class = QuotationForm
    success_url = '/'

class QuotationUpdate(UpdateView):

    model = Quotation
    template_name = 'backend/Quotation/update.html'
    form_class = QuotationForm
    success_url = '/'

class QuotationDelete(DeleteView):

    model = Quotation
    success_url = '/'