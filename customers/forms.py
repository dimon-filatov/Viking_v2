from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
from django import forms

from customers.models import Customer, CustomerFull


class CustomerEditForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'contacts_info', 'comment', 'if_individual_price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'mb-2 text-dark'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-2'),
            ),
            Row(
                Column('contacts_info', css_class='col-2 mr-5'),
                Column('comment', css_class='col-2 ml-5'),
            ),
            FormActions(
                Submit('submit', 'Сохранить', css_class='btn btn-success'),
                HTML('<a class="btn btn-danger" href="/customer">Отмена</a>')
            ),
        )


class CustomerFullEditForm(forms.ModelForm):
    class Meta:
        model = CustomerFull
        fields = ('customer', 'full_name', 'inn', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'mb-2 text-dark'
        self.helper.layout = Layout(
            Row(
                Column('customer', css_class='col-2'),
                Column('full_name', css_class='col-2'),
                Column('inn', css_class='col-2'),
            ),
            FormActions(
                Submit('submit', 'Сохранить', css_class='btn btn-success'),
                HTML('<a class="btn btn-danger" href="/customer/customer_full">Отмена</a>')
            ),
        )
