# Generated by Django 5.1.5 on 2025-01-30 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='imagen'),
        ),
    ]
