from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
from django import forms

from productions.models import Production


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ('customer', 'our_number', 'customers_number', 'constructor', 'manager', 'comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.label_class = 'mb-2 text-dark'
        self.helper.layout = Layout(
            Row(
                Column('our_number', css_class='col-12 col-md-4'),
                Column('customer', css_class='col-12 col-md-4'),
                Column('customers_number', css_class='col-12 col-md-4'),
            ),
            Row(
                Column('constructor', css_class='col-12 col-md-4'),
                Column('manager', css_class='col-12 col-md-4'),
            ),
            'comment',
            FormActions(
                Submit('submit', 'Сохранить', css_class='btn btn-success'),
                HTML('<a class="btn btn-danger" href="/product/read_all">Отмена</a>')
            ),
        )