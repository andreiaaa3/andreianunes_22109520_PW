from django.db import models


class Licenciatura(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=20)
    descricao = models.TextField(blank=True)
    duracao = models.PositiveIntegerField(blank=True, null=True)
    ects = models.PositiveIntegerField(blank=True, null=True)
    imagem = models.ImageField(upload_to='licenciaturas/', blank=True, null=True)

    def __str__(self):
        return f"{self.sigla} - {self.nome}"


class Docente(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    pagina_pessoal = models.URLField(blank=True)
    foto = models.ImageField(upload_to='docentes/', blank=True, null=True)

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=150)
    codigo = models.CharField(max_length=30)
    ano = models.PositiveSmallIntegerField(blank=True, null=True)
    semestre = models.PositiveSmallIntegerField(blank=True, null=True)
    ects = models.PositiveSmallIntegerField(blank=True, null=True)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name="ucs")
    docentes = models.ManyToManyField(Docente, related_name="ucs", blank=True)

    def __str__(self):
        return self.nome


class CategoriaTecnologia(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    website = models.URLField(blank=True)
    nivel_preferencia = models.PositiveSmallIntegerField(default=3)
    categoria = models.ForeignKey(
        CategoriaTecnologia,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tecnologias"
    )

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField(blank=True)
    git_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name="projetos")
    tecnologias = models.ManyToManyField(Tecnologia, related_name="projetos", blank=True)

    def __str__(self):
        return self.titulo


class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=120)
    ano = models.PositiveIntegerField(blank=True, null=True)
    resumo = models.TextField(blank=True)
    area = models.CharField(max_length=120, blank=True)
    url = models.URLField(blank=True)
    nivel_interesse = models.PositiveSmallIntegerField(default=3)
    destaque = models.BooleanField(default=False)
    tecnologias = models.ManyToManyField(Tecnologia, related_name="tfcs", blank=True)

    def __str__(self):
        return self.titulo


class Competencia(models.Model):
    CATEGORIAS = [
        ("tecnica", "Técnica"),
        ("soft", "Soft Skill"),
        ("lingua", "Língua"),
        ("outra", "Outra"),
    ]

    NIVEIS = [
        (1, "Inicial"),
        (2, "Básico"),
        (3, "Intermédio"),
        (4, "Bom"),
        (5, "Muito Bom"),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default="tecnica")
    nivel = models.PositiveSmallIntegerField(choices=NIVEIS, default=3)
    projetos = models.ManyToManyField(Projeto, related_name="competencias", blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name="competencias", blank=True)

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    TIPOS = [
        ("academica", "Académica"),
        ("curso", "Curso"),
        ("certificacao", "Certificação"),
        ("workshop", "Workshop"),
        ("outra", "Outra"),
    ]

    titulo = models.CharField(max_length=150)
    entidade = models.CharField(max_length=120)
    tipo = models.CharField(max_length=20, choices=TIPOS, default="curso")
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    duracao = models.CharField(max_length=60, blank=True)
    certificado_url = models.URLField(blank=True)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='formacoes/', blank=True, null=True)
    competencias = models.ManyToManyField(Competencia, related_name="formacoes", blank=True)

    def __str__(self):
        return self.titulo


class MakingOf(models.Model):
    ENTIDADES = [
        ("licenciatura", "Licenciatura"),
        ("uc", "Unidade Curricular"),
        ("docente", "Docente"),
        ("projeto", "Projeto"),
        ("tecnologia", "Tecnologia"),
        ("tfc", "TFC"),
        ("competencia", "Competência"),
        ("formacao", "Formação"),
        ("geral", "Geral"),
        ]

    titulo = models.CharField(max_length=150)
    data = models.DateField()
    entidade_alvo = models.CharField(max_length=20, choices=ENTIDADES, default="geral")
    objeto_nome = models.CharField(max_length=150, blank=True)
    descricao_processo = models.TextField()
    decisao_tomada = models.TextField(blank=True)
    justificacao = models.TextField(blank=True)
    erro_encontrado = models.TextField(blank=True)
    correcao = models.TextField(blank=True)
    foto = models.ImageField(upload_to='makingof/', blank=True, null=True)
    usei_ai = models.BooleanField(default=False)
    como_usei_ai = models.TextField(blank=True)
    
    def __str__(self):
        return self.titulo