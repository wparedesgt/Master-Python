from django import forms
from django.forms import widgets
from django.core import validators

class FormArticle(forms.Form):
    title = forms.CharField(
        label='Titulo:', 
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa el Titulo',
                'class': 'titulo_form_article'
            }
        ),
        validators =[
            validators.MinLengthValidator(4, 'El titulo es muy corto'),
            validators.RegexValidator('^[A-Za-z0-9ñáéíóú ]*$', 'Utilice Letras y Números solamente', 'titulo invalido')
            
        ]
    )
    content = forms.CharField(
        label='Contenido:',
        widget=forms.Textarea
        )

    content.widget.attrs.update({
        'placeholder': 'Ingresa la descripcion',
                'class': 'titulo_form_content'

    })
    
    
    public_options = [
        (1,'Si'),
        (0,'No')
    ]

    public = forms.TypedChoiceField(
        label='Publicado?',
        choices=public_options
    )