from django.db import models

from mainapp.models import LowerField


class Customer(models.Model):
    name = LowerField(
        max_length=30,
        verbose_name='Рабочее название',
        unique=True,
    )
    contacts_info = models.TextField(
        verbose_name='Контактная информация',
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True,
    )
    if_individual_price = models.BooleanField(
        verbose_name='Индивидуальные условия',
        default=False,
    )

    is_deleted = models.BooleanField(default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
        ordering = ['name']

    def __str__(self):
        return self.name


class CustomerFull(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        verbose_name='Заказчик',
        related_name='full_name',
    )
    full_name = LowerField(
        max_length=50,
        verbose_name='Полное название',
        unique=True,
    )
    inn = models.IntegerField(
        verbose_name='ИНН',
        unique=True,
    )

    is_deleted = models.BooleanField(default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    class Meta:
        verbose_name = 'Юр. лицо'
        verbose_name_plural = 'Юр. лица'
        ordering = ['customer']

    def __str__(self):
        return self.full_name
