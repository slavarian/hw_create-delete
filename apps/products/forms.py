from django.forms import ModelForm

from products.models import Products


class CreateForm(ModelForm):
    class Meta:
        model = Products
        fields = (
            'name',
            'price',
        )