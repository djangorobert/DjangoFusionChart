# Generated by Django 2.1.2 on 2018-10-20 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomechecker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlypay',
            name='month_earning',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]