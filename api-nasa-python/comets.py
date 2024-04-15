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
        print(f'Diameter max: {data['kilometers','estimated_diameter_max']}')
        #Estimate diameter min (KM)
        print(f'Diameter min: {data['kilometers','estimated_diameter_max']}')
        #Estimate diameter max (FT)
        print(f'Diameter max: {data['kilometers','estimated_diameter_max']}')
        #Estimate diameter min (FT)
        #obital_data
            #last_observation_date 

    except requests.exceptions.RequestException as e:
        print(f"Api error {e}") #==> print("API error",e)
    
 

#Main
api_key_nasa = 'J309LT6CHHVtDjMNeEhJMY6Oj4hByjFk4FxBeJaf'
get_commet_data(api_key_nasa)