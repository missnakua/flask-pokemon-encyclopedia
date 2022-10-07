import requests

def get_pokemon_by_name(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    pokemon = response.json()
    return pokemon
