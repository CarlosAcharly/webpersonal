from django.db import models

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=50, verbose_name='Nombre')
    description=models.TextField(verbose_name="Descripcion")
    image=models.ImageField(upload_to='images', verbose_name='imagen', null=True, blank=True)
    url= models.URLField(verbose_name='Enlace', null=True, blank=True)

def __str__(self):
    return self.name

class Meta:
    verbose_name='proyecto'
    ordering=['id']
