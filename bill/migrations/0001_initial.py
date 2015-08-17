# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('month', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Month Of Bill')),
                ('statement_date', models.DateField()),
                ('due_date', models.DateField()),
                ('sinking_fund', models.IntegerField(verbose_name='Sinking fund')),
                ('repair_and_maintainance', models.IntegerField(verbose_name='Repair and Maintainance')),
                ('water_charges', models.IntegerField(verbose_name='Water Charges')),
                ('electricity_charges', models.IntegerField(verbose_name='Electricity Charges')),
                ('service_charges', models.IntegerField(verbose_name='Service Charges')),
                ('interest', models.IntegerField(verbose_name='Interest rate')),
                ('penalty', models.IntegerField(verbose_name='Penalty')),
                ('adjustments', models.IntegerField(verbose_name='Adjustments')),
                ('unpaid_due', models.IntegerField(verbose_name='Unpaid due')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of Flat Holder')),
                ('flat_no', models.CharField(max_length=10, verbose_name='Flat No')),
                ('wing', models.CharField(max_length=26, verbose_name='Wing')),
                ('area', models.CharField(max_length=26, verbose_name='Flat Area')),
                ('mobile', models.IntegerField(verbose_name='Mobile No')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='user',
            field=models.ForeignKey(to='bill.Person'),
        ),
    ]
