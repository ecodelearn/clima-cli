import sys
import requests

CONDICOES = {
    "113": "Ensolarado", "116": "Parcialmente nublado", "119": "Nublado",
    "122": "Encoberto", "143": "Névoa", "176": "Chuva leve ocasional",
    "179": "Neve leve ocasional", "182": "Garoa com neve", "185": "Garoa gelada",
    "200": "Trovoada ocasional", "227": "Nevasca leve", "230": "Nevasca",
    "248": "Nevoeiro", "260": "Nevoeiro gelado", "263": "Garoa leve ocasional",
    "266": "Garoa leve", "281": "Garoa gelada", "284": "Garoa gelada intensa",
    "293": "Chuva leve ocasional", "296": "Chuva leve", "299": "Chuva moderada ocasional",
    "302": "Chuva moderada", "305": "Chuva intensa ocasional", "308": "Chuva intensa",
    "311": "Chuva gelada leve", "314": "Chuva gelada moderada", "317": "Mistura leve",
    "320": "Mistura moderada", "323": "Neve leve ocasional", "326": "Neve leve",
    "329": "Neve moderada ocasional", "332": "Neve moderada", "335": "Neve intensa ocasional",
    "338": "Neve intensa", "350": "Granizo", "353": "Chuva leve ocasional",
    "356": "Chuva moderada/intensa", "359": "Chuva torrencial", "362": "Mistura leve ocasional",
    "365": "Mistura moderada/intensa", "368": "Neve leve ocasional", "371": "Neve moderada/intensa",
    "374": "Granizo leve ocasional", "377": "Granizo moderado/intenso",
    "386": "Chuva leve com trovoada", "389": "Chuva moderada/intensa com trovoada",
    "392": "Neve leve com trovoada", "395": "Neve moderada/intensa com trovoada",
}

def consultar_clima(cidade: str) -> None:
    url = f"https://wttr.in/{cidade}?format=j1"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    atual = data["current_condition"][0]

    temp = atual["temp_C"]
    umidade = atual["humidity"]
    vento = atual["windspeedKmph"]
    codigo = atual["weatherCode"]
    condicao = CONDICOES.get(codigo, f"Código {codigo}")

    print(f"Clima em {cidade}:")
    print(f"  Temperatura : {temp}°C")
    print(f"  Umidade     : {umidade}%")
    print(f"  Vento       : {vento} km/h")
    print(f"  Condição    : {condicao}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <cidade>")
        sys.exit(1)
    consultar_clima(sys.argv[1])
