from django import forms
from .models import Product
from products.widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """
    Form for store owners to add/edit products
    """
    class Meta:
        model = Product
        fields = '__all__'  # Include all product fields

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """Override init method """
        super().__init__(*args, **kwargs)

        # Set custom placeholder text for fields
        placeholders = {
            'name': 'Product Name',
            'description': 'Product Description',
            'season': 'Season (optional)',
            'flavor_tones': 'Flavor Tones (optional)',
        }

        for field_name, field in self.fields.items():
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]
                field.widget.attrs['class'] = 'form-control border-black rounded-0'

        self.fields['category'].widget.attrs['class'] = 'form-control'
