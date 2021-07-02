from django import forms
from .models import HouseListing, HouseListingPicture

class HouseListingForm(forms.ModelForm):

    class Meta:
        model = HouseListing
        fields = [
            'nome_do_proprietario',
            'sobrenome_do_proprietario',
            'contacto_principal',
            'contacto_secúndario',
            'preço',
            'meses_adiantados',
            'cidade',
            'distrito',
            'bairro',
            'numero_de_divisoes',
            'mobiliada',
            'vedada'
        ]

        help_texts = {
        	'preço': 'O valor da renda mensal em meticais',
        	'meses_adiantados': 'Quantos meses adiantados o cliente terá que pagar inicialmente',
        	'contacto_principal': 'Usado por clientes para poder contactar o proprietario da casa',
        	'numero_de_divisoes': 'O número total de quartos, salas, cozinhas, etc, disponiveis na casa'
        }

class HousePictureForm(forms.ModelForm):
    class Meta:
        model = HouseListingPicture
        fields = [
            'descriçao',
            'picture'
        ]