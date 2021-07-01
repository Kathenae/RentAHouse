from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

YESNO = [
    ("Sim", "Sim"),
    ("Não", "Não"),
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
    contacto_principal = models.CharField(max_length=12)
    contacto_secúndario = models.CharField(max_length=12,blank=True,null=True)

    # Preçario
    preço = models.FloatField(default=0.0)
    meses_adiantados = models.IntegerField(default=1)

    # Localizaçao
    cidade = models.CharField(max_length=30, choices=MOZAMBIQUE.CITY_CHOICES)
    distrito = models.CharField(max_length=30,blank=True,null=True)
    bairro = models.CharField(max_length=100)

    # Compartimentos
    numero_de_divisoes = models.IntegerField()
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

    descriçao = models.CharField(max_length=20)

    picture = models.ImageField(upload_to="images/houses")