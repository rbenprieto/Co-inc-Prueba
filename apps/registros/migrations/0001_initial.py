# Generated by Django 4.0.6 on 2022-09-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuariosInscritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre completo')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('ciudad', models.CharField(max_length=255, verbose_name='Ciudad')),
                ('fecha_inscripcion', models.DateField(auto_now=True)),
            ],
        ),
    ]