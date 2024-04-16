import requests  
import os 

def get_commet_data(api_key):
    print("::: COMENT INFORMATIONS :::")
    api_url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try: 
        response  = requests.get(api_url)
        response.raise_for_status()
        data = response.json()


        os.system('clear')
        #Show:
        #comet name 
        print(f'Comet name: {data['name']}')
        #Absolute magnitud 
        print(f'Absolute magnitud: {data['absolute_magnitude_h']}')
        #Estimate diameter max (KM)
        print(f'Diameter max: {data['estimated_diameter']['kilometers']['estimated_diameter_max']}')
        #Estimate diameter min (KM)
        print(f'Diameter min: {data['estimated_diameter']['kilometers']['estimated_diameter_min']}')
        #Estimate diameter max (FT)
        print(f'Diameter max: {data['estimated_diameter']['feet']['estimated_diameter_max']}')
        #Estimate diameter min (FT)
        print(f'Diameter min: {data['estimated_diameter']['feet']['estimated_diameter_min']}')
        #obital_data
        for approach in data['close_approach_data']:
            date = approach["close_approach_date"]
            velocity_km_per_sec = approach["relative_velocity"]["kilometers_per_second"]
            miss_distance_km = approach["miss_distance"]["kilometers"]
            orbiting_body = approach["orbiting_body"]
            print("\nFecha de aproximación cercana:", date)
            print("Velocidad relativa (km/s):", velocity_km_per_sec)
            print("Distancia de fallo (km):", miss_distance_km)
            print("Cuerpo en órbita:", orbiting_body)
            
    except requests.exceptions.RequestException as e:
        print(f"Api error {e}") #==> print("API error",e)
    
 

#Main
api_key_nasa = 'J309LT6CHHVtDjMNeEhJMY6Oj4hByjFk4FxBeJaf'
get_commet_data(api_key_nasa)