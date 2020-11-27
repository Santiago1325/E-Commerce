# Generated by Django 3.1.2 on 2020-11-08 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Desarrollador', '0001_initial'),
        ('Clasificacion_Edad', '0001_initial'),
        ('Franquicia', '0001_initial'),
        ('Plataforma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('Codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('Multijugador', models.BooleanField()),
                ('Costo', models.IntegerField()),
                ('Nombre', models.CharField(max_length=45)),
                ('ID_Admin', models.IntegerField()),
                ('ID_Clasificacion_de_edad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clasificacion_Edad.clasificacion_edad')),
                ('ID_Desarrollador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Desarrollador.desarrollador')),
                ('ID_Franquicia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Franquicia.franquicia')),
                ('ID_Plataforma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plataforma.plataforma')),
            ],
        ),
    ]