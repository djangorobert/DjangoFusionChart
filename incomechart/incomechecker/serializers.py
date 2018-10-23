from rest_framework import serializers
from incomechecker.models import MonthlyPay

class MonthlyPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyPay
        fields = ('id', 'month', 'month_earning')
