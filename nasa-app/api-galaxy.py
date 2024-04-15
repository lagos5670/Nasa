#para usar un api en python usamos al siguiente biblioteca 
import requests 
import os 

def get_data():
    os.system("Clear") #limpiar pantalla 
    print(":: SOLAR SYSTEM INFORMATION ::")
    api_url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"


    try:
        #Request to Api 
        response = requests.get(api_url)
        response.raise_for_status() #genero un error

        data = response.json()
        print("### MAIN MENU ###")
        print("[1]. Planetas")
        print("[2]. Moons")
        print("[3]. Stars")
        print("[4]. Asteroid")
        print("[5]. Complets")
        print("[6]. Exit")
        





        return data

    except requests.exceptions.RequestException as e:
        print(f"Api error {e}")


 

#Main
info = get_data()
print(info)

