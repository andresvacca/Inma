from django.db import models

class Articulos(models.Model):
    nombre = models.CharField(max_length=150)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_compra = models.DecimalField(10, 2)
    stock = models.IntegerField(max_length=100)
    
