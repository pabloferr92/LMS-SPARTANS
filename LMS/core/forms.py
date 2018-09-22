from django import forms
from .models import Curso


class cursoForm (forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome']