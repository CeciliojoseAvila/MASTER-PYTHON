from django import forms
from django.core import validators
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class FormArticle(forms.Form):

    title = forms.CharField(

        label="Titulo",
        max_length= 20,
        required = True,
         widget=forms.TextInput(
             attrs={
                'placeholder': 'ingresa el titulo',
                'class': 'titulo_form_article',
             }
         ),
         validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', 'El titulo está mal formado', 'invalid_title')

         ]

    )

    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators= [
            validators.MaxLengthValidator(100, 'Te has pasado, has colocado mucho texto')
        ]
    )

    content.widget.attrs.update({
                'placeholder': 'ingresa el contenido YAA',
                'class': 'titulo_form_article',
                'id': 'contenido_form'
             })
    

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )
