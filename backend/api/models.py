from django.db import models

class Item(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    citizenship = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    civil_status = models.CharField(max_length=20, blank=True, null=True)
    height_m = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_type = models.CharField(max_length=3, blank=True, null=True)
    gsis_no = models.CharField(max_length=50, blank=True, null=True)
    pagibig_no = models.CharField(max_length=50, blank=True, null=True)
    philhealth_no = models.CharField(max_length=50, blank=True, null=True)
    sss_no = models.CharField(max_length=50, blank=True, null=True)
    tin_no = models.CharField(max_length=50, blank=True, null=True)

    # Family Background
    spouse_surname = models.CharField(max_length=100, blank=True, null=True)
    spouse_first_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_name_ext = models.CharField(max_length=10, blank=True, null=True)
    spouse_middle_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_occupation = models.CharField(max_length=100, blank=True, null=True)
    spouse_employer = models.CharField(max_length=255, blank=True, null=True)
    spouse_business_address = models.CharField(max_length=255, blank=True, null=True)
    spouse_telephone = models.CharField(max_length=20, blank=True, null=True)

    # Educational Background
    vocational = models.CharField(max_length=100, blank=True, null=True)
    elementary = models.CharField(max_length=100, blank=True, null=True)
    secondary = models.CharField(max_length=100, blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"