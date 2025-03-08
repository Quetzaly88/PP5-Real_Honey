from django import forms
from .models import UserProfile
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField


class UserProfileForm(forms.ModelForm):
    country = CountryField(blank_label="(Select Country)").formfield(
        widget=CountrySelectWidget(attrs={"class": "form-control"})
    )  # This is the CountryField from django-countries

    class Meta:
        model = UserProfile
        fields = ["full_name", "email", "phone_number", "address", "town_or_city", "postcode", "country"]
        # widgets = {"country": CountrySelectWidget()}

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

        self.fields["full_name"].widget.attrs["autofocus"] = True
