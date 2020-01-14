"""Users forms."""

# Django
from django import forms


# Los valores que deben ir aca son los que estoy validando en el formulario
# del HTML ademas estos deben coincidir con lo que hemos escrito en los modelos
class ProfileForm(forms.Form):
    """ProfileForm definition."""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
