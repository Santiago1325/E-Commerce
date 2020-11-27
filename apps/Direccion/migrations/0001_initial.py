# Generated by Django 3.1.2 on 2020-11-08 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('ID_Direccion', models.IntegerField(primary_key=True, serialize=False)),
                ('Direccion', models.CharField(max_length=45)),
                ('Identificacion_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cliente.cliente')),
            ],
        ),
    ]