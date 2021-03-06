# Generated by Django 2.2.7 on 2019-11-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Key', models.SlugField(max_length=100, unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True, null=True)),
                ('creado', models.DateField(auto_now_add=True)),
                ('actualizado', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]
