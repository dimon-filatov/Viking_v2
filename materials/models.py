from django.db import models

from productions.models import Production


class MaterialType(models.Model):
    material_type = models.CharField(
        max_length=40,
        verbose_name='Тип материала',
        unique=True,
    )

    class Meta:
        verbose_name = 'Тип материала'
        verbose_name_plural = 'Типы материалов'
        ordering = ['materials_type']

    def __str__(self):
        return self.material_type


class Material(models.Model):
    material_type = models.ForeignKey(
        MaterialType,
        on_delete=models.PROTECT,
        verbose_name='Тип материала',
        related_name='materials',
    )
    material = models.CharField(
        max_length=100,
        verbose_name='Название',
        unique=True,
    )

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        ordering = ['material_type']

    def __str__(self):
        return f'{self.material_type} - {self.material}'


class ProductionMaterials(models.Model):
    product = models.OneToOneField(
        Production,
        on_delete=models.PROTECT,
        verbose_name='Штамп',
        related_name='materials',
    )
    plywood = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        verbose_name='Фанера',
        related_name='plywood_in_production',
    )
    plywood_length = models.FloatField(
        verbose_name='Длина фанеры',
        default=0,
    )
    plywood_width = models.FloatField(
        verbose_name='Ширина фанеры',
        default=0,
    )
    cut = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        verbose_name='Тип ножа',
        null=True,
        blank=True,
        related_name='cut_in_production',
    )
    length_of_cut = models.FloatField(
        verbose_name='Метраж ножа',
        default=0,
    )
    crease = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        verbose_name='Тип биговки',
        null=True,
        blank=True,
        related_name='crease_in_production',
    )
    length_of_crease = models.FloatField(
        verbose_name='Метраж биговок',
        default=0,
    )
    punches_1 = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        verbose_name='Тип пробойника',
        null=True,
        blank=True,
        related_name='punches_1_in_production',
    )
    count_punches_1 = models.IntegerField(
        verbose_name='Количество пробойников',
        default=0,
    )
    punches_2 = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        verbose_name='Тип пробойника 2',
        null=True,
        blank=True,
        related_name='punches_2_in_production',
    )
    count_punches_2 = models.IntegerField(
        verbose_name='Количество пробойников 2',
        default=0,
    )
    rubber_1 = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        verbose_name='Тип резины',
        null=True,
        blank=True,
        related_name='rubber_1_in_production',
    )
    count_rubber_1 = models.IntegerField(
        verbose_name='Метраж резины',
        default=0,
    )
    rubber_2 = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        verbose_name='Тип резины 2',
        null=True,
        blank=True,
        related_name='rubber_2_in_production',
    )
    count_rubber_2 = models.IntegerField(
        verbose_name='Метраж резины 2',
        default=0,
    )
    additionally_1 = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        verbose_name='Дополнительные элементы 1',
        null=True,
        blank=True,
        related_name='additionally_1_in_production',
    )
    count_additionally_1 = models.IntegerField(
        verbose_name='Метраж дополнительного поля 1',
        default=0,
    )
    additionally_2 = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        verbose_name='Дополнительные элементы 2',
        null=True,
        blank=True,
        related_name='additionally_2_in_production',
    )
    count_additionally_2 = models.IntegerField(
        verbose_name='Метраж дополнительного поля 2',
        default=0,
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True,
    )

    class Meta:
        verbose_name = 'Материалы на штампе'
        verbose_name_plural = 'Материалы на штампе'
        ordering = ['product']

    def __str__(self):
        return f'{self.product}'
