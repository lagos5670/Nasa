import requests

def get_asteroid_data(api_key):
    print("::: ASTEROID INFORMATION :::")
    api_url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        # Acceder al nombre del asteroide
        name = data["name"]
        print("Nombre del asteroide:", name)

        # Acceder al diámetro estimado máximo en kilómetros
        diameter_max_km = data["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
        print("Diámetro estimado máximo (km):", diameter_max_km)

        # Acceder al diámetro estimado mínimo en pies
        diameter_min_ft = data["estimated_diameter"]["feet"]["estimated_diameter_min"]
        print("Diámetro estimado mínimo (ft):", diameter_min_ft)

        # Acceder al estado de potencialmente peligroso del asteroide
        is_potentially_hazardous = data["is_potentially_hazardous_asteroid"]
        print("Potencialmente peligroso:", is_potentially_hazardous)

        # Acceder a los datos de aproximación cercana del asteroide
        close_approach_data = data["close_approach_data"]
        print("\n::: CLOSE APPROACH DATA :::")
        for approach in close_approach_data:
            date = approach["close_approach_date"]
            velocity_km_per_sec = approach["relative_velocity"]["kilometers_per_second"]
            miss_distance_km = approach["miss_distance"]["kilometers"]
            orbiting_body = approach["orbiting_body"]
            print("\nFecha de aproximación cercana:", date)
            print("Velocidad relativa (km/s):", velocity_km_per_sec)
            print("Distancia de fallo (km):", miss_distance_km)
            print("Cuerpo en órbita:", orbiting_body)

    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")

# Main
api_key_nasa = 'mx8FwuOdnOCop3yLgiaSOi1ozitVAUcWDDu8JXaT'
get_asteroid_data(api_key_nasa)