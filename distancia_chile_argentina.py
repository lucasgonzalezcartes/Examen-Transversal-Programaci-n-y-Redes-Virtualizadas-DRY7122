# distancia_chile_argentina.py (usando coordenadas)

import requests

API_KEY = "93d2f644-3d8d-4675-bab6-eb2cff00b5cd"

# Diccionario de ciudades con sus coordenadas
ciudades = {
    "santiago": "-33.4489,-70.6693",
    "valparaiso": "-33.0472,-71.6127",
    "mendoza": "-32.8895,-68.8458",
    "buenos aires": "-34.6037,-58.3816"
}

print("=== Medidor de distancia entre Chile y Argentina (por coordenadas) ===")
print("Ciudades disponibles: santiago, valparaiso, mendoza, buenos aires\n")

while True:
    origen = input("Ciudad de origen (Chile) o 's' para salir: ").lower()
    if origen == 's':
        break

    destino = input("Ciudad de destino (Argentina): ").lower()
    modo = input("Transporte (car, bike, foot): ").lower()

    if origen not in ciudades or destino not in ciudades:
        print("❌ Ciudad no reconocida. Usa una del listado.\n")
        continue

    url = f"https://graphhopper.com/api/1/route?point={ciudades[origen]}&point={ciudades[destino]}&vehicle={modo}&locale=es&key={API_KEY}&instructions=true"

    response = requests.get(url)
    if response.status_code != 200:
        print("❌ Error al consultar la API.")
        print("Código de estado:", response.status_code)
        continue

    data = response.json()
    path = data["paths"][0]
    distancia_m = path["distance"]
    duracion_s = path["time"] / 1000
    instrucciones = path["instructions"]

    print(f"\n🛣️ Distancia: {distancia_m/1000:.2f} km ({distancia_m/1609:.2f} millas)")
    print(f"🕒 Duración: {duracion_s/60:.1f} minutos\n")

    print("📍 Ruta:")
    for paso in instrucciones:
        print(f"- {paso['text']}")
    print("\n")
