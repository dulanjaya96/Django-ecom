# Generated by Django 4.2.6 on 2023-11-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_rename_created_at_order_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='street_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
