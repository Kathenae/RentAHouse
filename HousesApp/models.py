from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

YESNO = [
    ("Sim", "Sim"),
    ("Não", "Não"),
]

MAIN_BEDROOM = "main_bedroom"
BEDROOM = "bedroom"
LIVING_ROOM = "living_room"
DINING_ROOM = "dining_room"
KITCHEN = "kitchen"
BATHROOM = "bathroom"

ROOMCHOICES = [
    (MAIN_BEDROOM, "Quarto Principal"),
    (BEDROOM, "Quarto"),
    (LIVING_ROOM, "Sala de Estar"),
    (DINING_ROOM, "Sala de Jantar"),
    (KITCHEN, "Cozinha"),
    (BATHROOM, "Quarto de Banho"),
]

class MOZAMBIQUE:
    TETE = "Tete"
    MAPUTO = "Maputo"
    GAZA = "Gaza"
    INHAMBANE = "Inhambane"
    MANICA = "Manica"
    SOFALA = "Sofala"
    ZAMBEZIA = "Zambezia"
    NAMPULA = "Nampula"
    CABO_DELGADO = "Cabo Delgado"
    NIASSA = "Niassa"

    CITY_CHOICES = [
        (TETE,"Tete"),
        (MAPUTO,"Maputo"),
        (GAZA,"Gaza"),
        (INHAMBANE,"Inhambane"),
        (MANICA,"Manica"),
        (SOFALA,"Sofala"),
        (ZAMBEZIA,"Zambezia"),
        (NAMPULA,"Nampula"),
        (CABO_DELGADO,"Cabo Delgado"),
        (NIASSA,"Niassa")
    ]

def validate_non_negative(value):
    if value < 0:
        raise ValidationError('Não são permitidos valores negativos', params={'value' : value})

class HouseListing(models.Model):

    # Dados de Registro
    create_by_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='houses'
    )

    data_registrada = models.DateField(default=timezone.now)
    mostrar_na_lista = models.BooleanField(default=True)

    # Proprietario
    nome_do_proprietario = models.CharField(max_length=30)
    sobrenome_do_proprietario = models.CharField(max_length=30)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="O número de telefone deve estar no seguinte formato: +999999999999. Deve conter no maximo 15 digitos")
    contacto_principal = models.CharField(max_length=15, validators=[phone_regex])
    contacto_secúndario = models.CharField(max_length=15, validators=[phone_regex],blank=True,null=True)

    # Preçario
    preço = models.FloatField(default=0.0, validators=[validate_non_negative])
    meses_adiantados = models.IntegerField(default=1, validators=[validate_non_negative])

    # Localizaçao
    cidade = models.CharField(max_length=30, choices=MOZAMBIQUE.CITY_CHOICES)
    distrito = models.CharField(max_length=30,blank=True,null=True)
    bairro = models.CharField(max_length=100)

    # Compartimentos
    numero_de_divisoes = models.IntegerField(validators=[validate_non_negative])
    mobiliada = models.CharField(max_length=6, choices=YESNO)
    vedada= models.CharField(max_length=6, choices=YESNO)

    def get_absolute_url(self):
        return reverse('house_detail', kwargs={'pk': self.pk})


class HouseListingPicture(models.Model):
    
    house = models.ForeignKey(
        to=HouseListing, 
        on_delete=models.CASCADE, 
        related_name="pictures"
    )

    descriçao = models.CharField(max_length=20,choices=ROOMCHOICES)

    picture = models.ImageField(upload_to="images/houses")