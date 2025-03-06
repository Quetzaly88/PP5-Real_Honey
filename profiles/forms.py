from django import forms
from .models import UserProfile
from django_countries.widgets import CountrySelectWidget


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["full_name", "email", "phone_number", "address", "town_or_city", "postcode", "country"]
        widgets = {"country": CountrySelectWidget()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "address": "Street Address",
            "town_or_city": "Town or City",
            "postcode": "Postcode",
            "country": "Country",
        }

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = placeholders[field]
            self.fields[field].label = False
