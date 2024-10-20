# Generated by Django 5.1.2 on 2024-10-19 16:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10, unique=True)),
                ('modelo', models.CharField(max_length=50)),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnh', models.CharField(max_length=12)),
                ('categoria', models.CharField(max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField(blank=True, null=True)),
                ('localizacao_inicio', models.CharField(max_length=100)),
                ('localizacao_fim', models.CharField(blank=True, max_length=100, null=True)),
                ('motorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frota.motorista')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frota.veiculo')),
            ],
        ),
    ]