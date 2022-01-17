from datetime import datetime

from django.core.management import BaseCommand
import data
from customers.models import Customer
from deliveries.models import DeliveryOptions
from employees.models import Position, Employer
from materials.models import MaterialType, Material
from productions.models import ProductStageOptions, ProductStage, Production


class Command(BaseCommand):
    def handle(self, *args, **options):

        ProductStage.objects.all().delete()
        Production.objects.all().delete()
        ProductStage.objects.all().delete()
        Customer.objects.all().delete()
        ProductStageOptions.objects.all().delete()
        DeliveryOptions.objects.all().delete()
        Material.objects.all().delete()
        MaterialType.objects.all().delete()
        Employer.objects.all().delete()
        Position.objects.all().delete()

        new_customers = data.data_material['customers']
        for customer in new_customers:
            new_customer = Customer(
                name=customer['name'],
                contacts_info=customer['contacts_info'],
            )
            new_customer.save()

        new_product_stage_options = data.data_material['product_stage_options']
        for product_stage_options in new_product_stage_options:
            new_product_stage = ProductStageOptions(
                id=product_stage_options['id'],
                name=product_stage_options['name'],
            )
            new_product_stage.save()

        new_delivery_options = data.data_material['delivery_options']
        for delivery_option in new_delivery_options:
            new_delivery_option = DeliveryOptions(
                id=delivery_option['id'],
                delivery_name=delivery_option['delivery_name'],
            )
            new_delivery_option.save()

        new_positions = data.data_material['positions']
        for position in new_positions:
            new_position = Position(
                id=position['id'],
                position_name=position['position_name'],
            )
            new_position.save()

        new_material_types = data.data_material['material_types']
        for material_type in new_material_types:
            new_material_type = MaterialType(
                id=material_type['id'],
                material_type=material_type['material_type'],
            )
            new_material_type.save()

        new_materials = data.data_material['materials']
        for material in new_materials:
            new_material = Material(
                id=material['id'],
                material_type=MaterialType.objects.get(id=material['material_type']),
                material_name=material['material_name'],
            )
            new_material.save()

        new_employees = data.data_material['employees']
        for employer in new_employees:
            new_employer = Employer(
                surname=employer['surname'],
                name=employer['name'],
                patronymic=employer['patronymic'],
                birthday=datetime.strptime(employer['birthday'], '%d.%m.%Y'),
                position=Position.objects.get(id=employer['position']),
            )
            new_employer.save()
