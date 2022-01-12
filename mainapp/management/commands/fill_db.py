from django.core.management import BaseCommand
import data
from customers.models import Customer
from deliveries.models import DeliveryOptions
from employees.models import Position
from materials.models import MaterialType, Material
from productions.models import ProductStageOptions


class Command(BaseCommand):
    def handle(self, *args, **options):

        Customer.objects.all().delete()
        new_customers = data.data_material['customers']
        for customer in new_customers:
            if 'full_name' in customer:
                full_name = customer['full_name']
            else:
                full_name = ''
            new_customer = Customer(
                name=customer['name'],
                full_name=full_name,
                inn=customer['inn'],
                contacts_info=customer['contacts_info'],
            )
            new_customer.save()

        ProductStageOptions.objects.all().delete()
        new_product_stage_options = data.data_material['product_stage_options']
        for product_stage_options in new_product_stage_options:
            new_product_stage = ProductStageOptions(
                id=product_stage_options['id'],
                name=product_stage_options['name'],
            )
            new_product_stage.save()

        DeliveryOptions.objects.all().delete()
        new_delivery_options = data.data_material['delivery_options']
        for delivery_option in new_delivery_options:
            new_delivery_option = DeliveryOptions(
                id=delivery_option['id'],
                delivery_name=delivery_option['delivery_name'],
            )
            new_delivery_option.save()

        Position.objects.all().delete()
        new_positions = data.data_material['positions']
        for position in new_positions:
            new_position = Position(
                id=position['id'],
                position_name=position['position_name'],
            )
            new_position.save()

        MaterialType.objects.all().delete()
        new_material_types = data.data_material['material_types']
        for material_type in new_material_types:
            new_material_type = MaterialType(
                id=material_type['id'],
                material_type=material_type['material_type'],
            )
            new_material_type.save()

        Material.objects.all().delete()
        new_materials = data.data_material['materials']
        for material in new_materials:
            new_material = Material(
                id=material['id'],
                material_type=MaterialType.objects.get(id=material['material_type']),
                material_name=material['material_name'],
            )
            new_material.save()
