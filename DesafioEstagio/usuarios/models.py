from django.db import models

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    senha = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    idDiscord = models.CharField(max_length=15, null=False, blank=False)
    
    def __str__(self):
        return self.nome