# Generated by Django 2.2.24 on 2022-03-20 07:30

from django.db import migrations


def add_owner_flats(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')

    # flat = Flat.objects.all()
    owner = Owner.objects.all()
    for flat in Flat.objects.all():
        flat.get_or_create(owner_id=owner.id)
        flat.save()

    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        owner, _ = Owner.objects.get_or_create(
            owner=flat.owner,
            phone_number=flat.owners_phonenumber,
        )
        owner.apartments_in_property.add(flat)
        owner.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0011_auto_20220328_1121'),
    ]

    operations = [
        migrations.RunPython(add_owner_flats),
    ]
