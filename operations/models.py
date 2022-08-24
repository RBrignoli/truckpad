from django.db import models
from helpers.models import TimestampModel
import requests


###
# Models
###

class Address(TimestampModel):
    address = models.CharField(
        max_length=512,
        verbose_name=('Logradouro'),
    )

    number = models.CharField(
        max_length=32,
        verbose_name=('Número'),
    )

    extra = models.CharField(
        max_length=64,
        verbose_name=('Complemento'),
        null=True,
        blank=True,
    )

    neighborhood = models.CharField(
        max_length=128,
        verbose_name=('Bairro'),
    )

    city = models.CharField(
        max_length=128,
        verbose_name=('Cidade'),
    )

    state = models.CharField(
        max_length=2,
        verbose_name=('Estado (UF)'),
    )

    postal_code = models.CharField(
        max_length=16,
        verbose_name=('CEP'),
    )

    latitude = models.CharField(
        max_length=128,
        verbose_name=('Coordenadas Geográficas (lat)'),
        null=True,
        blank=True,
    )
    longitude = models.CharField(
        max_length=128,
        verbose_name=('Coordenadas Geográficas (long)'),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.address}, {self.number}, {self.extra}, {self.neighborhood}, {self.city}, {self.state} - ' \
               f'{self.postal_code} (ID: {self.id})'

    # TODO get google maps api key
    # def save(self, *args, **kwargs):
    #     super(Address, self).save()
    #     GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
    #
    #     params = {
    #         'address': f'{self.address}, {self.number}, {self.extra}, {self.neighborhood}, {self.city}, {self.state}',
    #         'sensor': 'false',
    #         'region': 'brazil'
    #     }
    #
    #     # Do the request and get the response data
    #     req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    #     res = req.json()
    #
    #     # Use the first result
    #     result = res['results'][0]
    #
    #     self.latitude = result['geometry']['location']['lat']
    #     self.longitude = result['geometry']['location']['lng']


