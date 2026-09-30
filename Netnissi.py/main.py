
# ==========================================================
# NetNissi - Analizador básico de conexiones de red
# Autor: Josué
# Área: Sistema de Telecomunicaciones
# ==========================================================



def analizar_conexion(latencia, perdida, descarga, subida):
    problemas = []
    recomendaciones = []

    if latencia > 100:
        problemas.append("Latencia elevada")
        recomendaciones.append("Verifique la distancia al router o al servidor.")

    if perdida > 2:
        problemas.append("Perdida de paquetes")
        recomendaciones.append("Revise la conexion de red.")

    if descarga < 10:
        problemas.append("Velocidad de descarga baja")
        recomendaciones.append("Compruebe cuantos dispositivos utilizan la red.")

    if subida < 3:
        problemas.append("Velocidad de subida baja")
        recomendaciones.append("Revise la configuracion del router.")

    if len(problemas) == 0:
        estado = "ESTABLE"
    elif len(problemas) <= 2:
        estado = "PRESENTA POSIBLES PROBLEMAS"
    else:
        estado = "INESTABLE"

    return estado, problemas, recomendaciones


def main():
    print("=" * 50)
    print("                 NETNISSI")
    print("       Analizador de conexiones de red")
    print("=" * 50)

    try:
        latencia = float(input("Latencia (ms): "))
        perdida = float(input("Perdida de paquetes (%): "))
        descarga = float(input("Velocidad de descarga (Mbps): "))
        subida = float(input("Velocidad de subida (Mbps): "))

        if latencia < 0 or perdida < 0 or descarga < 0 or subida < 0:
            print("Error: los valores no pueden ser negativos.")
            return

        print("\nAnalizando conexion...")

        estado, problemas, recomendaciones = analizar_conexion(
            latencia,
            perdida,
            descarga,
            subida
        )

        print("\n" + "=" * 50)
        print("RESULTADO DEL ANALISIS")
        print("=" * 50)

        print("Estado:", estado)

        if problemas:
            print("\nProblemas detectados:")
            for problema in problemas:
                print("-", problema)
        else:
            print("\nNo se detectaron problemas importantes.")

        if recomendaciones:
            print("\nRecomendaciones:")
            for recomendacion in recomendaciones:
                print("-", recomendacion)

        print("=" * 50)

    except ValueError:
        print("Error: debes introducir solamente numeros.")


if __name__ == "__main__":
    main()

