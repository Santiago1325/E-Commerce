# Generated by Django 3.1.2 on 2020-11-08 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cliente', '0001_initial'),
        ('Domiciliario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito_de_Compra',
            fields=[
                ('ID_Carrito', models.IntegerField(primary_key=True, serialize=False)),
                ('ID_Domiciliario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Domiciliario.domiciliario')),
                ('Identificacion_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cliente.cliente')),
            ],
        ),
    ]