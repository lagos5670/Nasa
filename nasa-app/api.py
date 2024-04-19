import requests
import os

def get_bodies(body_type):
    os.system("clear")  # Limpiar pantalla
    print(f"::: INFORMACIÓN DE {body_type.upper()} :::")
    api_url = f"https://api.le-systeme-solaire.net/rest/bodies/"

    try:
        # Hacer la solicitud a la API con el filtro para el tipo de cuerpo celeste especificado
        response = requests.get(api_url, params={"filter[]": f"bodyType,{body_type}"})
        response.raise_for_status()  # Manejar errores

        data = response.json()

        if "bodies" in data:
             for body in data["bodies"]:
                if body.get("bodyType") == body_type.capitalize():  # Filtrar por tipo de cuerpo celeste
                    print("Nombre en inglés:", body["englishName"])
                    print("Gravedad:", body["gravity"])
                    print("Inclinación:", body["inclination"])
                    print("¿Es un planeta?", body["isPlanet"])
                    print("\n")
        else:
            print(f"No se encontraron datos de {body_type}.")

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud a la API: {e}")

def main(): 
    while True:
        print("#### MENÚ PRINCIPAL ####")
        print("[1]. Mostrar información de Planetas")
        print("[2]. Mostrar información de Lunas")
        print("[3]. Mostrar información de Estrellas")
        print("[3]. Mostrar información de Ateroides")
        print("[4]. Mostrar información de Cometas")
        print("[5]. Salir")

        opt = input("::: Elija una opción: ")

        if opt == '6':
            print("Saliendo del programa...")
            break
        
        if opt == '1':
            get_bodies("Planet")
        elif opt == '2':
            get_bodies("Moon")
        elif opt == '3':
            get_bodies("Star")
        elif opt == '4':
            get_bodies("Comet")
        elif opt == '5':
            get_bodies("Asteroid")    
        else:
            print("Opción no válida. Por favor, elija de nuevo.")

if _name_ == "_main_":
    main()

