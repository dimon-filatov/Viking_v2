from django.db import models


class Customer(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Рабочее название',
        unique=True,
    )
    full_name = models.CharField(
        max_length=50,
        verbose_name='Полное название',
        unique=True,
    )
    inn = models.IntegerField(
        verbose_name='ИНН',
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
