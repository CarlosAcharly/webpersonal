# Generated by Django 5.1.5 on 2025-01-30 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enlace')),
            ],
        ),
    ]
