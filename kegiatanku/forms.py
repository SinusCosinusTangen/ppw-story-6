from django.forms import ModelForm
from .models import peserta, tags

class tambahOrang(ModelForm):
    class Meta:
        model = peserta
        fields = '__all__'

class tambahTag(ModelForm):
    class Meta:
        model = tags
        fields = '__all__'