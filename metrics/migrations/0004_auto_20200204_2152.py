# Generated by Django 3.0 on 2020-02-04 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0003_auto_20200202_2304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientmetrics',
            old_name='attributes',
            new_name='attributes_id',
        ),
    ]