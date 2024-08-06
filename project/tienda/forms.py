from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, Categoria

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProductoForm(forms.ModelForm):
    nueva_categoria = forms.CharField(required=False, max_length=100, label='Nueva Categoría')

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'stock', 'categoria']

    def clean(self):
        cleaned_data = super().clean()
        imagen = cleaned_data.get('imagen')
        nueva_categoria = cleaned_data.get('nueva_categoria')
        categoria = cleaned_data.get('categoria')

        # Check if the image field is empty
        if not imagen:
            raise forms.ValidationError("Image is required")

        # Handle new category creation
        if nueva_categoria:
            categoria, created = Categoria.objects.get_or_create(nombre=nueva_categoria)
            cleaned_data['categoria'] = categoria

        # Check if a category is selected or created
        if not cleaned_data.get('categoria'):
            raise forms.ValidationError("Please select an existing category or create a new one.")

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        # No need to set a default category here, validation ensures a category is provided
        if commit:
            instance.save()
        return instance
