from django.db import models


class LowerField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LowerField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()
