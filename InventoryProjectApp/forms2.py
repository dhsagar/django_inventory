from django.forms import ModelForm
from .models import Product


class AddEditForm(ModelForm):
    class Meta:
        name=Product
        fields='__all__'
