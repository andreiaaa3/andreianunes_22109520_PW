import json
from portfolio.models import Licenciatura, UnidadeCurricular

with open("portfolio/data/json/ULHT12-PT.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

licenciatura, created = Licenciatura.objects.get_or_create(
    sigla="LIG",
    defaults={
        "nome": "Licenciatura em Informática de Gestão",
        "descricao": "Curso na área de informática e gestão.",
        "duracao": 3,
        "ects": 180,
    }
)

contador = 0

for uc in dados["courseFlatPlan"]:
    nome = uc.get("curricularUnitName", "")
    codigo = uc.get("curricularIUnitReadableCode", "")
    ano = uc.get("yearNumber") or 0
    semestre = uc.get("semesterNumber") or 0
    ects = uc.get("credits") or 0

    UnidadeCurricular.objects.get_or_create(
        codigo=codigo,
        defaults={
            "nome": nome,
            "ano": ano,
            "semestre": semestre,
            "ects": ects,
            "descricao": "",
            "licenciatura": licenciatura,
        }
    )

    contador += 1

print(f"{contador} UCs importadas com sucesso.")