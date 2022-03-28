# Generated by Django 2.2.24 on 2022-03-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20220320_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.AlterField(
            model_name='owner',
            name='apartments_in_property',
            field=models.ManyToManyField(
                blank=True, related_name='owners',
                to='property.Flat',
                verbose_name='Квартиры в собственности'
            ),
        ),
    ]
