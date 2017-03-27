from django.forms import ModelForm
from models import Rankssingle

class MyModelForm(ModelForm):
    class Meta:
        model = Rankssingle
        fields = ['eventid','personid']
