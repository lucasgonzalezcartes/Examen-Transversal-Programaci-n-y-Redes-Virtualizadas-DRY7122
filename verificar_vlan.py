# verificar_vlan.py

def verificar_vlan(numero):
    if 1 <= numero <= 1005:
        return "VLAN de rango NORMAL"
    elif 1006 <= numero <= 4094:
        return "VLAN de rango EXTENDIDO"
    else:
        return "Número de VLAN fuera del rango válido (1-4094)"

while True:
    entrada = input("Ingrese el número de VLAN (o escriba 's' para salir): ")

    if entrada.lower() == 's':
        print("Saliendo del programa...")
        break

    try:
        vlan = int(entrada)
        resultado = verificar_vlan(vlan)
        print(f"Resultado: {resultado}\n")
    except ValueError:
        print("⚠️ Ingrese un número válido.\n")
