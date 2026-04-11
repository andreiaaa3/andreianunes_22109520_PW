import json
from portfolio.models import TFC, Tecnologia

with open("portfolio/data/tfcs_2025.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

contador = 0

for item in dados:
    titulo = item.get("titulo") or ""
    autores = item.get("autores") or []
    autor = autores[0] if autores else "Desconhecido"
    ano = item.get("ano") or 0
    resumo = item.get("resumo") or ""
    areas = item.get("areas") or []
    area = areas[0] if areas else ""
    url = item.get("link_pdf") or ""

    tfc = TFC.objects.create(
        titulo=titulo,
        autor=autor,
        ano=ano,
        resumo=resumo,
        area=area,
        url=url,
    )

    for nome_tecnologia in item.get("tecnologias_usadas") or []:
        tecnologia, created = Tecnologia.objects.get_or_create(nome=nome_tecnologia)
        tfc.tecnologias.add(tecnologia)

    contador += 1

print(f"{contador} TFCs importados com sucesso!")