from django.db import models

from customers.models import Customer
from productions.models import Production


class DeliveryAddress(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        verbose_name='Заказчик',
        related_name='delivery_address',
    )
    address = models.TextField(
        verbose_name='Адрес',
    )
    contacts = models.TextField(
        verbose_name='Контакты',
        blank=True,
    )

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставок'
        ordering = ['customer']

    def __str__(self):
        return self.customer


class DeliveryOptions(models.Model):
    delivery_name = models.CharField(
        max_length=40,
        verbose_name='Вариант доставки',
        unique=True,
    )

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Вариант доставки'
        verbose_name_plural = 'Варианты доставки'
        ordering = ['delivery_name']

    def __str__(self):
        return self.delivery_name


class Delivery(models.Model):
    production = models.OneToOneField(
        Production,
        on_delete=models.PROTECT,
        verbose_name='Штамп',
        related_name='delivery',
    )
    delivery_options = models.ForeignKey(
        DeliveryOptions,
        on_delete=models.PROTECT,
        verbose_name='Вариант доставки',
        related_name='production',
    )
    delivery_address = models.ForeignKey(
        DeliveryAddress,
        on_delete=models.PROTECT,
        verbose_name='Адрес доставки',
        related_name='production',
    )

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'
        ordering = ['delivery_name']

    def __str__(self):
        return f'{self.production} - {self.delivery_options}'
