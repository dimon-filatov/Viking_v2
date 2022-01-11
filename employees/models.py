from django.db import models


class Position(models.Model):
    position_name = models.CharField(
        max_length=30,
        verbose_name='Название должности',
        unique=True,
    )

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['position_name']

    def __str__(self):
        return self.position_name


class Employer(models.Model):
    surname = models.CharField(
        max_length=30,
        verbose_name='Фамилия',
    )
    name = models.CharField(
        max_length=30,
        verbose_name='Имя',
    )
    patronymic = models.CharField(
        max_length=30,
        verbose_name='Отчество',
        blank=True,
    )
    birthday = models.DateField(
        verbose_name='День рождения',
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        verbose_name='Должность',
        related_name='employer',
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['surname']

    def __str__(self):
        return f'{self.surname} {self.name[0]}.{self.patronymic[0]}. - {self.position}'