class DriverProfile(TimestampModel):
    CARGO_TRUCK_34 = 1
    CARGO_TRUCK_TOCO = 2
    CARGO_TRUCK = 3
    SIMPLE_KART = 4
    EXTENDED_KART = 5

    VEHICLE_TYPE_CHOICES = [
        (CARGO_TRUCK_34, ('Caminhão 3/4')),
        (CARGO_TRUCK_TOCO, ('Caminhão Toco')),
        (CARGO_TRUCK, ('Caminhão Truck')),
        (SIMPLE_KART, ('Carreta Simples')),
        (EXTENDED_KART, ('Carreta eixo estendido')),
    ]

    PRIVATE = 'private'
    RENTAL = 'rental'

    VEHICLE_CATEGORY_CHOICES = [
        (PRIVATE, ('Particular')),
        (RENTAL, ('Aluguel')),
    ]

    MAN = 'man'
    WOMAN = 'woman'
    TRANSGENDER = 'transgender'
    NON_BINARY = 'non_binary'
    PREFER_NOT_TO_RESPOND = 'prefer_not_to_respond'

    GENDER_CHOICES = [
        (MAN, ('Homen')),
        (WOMAN, ('Mulher')),
        (TRANSGENDER, ('Transgenero')),
        (NON_BINARY, ('Não binário')),
        (PREFER_NOT_TO_RESPOND, ('Prefere não responder')),
    ]

    NONE = 'none'
    LESS_THAN_THREE_MONTHS = 'less_than_three_months'
    THREE_TO_SIX_MONTHS = 'three_to_six_months'
    SIX_MONTHS_TO_ONE_YEAR = 'six_months_to_one_year'
    MORE_THAN_ONE_YEAR = 'more_than_one_year'

    EXPERIENCE_TIME_CHOICES = [
        (NONE, ('Nenhum')),
        (LESS_THAN_THREE_MONTHS, ('Menos de três meses')),
        (THREE_TO_SIX_MONTHS, ('De três a seis meses')),
        (SIX_MONTHS_TO_ONE_YEAR, ('De seis meses a um ano')),
        (MORE_THAN_ONE_YEAR, ('Mais de um ano')),
    ]

    # Personal

    name = models.CharField(
        max_length=256,
        verbose_name=('Nome'),
    )

    email = models.EmailField(
        max_length=512,
        verbose_name=('Email'),
        unique=True,
        blank=True,
        null=True,
    )

    document_number = models.CharField(
        max_length=32,
        verbose_name=('CPF'),
        null=True,
        blank=True
    )

    address = models.ForeignKey(
        Address,
        verbose_name=('Endereço'),
        related_name='driver_profiles',
        on_delete=models.CASCADE,
        null=True,
    )

    gender = models.CharField(
        max_length=32,
        verbose_name=('Gênero'),
        choices=GENDER_CHOICES,
        default=PREFER_NOT_TO_RESPOND
    )

    phone_numbers = models.CharField(
        max_length=16,
        verbose_name=('Telefone'),
        blank=True,
        default=''
    )

    rg_document_number = models.CharField(
        max_length=32,
        verbose_name=('RG'),
        blank=True,
        default=''
    )

    birth_date = models.DateField(
        verbose_name=("Data de nascimento"),
        null=True,
        blank=True,
    )

    cnh_document_number = models.CharField(
        max_length=32,
        verbose_name=('CNH'),
        blank=True,
        default=''
    )

    cnh_category = models.CharField(
        max_length=32,
        verbose_name=('Categoría da CNH'),
        blank=True,
        default=''
    )

    cnh_expiration_date = models.DateField(
        verbose_name=("Validade da CNH"),
        null=True,
        blank=True,
    )

    # Vehicle

    vehicle_type = models.IntegerField(
        verbose_name=('Tipo do Veículo'),
        choices=VEHICLE_TYPE_CHOICES,
        default=CARGO_TRUCK
    )

    vehicle_license_plate = models.CharField(
        max_length=16,
        verbose_name=('Placa do Veículo'),
        null=True,
        blank=True,
    )

    vehicle_category = models.CharField(
        max_length=16,
        verbose_name=('Categoria do Veículo'),
        choices=VEHICLE_CATEGORY_CHOICES,
        default=PRIVATE
    )

    own_vehicle = models.BooleanField(
        verbose_name=('Veículo próprio'),
        default=False
    )

    has_experience = models.BooleanField(
        verbose_name=('Já trabalhou com entregas de e-commerce?'),
        default=False,
    )

    experience_time_choices = models.CharField(
        verbose_name=('Tempo de experiência com entregas'),
        choices=EXPERIENCE_TIME_CHOICES,
        default=NONE,
        max_length=32,
    )

    vehicle_brand = models.CharField(
        verbose_name=('Marca do veículo'),
        max_length=32,
        blank=True,
        default='',
    )

    vehicle_model = models.CharField(
        verbose_name=('Modelo do veículo'),
        max_length=64,
        blank=True,
        default='',
    )

    vehicle_color = models.CharField(
        verbose_name=('Cor do veículo'),
        max_length=32,
        blank=True,
        default='',
    )

    class Meta:
        verbose_name = ('Perfil de Motorista')
        verbose_name_plural = ('Perfis de Motoristas')


class DriverReport(TimestampModel):
    EMPTY = 'empty'
    LOADED = 'loaded'

    STATUS_CHOICES = [
        (LOADED, ('Transportando')),
        (EMPTY, ('Vazio')),
    ]

    CEREALS = 'cereals'
    VOLUMES = 'volumes'
    ALIVE = 'alive'
    DANGEROUS = 'dangerous'

    CARGO_TYPE_CHOICES = [
        (CEREALS, ('Grãos')),
        (VOLUMES, ('Volumes')),
        (ALIVE, ('Viva')),
        (DANGEROUS, ('Perigosa')),
    ]

    driver = models.ForeignKey(
        DriverProfile,
        verbose_name=('Motorista'),
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=32,
        verbose_name=('Status'),
        choices=STATUS_CHOICES,
        default=EMPTY,
    )

    status_observation = models.CharField(
        max_length=800,
        verbose_name=('Observações'),
        null=True,
        blank=True,
    )

    origin = models.ForeignKey(
        Address,
        verbose_name=('Endereço de origem'),
        related_name=('address_origin'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    destination = models.ForeignKey(
        Address,
        verbose_name=('Endereço do destino'),
        related_name=('address_destination'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    cargo_type = models.CharField(
        max_length=32,
        verbose_name=('Tipo de carga'),
        choices=CARGO_TYPE_CHOICES,
        default=EMPTY,
    )

    cargo_weight = models.FloatField(
        verbose_name=('Peso da entrega em toneladas'),
        help_text=('0,5 para indicar meia tonelada'),
        default=0.5
    )

    has_cargo_to_return = models.BooleanField(
        verbose_name=('Tem carga para voltar?'),
        default=True
    )

    class Meta:
        verbose_name = ('Status do Caminhão')
        verbose_name_plural = ('Status dos Caminhões')
