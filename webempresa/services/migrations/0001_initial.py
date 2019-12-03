# Generated by Django 2.2.7 on 2019-11-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(upload_to='services')),
                ('creado', models.DateField(auto_now_add=True)),
                ('actualizado', models.DateField(auto_now=True)),
            ],
        ),
    ]