from django.db import models

class Profissional(models.Model):
    nome = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    data = models.DateField()
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)

    def __str__(self):
        return self.data
