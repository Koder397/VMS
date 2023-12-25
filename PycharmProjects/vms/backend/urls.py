from django.contrib.auth.decorators import login_required
from django.urls import path

from backend.views import DriverList, DriverCreate, DriverUpdate, DriverDelete, Rc_BookList, \
    Rc_BookCreate, Rc_BookUpdate, Rc_BookDelete, Fitness_CertificateList, Fitness_CertificateCreate, \
    Fitness_CertificateUpdate, Fitness_CertificateDelete, InsuranceList, InsuranceUpdate, InsuranceCreate, \
    InsuranceDelete, TaxCreate, TaxList, TaxDelete, TaxUpdate, PermitList, PermitCreate, PermitUpdate, PermitDelete, \
    Bus_Route_DetailsList, Bus_Route_DetailsCreate, Bus_Route_DetailsUpdate, Bus_Route_DetailsDelete, BusLogList, \
    BusLogCreate, BusLogUpdate, BusLogDelete, DieselList, DieselCreate, DieselDelete, DieselUpdate, MaintainanceList, \
    MaintainanceCreate, MaintainanceUpdate, MaintainanceDelete, FuelList, FuelCreate, FuelUpdate, FuelDelete, TyreList, \
    TyreCreate, TyreUpdate, TyreDelete, PaintingList, PaintingCreate, PaintingUpdate, PaintingDelete, ElectricalList, \
    ElectricalCreate, ElectricalUpdate, ElectricalDelete, MechanicalList, MechanicalDelete, MechanicalUpdate, \
    MechanicalCreate, RtoList, RtoCreate, RtoDelete, RtoUpdate, QuotationList, QuotationCreate, QuotationUpdate, \
    QuotationDelete, Dashboard

urlpatterns = [

    #Dashboard
    path('', Dashboard.as_view()),

    # Driver
    path('driver', DriverList.as_view()),
    path('driver/create', DriverCreate.as_view()),
    path('driver/update/<pk>', DriverUpdate.as_view()),
    path('driver/delete/<pk>', DriverDelete.as_view()),

    # Rc_Book
    path('rc_book', Rc_BookList.as_view()),
    path('rc_book/create', Rc_BookCreate.as_view()),
    path('rc_book/update/<pk>', Rc_BookUpdate.as_view()),
    path('rc_book/delete/<pk>', Rc_BookDelete.as_view()),

    # Fitness_Certificate
    path('fitness_certificate', Fitness_CertificateList.as_view()),
    path('fitness_certificate/create', Fitness_CertificateCreate.as_view()),
    path('fitness_certificate/update/<pk>', Fitness_CertificateUpdate.as_view()),
    path('fitness_certificate/delete/<pk>', Fitness_CertificateDelete.as_view()),

    # Insurance
    path('insurance', InsuranceList.as_view()),
    path('insurance/create', InsuranceCreate.as_view()),
    path('insurance/update/<pk>', InsuranceUpdate.as_view()),
    path('insurance/delete/<pk>', InsuranceDelete.as_view()),

    # Tax
    path('tax', TaxList.as_view()),
    path('tax/create', TaxCreate.as_view()),
    path('tax/update/<pk>', TaxUpdate.as_view()),
    path('tax/delete/<pk>', TaxDelete.as_view()),

    # Permit
    path('permit', PermitList.as_view()),
    path('permit/create', PermitCreate.as_view()),
    path('permit/update/<pk>', PermitUpdate.as_view()),
    path('permit/delete/<pk>', PermitDelete.as_view()),

    # Bus_Route_Details
    path('bus_route_details', Bus_Route_DetailsList.as_view()),
    path('bus_route_details/create', Bus_Route_DetailsCreate.as_view()),
    path('bus_route_details/update/<pk>', Bus_Route_DetailsUpdate.as_view()),
    path('bus_route_details/delete/<pk>', Bus_Route_DetailsDelete.as_view()),

    # BusLog
    path('buslog', BusLogList.as_view()),
    path('buslog/create', BusLogCreate.as_view()),
    path('buslog/update/<pk>', BusLogUpdate.as_view()),
    path('buslog/delete/<pk>', BusLogDelete.as_view()),

    # Diesel
    path('diesel', DieselList.as_view()),
    path('diesel/create', DieselCreate.as_view()),
    path('diesel/update/<pk>', DieselUpdate.as_view()),
    path('diesel/delete/<pk>', DieselDelete.as_view()),

    # Maintainance
    path('maintainance', MaintainanceList.as_view()),
    path('maintainance/create', MaintainanceCreate.as_view()),
    path('maintainance/update/<pk>', MaintainanceUpdate.as_view()),
    path('maintainance/delete/<pk>', MaintainanceDelete.as_view()),

    # Fuel
    path('fuel', FuelList.as_view()),
    path('fuel/create', FuelCreate.as_view()),
    path('fuel/update/<pk>', FuelUpdate.as_view()),
    path('fuel/delete/<pk>', FuelDelete.as_view()),

    # Tyre
    path('tyre', TyreList.as_view()),
    path('tyre/create', TyreCreate.as_view()),
    path('tyre/update/<pk>', TyreUpdate.as_view()),
    path('tyre/delete/<pk>', TyreDelete.as_view()),

    # Painting
    path('painting', PaintingList.as_view()),
    path('painting/create', PaintingCreate.as_view()),
    path('painting/update/<pk>', PaintingUpdate.as_view()),
    path('painting/delete/<pk>', PaintingDelete.as_view()),

    # Electrical
    path('electrical', ElectricalList.as_view()),
    path('electrical/create', ElectricalCreate.as_view()),
    path('electrical/update/<pk>', ElectricalUpdate.as_view()),
    path('electrical/delete/<pk>', ElectricalDelete.as_view()),

    # Mechanical
    path('mechanical', MechanicalList.as_view()),
    path('mechanical/create', MechanicalCreate.as_view()),
    path('mechanical/update/<pk>', MechanicalUpdate.as_view()),
    path('mechanical/delete/<pk>', MechanicalDelete.as_view()),

    # Rto
    path('rto', RtoList.as_view()),
    path('rto/create', RtoCreate.as_view()),
    path('rto/update/<pk>', RtoUpdate.as_view()),
    path('rto/delete/<pk>', RtoDelete.as_view()),

    # Quotation
    path('quotation', QuotationList.as_view()),
    path('quotation/create', QuotationCreate.as_view()),
    path('quotation/update/<pk>', QuotationUpdate.as_view()),
    path('quotation/delete/<pk>', QuotationDelete.as_view()),

]