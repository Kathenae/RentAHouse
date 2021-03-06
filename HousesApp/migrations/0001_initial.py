# Generated by Django 3.1.6 on 2021-06-30 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_registrada', models.DateField(default=django.utils.timezone.now)),
                ('mostrar_na_lista', models.BooleanField(default=True)),
                ('nome_do_proprietario', models.CharField(max_length=30)),
                ('sobrenome_do_proprietario', models.CharField(max_length=30)),
                ('contacto_principal', models.CharField(max_length=12)),
                ('contacto_secúndario', models.CharField(blank=True, max_length=12, null=True)),
                ('preço', models.FloatField(default=0.0)),
                ('meses_adiantados', models.IntegerField(default=1)),
                ('cidade', models.CharField(choices=[('Tete', 'Tete'), ('Maputo', 'Maputo'), ('Gaza', 'Gaza'), ('Inhambane', 'Inhambane'), ('Manica', 'Manica'), ('Sofala', 'Sofala'), ('Zambezia', 'Zambezia'), ('Nampula', 'Nampula'), ('Cabo Delgado', 'Cabo Delgado'), ('Niassa', 'Niassa')], max_length=30)),
                ('distrito', models.CharField(blank=True, max_length=30, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('numero_de_divisoes', models.IntegerField()),
                ('mobiliada', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=6)),
                ('vedada', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=6)),
                ('create_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HouseListingPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriçao', models.CharField(max_length=20)),
                ('picture', models.ImageField(upload_to='images/houses')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='HousesApp.houselisting')),
            ],
        ),
    ]
