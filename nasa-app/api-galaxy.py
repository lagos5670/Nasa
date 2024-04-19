#para usar un api en python usamos al siguiente biblioteca 
import requests 
import os 

def get_data(body):
    os.system("Clear") #limpiar pantalla 
    print(":: SOLAR SYSTEM INFORMATION ::")
    api_url = "https://api.le-systeme-solaire.net/rest/bodies/"


    try:
        #Request to Api 
        response = requests.get(api_url, params={'filter[]':f'bodyType,{body}'})
        response.raise_for_status() #genero un error

        data = response.json()#Almacena los datos de la Api en la variablle data 

        if 'bodies' in data:
                for planeta in data['bodies']:
                    if planeta.get('bodyType')== body.capitalize():
                        print(f'Nombre planeta: {planeta['englishName']}')
                        print(f'Gravedad: {planeta['gravity']}')
                        print(f'Inclinación: {planeta['inclination']}')
                        print(f'Es un planeta: {planeta['isPlanet']}')
        else:
            print(f'Nose encontraron datos de: {body}')

    except requests.exceptions.RequestException as e:
        print(f"Api error {e}") #==> print("API error",e)


    
def menu():
    while True:
        print("### MAIN MENU ###")
        print("[1]. Planetas")
        print("[2]. Moons")
        print("[3]. Stars")
        print("[4]. Asteroid")
        print("[5]. Complets")
        print("[6]. Exit")
        opt = input("::: Press any option ::: ")

        if opt == '6':
           print('Usted salio del programa')
           break

        if opt == '1':
           get_data('planet')

        elif opt == '2':
            get_data('Moon')

        elif opt == '3':
            get_data('Star')

        elif opt == '4':
           get_data('Comet')

        elif opt == '5':
           get_data('Asteroid')
        
        else:
            print("La Opcion ingresada es incorrecta")
        
       
#Main
menu()



   

 




