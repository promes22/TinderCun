def registrar_personas():
    #Datos requeridos de un usuario
    individuo={}
    print ("\n---Registro para nuevos usuarioas---")
    individuo [nombre]= input("¿como te llamas?")
    individuo [edad]= int(input("¿Cuantos años tienes?"))
    individuo [ciudad]= input("¿En que ciudad te encuentras?")
    individuo [buscar]= input("¿Que genero estas buscando (M/F otro)").strip().lower()
    individuo [genero]= input("¿ual es tu genero?(M/F Otros)").strip().lower()
    individuo [Edadminima]= int(input("¿Edad minima de la persona de tu vida?"))
    individuo [Edadmaxima]= int(input("¿Edad maxina de la persona de tu vida?"))

    integrantes= input("ingresa tus intereses personales separados por comas (ej. viajar,correr,comer,):")
    individuo["Intereses"] = [i.strip().lower() for i in intereses_str.split(",")]
    individuo["DistanciaMax"]= int(input("distancia maxima que estas dispuestos aceptar (en km):"))

    print(f"\n¡hola {individuo[nombre]}Tu registro a sido exitoso")
    return individuo

def mostrar_personas(personas):
    if not personas:
        print("\nNo hay personas registradas todavía.")
        return

    print("\n--- PERSONAS REGISTRADAS EN EL SISTEMA ---")
    
    for idx, persona in enumerate(personas):
        print(f"\n[{idx}] Nombre: {persona['Nombre']}, Edad: {persona['Edad']}, Ciudad: {persona['Ciudad']}")
        print(f"    Busca: {persona['Busca']} | Rango de edad: {persona['EdadMin']}-{persona['EdadMax']} años")
        print(f"    Intereses: {', '.join(persona['Intereses'])}")

def calcular_distancia_simulada(ciudad1, ciudad2):
    if ciudad1.strip().lower() == ciudad2.strip().lower():
        return 5 
    else:
        return 50
def evaluar_compatibilidad(p1, p2):
    edad_valida = (p2["Edad"] >= p1["EdadMin"] and p2["Edad"] <= p1["EdadMax"])
    preferencia_valida = (p1["Genero"] == p2["Busca"] and p2["Genero"] == p1["Busca"])
    distancia = calcular_distancia_simulada(p1["Ciudad"], p2["Ciudad"])
    distancia_valida = (distancia <= p1["DistanciaMax"] and distancia <= p2["DistanciaMax"])
    
    if not (edad_valida and preferencia_valida and distancia_valida):
        return 0, edad_valida, preferencia_valida, distancia_valida, []

    intereses_comunes = list(set(p1["Intereses"]) & set(p2["Intereses"]))

    puntos_intereses = min(len(intereses_comunes) * 15, 50)
    porcentaje = 50 + puntos_intereses

    return porcentaje, edad_valida, preferencia_valida, distancia_valida, intereses_comunes

def buscar_coincidencias_usuario(personas):
    if len(personas) < 2:
        print("\nSe necesitan al menos 2 personas registradas para buscar coincidencias.")
        return

    mostrar_personas(personas)
    idx = int(input("\nIngresa el número [índice] de la persona para la que deseas buscar pareja: "))

    if idx < 0 or idx >= len(personas):
        print("Índice no válido.")
        return

    persona_principal = personas[idx]
    print(f"\nBuscando el Top de coincidencias para: {persona_principal['Nombre']}...")


    for i, candidato in enumerate(personas):
        if i == idx:
            continue
        porc, e_val, pref_val, dist_val, in_com = evaluar_compatibilidad(persona_principal, candidato)
        
        resultados = []
        
        resultados.append({
            "Candidato": candidato,
            "Porcentaje": porc,
            "EdadValida": e_val,
            "PrefValida": pref_val,
            "DistValida": dist_val,
            "InteresesComunes": in_com
        })


        resultados = sorted(resultados, key=lambda x: x["Porcentaje"], reverse=True)
    
    print(f"\n========================================")
    print(f" TOP DE COINCIDENCIAS PARA: {persona_principal['Nombre']}")
    print(f"========================================")

    for r in resultados[:3]: 
        c = r["Candidato"]
        print(f"\nNombre: {c['Nombre']}")
        print(f"Compatibilidad: {r['Porcentaje']}%")
        print(f"Intereses en común: {', '.join(r['InteresesComunes']) if r['InteresesComunes'] else 'Ninguno'}")
        print(f"Edad compatible: {'Sí' if r['EdadValida'] else 'No'}")
        print(f"Preferencias compatibles: {'Sí' if r['PrefValida'] else 'No'}")
        print(f"Distancia compatible: {'Sí' if r['DistValida'] else 'No'}")
        print("-" * 40)

def main():
    lista_personas = []

    lista_personas.append({
        "Nombre": "Carlos", "Edad": 20, "Ciudad": "Bogota", "Genero": "m", "Busca": "f",
        "EdadMin": 18, "EdadMax": 25, "Intereses": ["musica", "viajar", "videojuegos"], "DistanciaMax": 30
    })
    lista_personas.append({
        "Nombre": "Laura", "Edad": 19, "Ciudad": "Bogota", "Genero": "f", "Busca": "m",
        "EdadMin": 18, "EdadMax": 23, "Intereses": ["viajar", "musica", "cine"], "DistanciaMax": 25
    })

    while True:
        print("\n===============================")
        print("     MENÚ PRINCIPAL - TINDER   ")
        print("===============================")
        print("1. Registrar nueva persona")
        print("2. Mostrar personas registradas")
        print("3. Buscar Top 3 de coincidencias para alguien")
        print("4. Salir")


        opcion = input("\nElige una opción (1-4): ")
        
        if opcion == "1":
            nueva = registrar_persona()
            lista_personas.append(nueva) # Agregamos el nuevo diccionario a nuestra lista principal
        elif opcion == "2":
            mostrar_personas(lista_personas)
        elif opcion == "3":
            buscar_coincidencias_usuario(lista_personas)
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema de citas! Saliendo...")
            break # Rompe el ciclo while y termina el programa
        else:
            print("\nOpción inválida. Por favor, elige un número del 1 al 4.")

if __name__ == "__main__":
    main()


        


