# Generated by Django 2.2.24 on 2022-03-30 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20220330_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner',
            field=models.CharField(blank=True, db_index=True, default='', max_length=200, verbose_name='ФИО владельца'),
        ),
    ]