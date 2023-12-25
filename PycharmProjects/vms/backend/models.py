from django.db import models

class Driver(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=12)
    alternative_contact = models.CharField(max_length=12)
    licence_number = models.CharField(max_length=30)
    licence_expired_date = models.DateField(blank=True, null=True)
    driver_joining_date = models.DateField(blank=True, null=True)
    driver_resigned_date = models.DateField(blank=True, null=True)
    driver_incharge = models.CharField(max_length=255)
    driver_image = models.ImageField(upload_to="driver")
    driver_license_image = models.ImageField(upload_to="driver", blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.name

    class Meta:
        db_table = 'driver'

class Rc_Book(models.Model):

    id = models.BigAutoField(primary_key=True)
    vehicle_no = models.CharField(max_length=10, blank=True, null=True)
    vehicle_register_no = models.CharField(max_length=10, blank=True, null=True)
    chassis_number = models.CharField(max_length=40)
    engine_number = models.CharField(max_length=30)
    vehicle_type = models.CharField(max_length=12, blank=True, null=True)
    vehicle_company = models.CharField(max_length=20, blank=True, null=True)
    reg_owner_name = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_year = models.DateTimeField(auto_now_add=True)
    rc_expired_date = models.DateField(blank=True, null=True)
    rc_image = models.ImageField(upload_to="rc_book")

    def _str_(self):
        return self.vehicle_register_no

    class Meta:
        db_table = 'rc_book'


class Fitness_Certificate(models.Model):

    id = models.BigAutoField(primary_key=True)
    # owner_name = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    paid_date = models.DateTimeField(auto_now_add=True)
    vehicle_no = models.CharField(max_length=10,blank=True, null=True)
    vehicle_register_no = models.CharField(max_length=20,blank=True, null=True)
    amount = models.CharField(max_length=255,blank=True, null=True)
    fc_renewal_officer_name = models.CharField(max_length=255)
    fitness_from_date = models.DateTimeField(blank=True, null=True)
    fitness_renewal_date = models.DateTimeField(blank=True, null=True)
    receipt_image = models.ImageField(upload_to="fc")


    def _str_(self):
        return self.fitness_renewal_date

    class Meta:
        db_table = 'fitness_certificate'

class Insurance(models.Model):

    id = models.BigAutoField(primary_key=True)
    # driver_name = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    # vehicle_Register_no = models.ForeignKey(Rc_Book, on_delete=models.CASCADE, null=True)
    # vehicle_Register_no = models.ForeignKey(Rc_Book, on_delete=models.CASCADE, blank=True, null=True)
    # vehicle_Register_no = models.ForeignKey(Rc_Book, on_delete=models.CASCADE, blank=True, null=True)
    insurance_company_name = models.CharField(max_length=255,blank=True, null=True)
    insurance_policy_number = models.CharField(max_length=155,blank=True, null=True)
    policy_start_date = models.DateTimeField(blank=True, null=True)
    policy_expired_date = models.DateTimeField(blank=True, null=True)
    check_number = models.CharField(max_length=50)
    amount = models.CharField(max_length=10,blank=True, null=True)

    def _str_(self):
        return self.insurance_company_name

    class Meta:
        db_table = 'insurance'

class Tax(models.Model):

    id = models.BigAutoField(primary_key=True)
    # bus_number = models.ForeignKey(Rc_Book, on_delete=models.CASCADE, blank=True, null=True)
    # rc_book = models.ForeignKey(Rc_Book, on_delete=models.CASCADE, blank=True, null=True)
    # driver = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    # rc_book = models.ForeignKey(Rc_Book, on_delete=models.CASCADE, blank=True, null=True)
    # paid_person_name = models.CharField(max_length=40, blank=True, null=True)
    check_number = models.CharField(max_length=50)
    bank_details = models.TextField()
    vehicle_type = models.CharField(max_length=40, blank=True, null=True)

    vehicle_no = models.CharField(max_length=10, blank=True, null=True)
    vehicle_register_no = models.CharField(max_length=10, blank=True, null=True)



    pondicherry_tax_amount = models.CharField(max_length=30, blank=True, null=True)
    pondicherry_from_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    pondicherry_end_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)


    tamilnadu_tax_amount = models.CharField(max_length=30, blank=True, null=True)
    tamilnadu_from_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    tamilnadu_end_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    tax_copy_image = models.ImageField(upload_to="tax")


    def _str_(self):
        return self.vehicle_register_no

    class Meta:
        db_table = 'tax'


