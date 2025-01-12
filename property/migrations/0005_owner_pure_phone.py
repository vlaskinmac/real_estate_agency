# Generated by Django 2.2.24 on 2022-03-19 09:36
import phonenumbers

from django.db import migrations


def set_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for phonenumber in Flat.objects.all().iterator():
        phonenumber_ru = phonenumbers.parse(phonenumber.owners_phonenumber, "RU")
        phonenumber.owner_pure_phone = phonenumbers.format_number(phonenumber_ru, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        phonenumber.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0004_auto_20220319_1451'),
    ]


    operations = [
        migrations.RunPython(set_owner_pure_phone),
    ]
