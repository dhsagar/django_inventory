from django import forms
from django.forms import ModelForm
from .models import Product

class AddEditForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        widgets= {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'product_id': forms.NumberInput(attrs={'class':'form-control'}),
            'purchase_date': forms.TextInput(attrs={'class': 'form-control'}),
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'used_in': forms.TextInput(attrs={'class': 'form-control'}),
            'technical_data': forms.Textarea(attrs={'class': 'form-control'}),
            'landed_to': forms.TextInput(attrs={'class': 'form-control'}),
            'landed_till': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'