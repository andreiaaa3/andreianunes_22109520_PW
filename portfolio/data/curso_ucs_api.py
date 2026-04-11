import requests
import json
import os

schoolYear = '202526'
course = 12

os.makedirs("portfolio/data/json", exist_ok=True)

for language in ['PT']:
    url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'

    payload = {
        'language': language,
        'courseCode': course,
        'schoolYear': schoolYear
    }

    headers = {'content-type': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)
    response_dict = response.json()

    with open(f"portfolio/data/json/ULHT{course}-{language}.json", "w", encoding="utf-8") as f:
        json.dump(response_dict, f, indent=4, ensure_ascii=False)

print("JSON do curso guardado com sucesso.")