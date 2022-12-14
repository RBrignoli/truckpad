# Generated by Django 4.1 on 2022-08-23 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=512, verbose_name='Logradouro')),
                ('number', models.CharField(max_length=32, verbose_name='Número')),
                ('extra', models.CharField(blank=True, max_length=64, null=True, verbose_name='Complemento')),
                ('neighborhood', models.CharField(max_length=128, verbose_name='Bairro')),
                ('city', models.CharField(max_length=128, verbose_name='Cidade')),
                ('state', models.CharField(max_length=2, verbose_name='Estado (UF)')),
                ('postal_code', models.CharField(max_length=16, verbose_name='CEP')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=512, null=True, unique=True, verbose_name='Email')),
                ('document_number', models.CharField(blank=True, max_length=32, null=True, verbose_name='CPF')),
                ('phone_numbers', models.CharField(blank=True, default='', max_length=16, verbose_name='Telefone')),
                ('rg_document_number', models.CharField(blank=True, default='', max_length=32, verbose_name='RG')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('cnh_document_number', models.CharField(blank=True, default='', max_length=32, verbose_name='CNH')),
                ('cnh_category', models.CharField(blank=True, default='', max_length=32, verbose_name='Categoría da CNH')),
                ('cnh_expiration_date', models.DateField(blank=True, null=True, verbose_name='Validade da CNH')),
                ('vehicle_type', models.IntegerField(choices=[(1, 'Caminhão 3/4'), (2, 'Caminhão Toco'), (3, 'Caminhão Truck'), (4, 'Carreta Simples'), (5, 'Carreta eixo estendido')], default=3, verbose_name='Tipo do Veículo')),
                ('vehicle_license_plate', models.CharField(blank=True, max_length=16, null=True, verbose_name='Placa do Veículo')),
                ('vehicle_category', models.CharField(choices=[('private', 'Particular'), ('rental', 'Aluguel')], default='private', max_length=16, verbose_name='Categoria do Veículo')),
                ('own_vehicle', models.BooleanField(default=False, verbose_name='Veículo próprio')),
                ('has_experience', models.BooleanField(default=False, verbose_name='Já trabalhou com entregas de e-commerce?')),
                ('experience_time_choices', models.CharField(choices=[('none', 'Nenhum'), ('less_than_three_months', 'Menos de três meses'), ('three_to_six_months', 'De três a seis meses'), ('six_months_to_one_year', 'De seis meses a um ano'), ('more_than_one_year', 'Mais de um ano')], default='none', max_length=32, verbose_name='Tempo de experiência com entregas')),
                ('vehicle_brand', models.CharField(blank=True, default='', max_length=32, verbose_name='Marca do veículo')),
                ('vehicle_model', models.CharField(blank=True, default='', max_length=64, verbose_name='Modelo do veículo')),
                ('vehicle_color', models.CharField(blank=True, default='', max_length=32, verbose_name='Cor do veículo')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_profiles', to='operations.address', verbose_name='Endereço')),
            ],
            options={
                'verbose_name': 'Perfil de Motorista',
                'verbose_name_plural': 'Perfis de Motoristas',
            },
        ),
        migrations.CreateModel(
            name='DriverReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('loaded', 'Transportando'), ('empty', 'Vazio')], default='empty', max_length=32, verbose_name='Status')),
                ('status_observation', models.CharField(blank=True, max_length=800, null=True, verbose_name='Observações')),
                ('cargo_type', models.CharField(choices=[('cereals', 'Grãos'), ('volumes', 'Volumes'), ('alive', 'Viva'), ('dangerous', 'Perigosa')], default='empty', max_length=32, verbose_name='Tipo de carga')),
                ('cargo_weight', models.FloatField(default=0.5, help_text='0,5 para indicar meia tonelada', verbose_name='Peso da entrega em toneladas')),
                ('destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address_destination', to='operations.address', verbose_name='Endereço do destino')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.driverprofile', verbose_name='Motorista')),
                ('origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address_origin', to='operations.address', verbose_name='Endereço de origem')),
            ],
            options={
                'verbose_name': 'Status do Caminhão',
                'verbose_name_plural': 'Status dos Caminhões',
            },
        ),
    ]
