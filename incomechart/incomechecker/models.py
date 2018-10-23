from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MonthlyPay(models.Model):

    JANUARY = 'JANUARY'
    FEBRUARY = 'FEBRUARY'
    MARCH = 'MARCH'
    APRIL = 'APRIL'
    MAY  = 'MAY'
    JUNE = 'JUNE'
    JULY = 'JULY'
    AUGUST = 'AUGUST'
    SEPTEMBER = 'SEPTEMBER'
    OCTOBER = 'OCTOBER'
    NOVEMBER = 'NOVEMBER'
    DECEMBER = 'DECEMBER'

    MONTH = (
        (JANUARY, 'JANUARY'),
    (FEBRUARY,  'FEBRUARY'),
    (MARCH, 'MARCH'),
    (APRIL, 'APRIL'),
    (MAY, 'MAY'),
    (JUNE,  'JUNE'),
    (JULY, 'JULY'),
    (AUGUST, 'AUGUST'),
    (SEPTEMBER, 'SEPTEMBER'),
    (OCTOBER, 'OCTOBER'),
    (NOVEMBER, 'NOVEMBER'),
    (DECEMBER, 'DECEMBER'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=15,
                            choices=MONTH,
                            null=True)

    month_earning = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.month
