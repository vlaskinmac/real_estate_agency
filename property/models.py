from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owner = models.ForeignKey(
        'Owner',
        on_delete=models.CASCADE,
        related_name='owners',
        verbose_name='ФИО владельца',
    )

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)
    new_building = models.NullBooleanField(verbose_name='Новостройка', db_index=True)
    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True
    )
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное'
    )
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4'
    )
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж'
    )
    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True
    )
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True
    )
    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    author_like = models.ManyToManyField(
        User,
        related_name='likes',
        verbose_name='Кто лайкнул',
        blank=True,
    )
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True,
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Claim(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='claims',
        verbose_name='Кто пожаловался'
    )
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        related_name='claims',
        verbose_name='Квартира на которую пожаловались'
    )
    body = models.TextField(verbose_name='Текст жалобы')

    def __str__(self):
        return f'Жалоба на квартиру {self.flat} от {self.author}'


class Owner(models.Model):
    owner = models.CharField(
        verbose_name='ФИО владельца',
        max_length=200,
        db_index=True
    )
    phone_number = models.CharField(
        verbose_name='Номер владельца',
        max_length=20,
        db_index=True
    )
    normalaized_phone_number = PhoneNumberField(
        verbose_name='Нормализованный номер владельца',
        default="0",
        blank=True
    )
    apartments_in_property = models.ManyToManyField(
        Flat,
        verbose_name='Квартиры в собственности',
        blank=True,
        related_name='owners'
    )

    def __str__(self):
        return f'Собственник: {self.owner}'
