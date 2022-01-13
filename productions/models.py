from django.db import models

from customers.models import Customer
from employees.models import Employer


class Production(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        verbose_name='Заказчик',
        related_name='production',
    )
    our_number = models.IntegerField(
        verbose_name='Наш номер',
        unique=True,
    )
    customers_number = models.CharField(
        verbose_name='Номер заказчика',
        max_length=100,
        blank=True,
        null=True,
    )
    constructor = models.ForeignKey(
        Employer,
        on_delete=models.PROTECT,
        verbose_name='Конструктор',
        related_name='constructors_production',
    )
    manager = models.ForeignKey(
        Employer,
        on_delete=models.PROTECT,
        verbose_name='Менеджер',
        related_name='manager_production',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    is_deleted = models.BooleanField(default=False)

    comment_for_deleted = models.TextField(
        verbose_name='Причина удаления',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Штамп'
        verbose_name_plural = 'Штампы'
        ordering = ['our_number']

    def __str__(self):
        return f'{self.our_number} | {self.customer}'


class ProductStageOptions(models.Model):
    name = models.CharField(
        max_length=40,
        verbose_name='Название стадии',
    )

    class Meta:
        verbose_name = 'Стадия'
        verbose_name_plural = 'Стадии'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProductStage(models.Model):
    production = models.OneToOneField(
        Production,
        on_delete=models.PROTECT,
        verbose_name='Штамп',
        related_name='product_stage',
    )
    product_stage = models.ForeignKey(
        ProductStageOptions,
        on_delete=models.PROTECT,
        verbose_name='Стадия',
        related_name='product_stage',
    )
    date_of_last_change = models.DateField(
        verbose_name='Дата последнего изменения',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Стадия штампа'
        verbose_name_plural = 'Стадии штампа'
        ordering = ['production']

    def __str__(self):
        return f'{self.production} - {self.product_stage}'


class ProductPrice(models.Model):
    production = models.OneToOneField(
        Production,
        on_delete=models.PROTECT,
        verbose_name='Штамп',
        related_name='product_price',
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    class Meta:
        verbose_name = 'Цена штампа'
        verbose_name_plural = 'Цены штампа'
        ordering = ['production']

    def __str__(self):
        return f'{self.production} - {self.price}'


class ProductTiming(models.Model):
    production = models.OneToOneField(
        Production,
        on_delete=models.PROTECT,
        verbose_name='Штамп',
        related_name='product_timing',
    )
    date_of_start = models.DateField(
        verbose_name='Дата запуска',
    )
    date_of_readiness = models.DateField(
        verbose_name='Дата готовности',
        blank=True,
        null=True,
    )
    deadline = models.DateField(
        verbose_name='Дата сдачи',
    )
    date_of_delivery = models.DateField(
        verbose_name='Дата доставки',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Сроки штампа'
        verbose_name_plural = 'Сроки штампа'
        ordering = ['production']

    def __str__(self):
        return f'{self.production} - {self.deadline}'


class ProductFile(models.Model):
    production = models.OneToOneField(
        Production,
        on_delete=models.PROTECT,
        verbose_name='Штамп',
        related_name='Product_file',
    )
    drawing_file = models.FileField(
        upload_to='drawing file',
        verbose_name='Чертёж',
    )

    class Meta:
        verbose_name = 'Чертёж'
        verbose_name_plural = 'Чертежи'
        ordering = ['production']

    def __str__(self):
        return self.production
