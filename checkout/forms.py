from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'address', 'town_or_city', 'postcode', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'address': 'Street Address',
            'town_or_city': 'Town or City',
            'postcode': 'Postal Code',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            placeholder = f"{placeholders[field]} *" if self.fields[
                field].required else placeholders[field]
            self.fields[field].widget.attrs.update({
                'class': 'stripe-style-input',
                'placeholder': placeholder
            })
            self.fields[field].label = False

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number should contain just digits.")
        return phone_number
