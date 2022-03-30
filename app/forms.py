from django.forms import ModelForm
from app.models import fruits, region

# Create the form class.
class fruitsForm(ModelForm):
    class Meta:
         model = fruits
         fields = ['fruits', 'region']
