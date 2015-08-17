# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0002_auto_20150803_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='payble_amt',
            field=models.IntegerField(default=0, verbose_name='Total Amount Due'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='total_charges',
            field=models.IntegerField(default=0, verbose_name='total of charges'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]
