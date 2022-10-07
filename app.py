from flask import Flask


app = Flask(__name__)

@app.get("/")
def pokemon_list():
    return "Bulbasaur, charmander, pikachu, eevee, diglett, "


@app.get("/bulbasaur")
def bulbasaur_data():
    return "This is Bulbasaur, a generation 1 pokemon who looks like a tiny dinosaur"


@app.get("/charmander")
def charmander_data():
    return "This is Charmander, a generation 1 pokemon who looks like a tiny reptile"


@app.get("/pikachu")
def pikachu_data():
    return "This is Pikachu, a generation 1 pokemon who looks like a tiny rodent"


@app.get("/eevee")
def eevee_data():
    return "This is Eevee, a generation 1 pokemon who looks like a tiny fox"


@app.get("/diglett")
def diglett_data():
    return "This is Diglett, a generation 1 pokemon who looks like a tiny mole"


if __name__ == "__main__":
    app.run()
