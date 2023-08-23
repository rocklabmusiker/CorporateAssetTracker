from django.db import models
from django.contrib.auth.models import User

# Models for asset tracking system.


class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=16, unique=True)
    subscription_status = models.CharField(
        max_length=10,
        choices=[('active', 'Active'), ('inactive', 'Inactive')],
        default='inactive'
    )

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']
        db_table = 'company'

    def __str__(self):
        return self.name


class Device(models.Model):
    # Device condition choices.
    NEW = 'New'
    GOOD = 'Good'
    FAIR = 'Fair'
    POOR = 'Poor'
    DEVICE_CONDITION_CHOICES = [
        (NEW, 'New'),
        (GOOD, 'Good'),
        (FAIR, 'Fair'),
        (POOR, 'Poor')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    serial_number = models.CharField(max_length=255, unique=True)
    condition = models.CharField(
        max_length=50, choices=DEVICE_CONDITION_CHOICES, default=GOOD)
    checked_out = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        ordering = ['serial_number']
        db_table = 'Device'

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    devices = models.ManyToManyField(Device, through='DeviceAssignment')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['user']
        db_table = 'Employee'

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class DeviceAssignment(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Device Assignment'
        verbose_name_plural = 'Device Assignments'
        ordering = ['-updated_at']
        db_table = 'DeviceAssignment'

    def __str__(self):
        status = "returned" if self.return_date else "assigned"
        date = self.return_date or self.assigned_date
        return f"{self.device.name} {status} by {self.employee.user.get_username()} at {date.ctime()}"


def register_company(company_data):
    # Placeholder for registering a company
    company = Company.objects.create(**company_data)
    # ... other registration logic ...
    return company


def provide_payment_details(company):
    # Placeholder for adding payment details for a company
    # In real-world scenarios, this would involve interactions with payment gateways like Stripe, PayPal, etc.
    # For our placeholder, we just activate the subscription
    company.subscription_status = 'active'
    company.save()


def process_monthly_payment(company):
    # Placeholder for monthly payment processing
    # This is where the actual payment processing would happen with a third-party service.
    # For our simulation, we'll assume the payment always succeeds.
    print(f"Processed payment for {company.name}")


def check_subscription_status(company):
    # Placeholder function to check if a company's subscription is active
    if company.subscription_status == 'active':
        return True
    return False
