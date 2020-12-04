# Generated by Django 3.1.2 on 2020-12-03 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Carrito_de_Compra', '0001_initial'),
        ('Videojuego', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('ID_Factura', models.IntegerField(primary_key=True, serialize=False)),
                ('Valor_Total', models.IntegerField()),
                ('Metodo_De_Pago', models.CharField(max_length=45)),
                ('Codigo_Video_Juegos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Videojuego.videojuego')),
                ('ID_Carrito_Carrito_De_Compras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Carrito_de_Compra.carrito_de_compra')),
            ],
        ),
    ]
