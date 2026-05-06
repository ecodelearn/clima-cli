import sys
import requests

def consultar_clima(cidade: str) -> None:
    url = f"https://wttr.in/{cidade}?format=j1"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    atual = data["current_condition"][0]
    temp = atual["temp_C"]
    print(f"Clima em {cidade}: {temp}°C")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <cidade>")
        sys.exit(1)
    consultar_clima(sys.argv[1])
