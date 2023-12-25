from django import forms

from backend.models import Driver, Rc_Book, Fitness_Certificate, Insurance, Tax, Permit, Bus_Route_Details, BusLog, \
    Diesel, Maintainance, Fuel, Tyre, Painting, Electrical, Mechanical, Rto, Quotation


class DriverForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DriverForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['alternative_contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['licence_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['licence_expired_date'].widget.attrs.update({'class': 'form-control datepicker'})
        self.fields['driver_joining_date'].widget.attrs.update({'class': 'form-control datepicker'})
        self.fields['driver_resigned_date'].widget.attrs.update({'class': 'form-control datepicker'})
        self.fields['driver_incharge'].widget.attrs.update({'class': 'form-control'})
        self.fields['driver_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['driver_license_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Driver
        fields = '__all__'


class Rc_bookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Rc_bookForm, self).__init__(*args, **kwargs)

        self.fields['vehicle_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['chassis_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['engine_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_company'].widget.attrs.update({'class': 'form-control'})
        self.fields['reg_owner_name'].widget.attrs.update({'class': 'form-control'})
        # self.fields['manufacturer_year'].widget.attrs.update({'class': 'form-control'})
        # self.fields['rc_expired_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['rc_image'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Rc_Book
        fields = '__all__'

class Fitness_CertificateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Fitness_CertificateForm, self).__init__(*args, **kwargs)

        # self.fields['paid_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['fc_renewal_officer_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['fitness_from_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['fitness_renewal_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['receipt_image'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Fitness_Certificate
        fields = '__all__'

class InsuranceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InsuranceForm, self).__init__(*args, **kwargs)

        self.fields['insurance_company_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['insurance_policy_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['policy_start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['policy_expired_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['check_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Insurance
        fields = '__all__'

class TaxForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaxForm, self).__init__(*args, **kwargs)

        self.fields['check_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['bank_details'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['pondicherry_tax_amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['pondicherry_from_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['pondicherry_end_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['tamilnadu_tax_amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['tamilnadu_from_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['tamilnadu_end_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['tax_copy_image'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Tax
        fields = '__all__'

class PermitForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PermitForm, self).__init__(*args, **kwargs)

        self.fields['vehicle_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['mode'].widget.attrs.update({'class': 'form-control'})
        self.fields['permit_amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['permit_A_img_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['permit_B_img_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['permit_from_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['permit_expired_date'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Permit
        fields = '__all__'

class Bus_Route_DetailsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Bus_Route_DetailsForm, self).__init__(*args, **kwargs)

        self.fields['vehicle_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['mode'].widget.attrs.update({'class': 'form-control'})
        self.fields['permit_amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['permit_A_img_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['permit_B_img_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['permit_from_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['permit_expired_date'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Bus_Route_Details
        fields = '__all__'

class BusLogForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BusLogForm, self).__init__(*args, **kwargs)

        self.fields['rc_book'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['starting_time'].widget.attrs.update({'class': 'form-control'})
        self.fields['starting_km'].widget.attrs.update({'class': 'form-control'})
        self.fields['from_place'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_place'].widget.attrs.update({'class': 'form-control'})
        self.fields['purpose_of_journey'].widget.attrs.update({'class': 'form-control'})
        self.fields['closing_time'].widget.attrs.update({'class': 'form-control'})
        self.fields['closing_km'].widget.attrs.update({'class': 'form-control'})
        self.fields['total_km'].widget.attrs.update({'class': 'form-control'})
        self.fields['fuel_field'].widget.attrs.update({'class': 'form-control'})
        self.fields['remark'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = BusLog
        fields = '__all__'

class DieselForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DieselForm, self).__init__(*args, **kwargs)

        self.fields['rc_book'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['paid_person_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['petrol_bunk_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['petrol_bunk_address'].widget.attrs.update({'class': 'form-control'})
        self.fields['starting_KM'].widget.attrs.update({'class': 'form-control'})
        self.fields['closing_KM'].widget.attrs.update({'class': 'form-control'})
        self.fields['total_KM'].widget.attrs.update({'class': 'form-control'})
        self.fields['diesel_filled'].widget.attrs.update({'class': 'form-control'})
        self.fields['fuel_consumption'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Diesel
        fields = '__all__'

class MaintainanceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MaintainanceForm, self).__init__(*args, **kwargs)

        self.fields['rc_book'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['driver_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['incharge_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['from_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['to_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['workshop_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['purpose'].widget.attrs.update({'class': 'form-control'})
        self.fields['particulars'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['total'].widget.attrs.update({'class': 'form-control'})
        self.fields['bill_upload'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Maintainance
        fields = '__all__'

class FuelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FuelForm, self).__init__(*args, **kwargs)

        self.fields['rc_book'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['paid_person'].widget.attrs.update({'class': 'form-control'})
        self.fields['oil_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['bill_upload'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Fuel
        fields = '__all__'

class TyreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TyreForm, self).__init__(*args, **kwargs)

        self.fields['rc_book'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['paid_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['brand_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['tyre_size_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['tyre_size'].widget.attrs.update({'class': 'form-control'})
        self.fields['grd'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_of_service'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['bill_upload'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Tyre
        fields = '__all__'

class PaintingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaintingForm, self).__init__(*args, **kwargs)

        self.fields['rc_book'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['color'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['bill_upload'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Painting
        fields = '__all__'

class ElectricalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ElectricalForm, self).__init__(*args, **kwargs)

        self.fields['rc_book'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['particulars'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['electrical_bill_upload'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Electrical
        fields = '__all__'

class MechanicalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MechanicalForm, self).__init__(*args, **kwargs)

        self.fields['rc_book'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['particulars'].widget.attrs.update({'class': 'form-control'})
        self.fields['shop_contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['particulars'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['mechanical_bill_upload'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Mechanical
        fields = '__all__'

class RtoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RtoForm, self).__init__(*args, **kwargs)

        self.fields['rc_book'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['register_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['valid_till'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['mfr_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['fuel'].widget.attrs.update({'class': 'form-control'})
        self.fields['chassis_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['engine_number'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Rto
        fields = '__all__'

class QuotationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(QuotationForm, self).__init__(*args, **kwargs)

        self.fields['rc_book'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['vehicle_register_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['person_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['quotation'].widget.attrs.update({'class': 'form-control'})
        self.fields['quotation_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['quotation_upload_img'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Quotation
        fields = '__all__'