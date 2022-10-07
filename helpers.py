import requests
import random


FIRST_GENERATION_POKEMON_IDS = range(1, 152)


def get_pokemon_by_name(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    pokemon = response.json()
    return pokemon


def get_pokemon_by_id(pokemon_id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    pokemon = response.json()
    return pokemon


def get_random_pokemon_list():
    random_pokemon_ids = random.sample(FIRST_GENERATION_POKEMON_IDS, 5)
    random_pokemon = [get_pokemon_by_id(pokemon_id) for pokemon_id in random_pokemon_ids]
    return random_pokemon