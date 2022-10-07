from flask import Flask


app = Flask(__name__)


pokemon_creatures = {
    "bulbasaur": "dinosaur",
    "charmander": "reptile",
    "pikachu": "rodent",
    "eevee": "fox",
    "diglett": "mole"
}

@app.get("/")
def pokemon_list():
    return "Bulbasaur, charmander, pikachu, eevee, diglett, "


@app.get("/<pokemon_name>")
def pokemon_data(pokemon_name):
    creature = pokemon_creatures.get(pokemon_name)
    return f"This is {pokemon_name}, a generation 1 pokemon who looks like a tiny {creature}"


if __name__ == "__main__":
    app.run()
