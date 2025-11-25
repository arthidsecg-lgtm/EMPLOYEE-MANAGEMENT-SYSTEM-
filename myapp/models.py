from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_code = models.CharField(max_length=20, unique=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name


class Employee(models.Model):
    employee_code = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(null=True)
    date_of_joining = models.DateField(null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    designation = models.CharField(max_length=150, null=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=20, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class User(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=150)
    sso_provider = models.CharField(max_length=50)
    sso_id = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20, null=True)  # FIXED INDENTATION
    profile_picture = models.TextField(null=True)
    last_login = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

