# Generated by Django 4.0.2 on 2022-03-04 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicApp', '0002_issuedbooks'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedbooks',
            name='noOfDays',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
