from django.db import models

    
class Escola(models.Model):
    nome = models.CharField(max_length=100)
    #morada = models.CharField(max_length=100)

    
    def __str__(self):
        return f'{self.nome}: {self.morada}'
    
class Turma(models.Model):
    ano = models.CharField(max_length=100)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name = "turmas") 

    def __str__(self):
        return f'{self.ano}: {self.escola}'  

    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name = "alunos") 
    #escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="alunos")

    def __str__(self):
        return f'{self.nome} {self.idade}'
    
    
class Professor(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name = "professores") 
   # escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name = "professores") 

    class Meta:
        verbose_name = "professor"
        verbose_name_plural = "professores"

    def __str__(self):
        return f'{self.nome} {self.turma}'


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='cursos')
    aluno = models.ManyToManyField(Aluno, related_name='cursos')
    escola = models.ForeignKey(Escola, on_delete = models.CASCADE, related_name = "cursos")

    def __str__(self):
        return self.nome
