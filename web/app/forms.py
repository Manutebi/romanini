from django import forms
from .models import *

class AlarmaForm(forms.ModelForm):

    class Meta:
        model = Alerta
        fields = '__all__'

class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = '__all__'

class OtForm(forms.ModelForm):

    class Meta:
        model = Ot_mecanicos
        fields = '__all__'

class CheckForm(forms.ModelForm):

    class Meta:
        model = Checklist
        fields = '__all__'