class Permit(models.Model):
    id = models.BigAutoField(primary_key=True)

    vehicle_no = models.CharField(max_length=10, blank=True, null=True)
    vehicle_register_no = models.CharField(max_length=10, blank=True, null=True)

    vehicle_register_name = models.CharField(max_length=40, blank=True, null=True)
    mode = models.CharField(max_length=20)
    permit_amount = models.CharField(max_length=10, blank=True, null=True)

    permit_A_img_upload = models.ImageField(upload_to='permit a')
    permit_B_img_upload = models.ImageField(upload_to='permit b')

    permit_from_date = models.DateTimeField(auto_now_add=True)
    permit_expired_date = models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return self.vehicle_register_name

    class Meta:
        db_table = 'permit'
class Bus_Route_Details(models.Model):

    id = models.BigAutoField(primary_key=True)
    # vehicle_Register_no = models.ForeignKey(Rc_Book, on_delete=models.CASCADE, blank=True, null=True)
    # vehicle_Register_no = models.ForeignKey(Rc_Book, on_delete=models.CASCADE, blank=True, null=True)
    # driver_name = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    # licence_no = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    # driver_contact = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)

    rc_book = models.ForeignKey(Rc_Book, on_delete=models.CASCADE, blank=True, null=True)

    vehicle_no = models.CharField(max_length=10, blank=True, null=True)
    vehicle_register_no = models.CharField(max_length=10, blank=True, null=True)

    driver_name = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)

    bus_route_timing = models.DateTimeField(blank=True, null=True)

    bus_co_ordinator = models.CharField(max_length=255, blank=True, null=True)
    pro_name = models.CharField(max_length=30, blank=True, null=True)
    pro_contact = models.CharField(max_length=12, blank=True, null=True)

    student_name = models.CharField(max_length=30, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=40, blank=True, null=True)
    bus_stop = models.CharField(max_length=50, blank=True, null=True)

    time_picking = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.driver_name

    class Meta:
        db_table = 'bus_route_details'

class BusLog(models.Model):

    id = models.BigAutoField(primary_key=True)
    # name = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    # vehicle_Register_no = models.ForeignKey(Rc_Book, on_delete=models.CASCADE, blank=True, null=True)
    # vehicle_Register_no = models.ForeignKey(Rc_Book, on_delete=models.CASCADE, blank=True, null=True)

    driver_name = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    vehicle_no = models.CharField(max_length=10, blank=True, null=True)
    vehicle_register_no = models.CharField(max_length=10, blank=True, null=True)

    starting_time = models.DateTimeField(auto_now_add=True)
    starting_km = models.CharField(max_length=30, blank=True, null=True)

    from_place = models.CharField(max_length=30, blank=True, null=True)
    end_place = models.CharField(max_length=30, blank=True, null=True)

    purpose_of_journey = models.CharField(max_length=30, blank=True, null=True)

    closing_time = models.DateTimeField(auto_now_add=True)
    closing_km = models.CharField(max_length=30)

    total_km = models.CharField(max_length=30)

    fuel_field = models.CharField(max_length=30)
    remark = models.TextField()

    def _str_(self):
        return self.purpose_of_journey

    class Meta:
        db_table = 'log'

class Diesel(models.Model):

    id = models.BigAutoField(primary_key=True)
    # vehicle_Register_no = models.ForeignKey(Rc_Book, on_delete=models.CASCADE, blank=True, null=True)
    # vehicle_Register_no = models.ForeignKey(Rc_Book, on_delete=models.CASCADE, blank=True, null=True)

    vehicle_no = models.CharField(max_length=10, blank=True, null=True)
    vehicle_register_no = models.CharField(max_length=10, blank=True, null=True)

    paid_person_name = models.CharField(max_length=30,blank=True, null=True)

    petrol_bunk_name = models.CharField(max_length=100,blank=True, null=True)
    petrol_bunk_address = models.TextField()

    starting_KM = models.CharField(max_length=30,blank=True, null=True)
    closing_KM = models.CharField(max_length=30,blank=True, null=True)

    total_KM = models.CharField(max_length=30, blank=True, null=True)
    diesel_filled = models.CharField(max_length=30,blank=True, null=True)
    fuel_consumption = models.CharField(max_length=30, null=True, blank=True)

    def _str_(self):
        return self.petrol_bunk_name


    @property
    def total_KM(self):
        if hasattr(self, 'starting_KM') and hasattr(self, 'closing_KM'):
            return str(int(self.closing_KM) - int(self.starting_KM))
        return None

    def fuel_consumption(self):
        if hasattr(self, 'total_KM') and hasattr(self, 'diesel_filled'):
            return str(int(self.total_KM) / int(self.diesel_filled))
        return None

    class Meta:
        db_table = 'diesel'


