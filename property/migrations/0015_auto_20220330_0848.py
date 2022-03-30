# Generated by Django 2.2.24 on 2022-03-30 05:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20220330_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='normalaized_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='', max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner',
            field=models.TextField(blank=True, db_index=True, default='', verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='phone_number',
            field=models.CharField(blank=True, db_index=True, default='', max_length=20, verbose_name='Номер владельца'),
        ),
    ]
