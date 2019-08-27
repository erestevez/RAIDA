import self as self
from django import forms
from .models import registro


class subir(forms.ModelForm):
    class Meta:
        model = registro
        fields=[
            'usuario',
            'dirip',
            'area',
            'aida',
            'inven',
            'sello',
        ]
        widgets={
            'usuario':forms.TextInput(attrs={'id':'usuario','class':'form-control','placeholder':'Nombre de Usuario'}),
            'dirip': forms.TextInput(attrs={'id':'dirip','class': 'form-control','placeholder':'Direccion Ip'}),
            'area': forms.Select(attrs={'class': 'form-control','placeholder':'Area'}),
            'aida': forms.FileInput(attrs={'class':'btn btn-outline-secondary','accept':'text/html','id':'fileinput'}),
            'inven': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inventario'}),
            'sello': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero de Sello'}),
        }

    def clean_usuario(self):
        usuario = self.cleaned_data['usuario']
        if not usuario.isalpha():
            raise forms.ValidationError('El usuario no puede contener numeros')
        return usuario