class Maintainance(models.Model):
    id = models.BigAutoField(primary_key=True)

    vehicle_no = models.CharField(max_length=10, blank=True, null=True)
    vehicle_register_no = models.CharField(max_length=10, blank=True, null=True)

    driver_name = models.CharField(max_length=30, blank=True, null=True)
    incharge_name = models.CharField(max_length=30, blank=True, null=True)

    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)

    workshop_name = models.CharField(max_length=30, blank=True, null=True)
    purpose = models.CharField(max_length=255, blank=True, null=True)
    particulars = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=20, blank=True, null=True)
    total = models.CharField(max_length=20, blank=True, null=True)
    bill_upload = models.ImageField(upload_to='maintenance_bill')

    def _str_(self):
        return self.workshop_name

    class Meta:
        db_table = 'maintainance'

class Fuel(models.Model):

    id = models.BigAutoField(primary_key=True)
    vehicle_no = models.CharField(max_length=255, blank=True, null=True)
    vehicle_register_no = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=12, blank=True, null=True)
    paid_person = models.CharField(max_length=255, blank=True, null=True)
    bunk_name = models.CharField(max_length=255, blank=True, null=True)
    petrol = models.CharField(max_length=12, blank=True, null=True)
    diesel = models.CharField(max_length=12, blank=True, null=True)
    amount = models.CharField(max_length=12, blank=True, null=True)
    bill_upload = models.ImageField(upload_to="fuel")

    def _str_(self):
        return self.bunk_name

    class Meta:
        db_table = 'fuel'

class Tyre(models.Model):

    id = models.BigAutoField(primary_key=True)
    vehicle_no = models.CharField(max_length=255, blank=True, null=True)
    vehicle_register_no = models.CharField(max_length=255, blank=True, null=True)
    paid_date = models.DateTimeField(blank=True, null=True)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    vehicle_type = models.CharField(max_length=255, blank=True, null=True)
    tyre_size_no = models.CharField(max_length=50, blank=True, null=True)
    tyre_size = models.CharField(max_length=255, blank=True, null=True)
    grd = models.CharField(max_length=8, blank=True, null=True)
    type_of_service = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=255, blank=True, null=True)
    bill_upload = models.ImageField(upload_to="tyre")

    def _str_(self):
        return self.vehicle_register_no

    class Meta:
        db_table = 'tyre'

class Painting(models.Model):

    id = models.BigAutoField(primary_key=True)
    vehicle_no = models.CharField(max_length=50, blank=True, null=True)
    vehicle_register_no = models.CharField(max_length=255, blank=True, null=True)
    vehicle_type = models.CharField(max_length=60, blank=True, null=True)
    color = models.CharField(max_length=40, blank=True, null=True)
    amount = models.CharField(max_length=50, blank=True, null=True)
    bill_upload = models.ImageField(upload_to="painting")

    def _str_(self):
        return self.color

    class Meta:
        db_table = 'painting'

class Electrical(models.Model):

    id = models.BigAutoField(primary_key=True)
    vehicle_no = models.CharField(max_length=255, blank=True, null=True)
    vehicle_register_number = models.CharField(max_length=255, blank=True, null=True)
    particulars = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=50, blank=True, null=True)
    electrical_bill_upload = models.ImageField(upload_to="electrical")

    def _str_(self):
        return self.vehicle_register_number

    class Meta:
        db_table = 'electrical'

class Mechanical(models.Model):

    id = models.BigAutoField(primary_key=True)
    vehicle_no = models.CharField(max_length=255, blank=True, null=True)
    vehicle_register_number = models.CharField(max_length=255, blank=True, null=True)
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    shop_contact = models.CharField(max_length=12, blank=True, null=True)
    particulars = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=255, blank=True, null=True)
    mechanical_bill_upload = models.ImageField(upload_to="mechanical")

    def _str_(self):
        return self.shop_name

    class Meta:
        db_table = 'mechanical'

class Rto(models.Model):

    id = models.BigAutoField(primary_key=True)
    vehicle_no = models.CharField(max_length=255, blank=True, null=True)
    vehicle_register_number = models.CharField(max_length=255, blank=True, null=True)
    register_date = models.DateTimeField(blank=True, null=True)
    valid_till = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField()
    mfr_name = models.CharField(max_length=255, blank=True, null=True)
    fuel = models.CharField(max_length=255, blank=True, null=True)
    chassis_no = models.CharField(max_length=10, blank=True, null=True)
    engine_number = models.CharField(max_length=10, blank=True, null=True)

    def _str_(self):
        return self.name

    class Meta:
        db_table = 'rto'

class Quotation(models.Model):

    id = models.BigAutoField(primary_key=True)
    vehicle_no = models.CharField(max_length=255)
    vehicle_register_no = models.CharField(max_length=255)
    person_name = models.CharField(max_length=255)
    quotation = models.TextField()
    quotation_date = models.DateTimeField()
    amount = models.CharField(max_length=10)
    quotation_upload_img = models.ImageField(upload_to="quotation")

    def _str_(self):
        return self.person_name

    class Meta:
        db_table = 'quotation'