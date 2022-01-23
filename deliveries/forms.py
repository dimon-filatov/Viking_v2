from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
from django import forms


from deliveries.models import DeliveryAddress


class DeliveryAddressEditForm(forms.ModelForm):
    class Meta:
        model = DeliveryAddress
        fields = ('customer', 'address', 'contacts',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'mb-2 text-dark'
        self.helper.layout = Layout(
            Row(
                Column('customer', css_class='col-2'),
            ),
            Row(
                Column('address', css_class='col-2'),
                Column('contacts', css_class='col-2'),
            ),
            FormActions(
                Submit('submit', 'Сохранить', css_class='btn btn-success'),
                HTML('<a class="btn btn-danger" href="/">Отмена</a>')
            ),
        )
