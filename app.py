from flask import Flask, render_template
from helpers import get_pokemon_by_name, get_random_pokemon_list


app = Flask(__name__)


@app.get("/")
def pokemon_list():
    random_pokemon = get_random_pokemon_list()
    return render_template("pokemon_list.html", random_pokemon=random_pokemon)


@app.get("/<pokemon_name>")
def pokemon_data(pokemon_name):
    pokemon = get_pokemon_by_name(pokemon_name)
    return render_template("pokemon_data.html", pokemon=pokemon)


if __name__ == "__main__":
    app.run()