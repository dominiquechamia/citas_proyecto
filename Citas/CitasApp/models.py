from django.db import models

class Citados (models.Model):
    autor = models.CharField(max_length=100)
    fuente = models.TextField()
    fecha_citas = models.DateTimeField(auto_now_add=True) 
