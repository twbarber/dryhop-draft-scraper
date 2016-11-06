from flask import Flask
from flask import Response

from TapScraper.taps import corridor
from TapScraper.taps import dryhop

app = Flask(__name__)


@app.route("/dryhop")
def taps_dryhop():
    menu = dryhop.get_menu()
    data = menu.json()
    response = Response(response=data, status=200, mimetype="application/json")
    return response


@app.route("/corridor")
def taps_corridor():
    menu = corridor.get_menu()
    data = menu.json()
    response = Response(response=data, status=200, mimetype="application/json")
    return response


if __name__ == "__main__":
    app.run()