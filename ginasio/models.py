from django.db import models

class Ginasio(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'
    
class PersonalTrainer(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    ginasio = models.ForeignKey(Ginasio, on_delete=models.CASCADE, related_name = "personaltrainers")  

    def __str__(self):
        return f'{self.nome}: {self.ginasio}'

class Membro(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    nome = models.CharField(max_length=100)
    personalTrainer = models.ForeignKey(PersonalTrainer, on_delete = models.CASCADE, related_name= "membros")
    #ginasio = models.ForeignKey(Ginasio, on_delete=models.CASCADE, related_name = "membros")
    #sessoes = models.ManyToManyField(Sessao, related_name= "membros")  

    def __str__(self):
        return f'{self.nome}: {self.idade} anos, {self.sessoes}'

class Sessao(models.Model):
    tipo = models.CharField(max_length=100)
    dataHora = models.DateTimeField()
    membros = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name = "sessoes")  
    personaltrainer = models.ForeignKey(PersonalTrainer, on_delete=models.CASCADE, related_name = "sessoes")  
    ginasio = models.ForeignKey(Ginasio, on_delete=models.CASCADE, related_name = "sessoes")  

    def __str__(self):
        return f'{self.tipo}: {self.dataHora} {self.personaltrainer}'
