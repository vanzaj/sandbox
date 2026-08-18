import marimo

__generated_with = "0.24.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # RSE course practice

    [Research Software Engineering with Python](https://alan-turing-institute.github.io/rse-course/html/index.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1.9 Exercise Maze Model

    Work with a partner to design a data structure to represent a **maze** using dictionaries and lists.
      - Each place in the maze has a name, which is a string.
      - Each place in the maze has one or more **people** currently standing at it, by name.
      - Each place in the maze has a maximum capacity of people that can fit in it.
      - From each place in the maze, you can go from that place to a few other places, using a direction like ‘up’, ‘north’, or ‘sideways’

    Create an example instance, in a notebook, of a simple structure for your maze:
      - The front room can hold 2 people. James is currently there. You can go outside to the garden, or upstairs to the bedroom, or north to the kitchen.
      - From the kitchen, you can go south to the front room. It fits 1 person.
      - From the garden you can go inside to front room. It fits 3 people. Sue is currently there.
      - From the bedroom, you can go downstairs to the front room. You can also jump out of the window to the garden. It fits 2 people.

    Make sure that your model:
      - Allows empty rooms
      - Allows you to jump out of the upstairs window, but not to fly back up.
      - Allows rooms which people can’t fit in.
    """)
    return


@app.cell
def _():
    frontroom = {"name": "FrontRoom",
                 "occupants": ["James"],
                 "max_capacity": 2,
                 "directions": [{"outside": "Garden"}, {"upstairs": "Bedroom"}, {"north": "Kitchen"}]
                }
    kitchen = {"name": "Kitchen",
               "occupants": [],
               "max_capacity": 1,
               "directions": {"south": "FrontRoom"}
              }
    garden = {}
    bedroom = {}
    maze = [frontroom, kitchen]

    d = {room["name"]:room["max_capacity"] for room in maze}
    d
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2.3 Working with files
    """)
    return


@app.cell
def _():
    from pathlib import Path

    return (Path,)


@app.cell
def _(Path):
    p = Path("~/tmp/test.txt").expanduser()
    p
    return (p,)


@app.cell
def _(Path):
    pp = Path("~").expanduser() / "tmp/test.txt"
    pp
    return (pp,)


@app.cell
def _(p, pp):
    pp == p
    return


@app.cell
def _():
    # magic command not supported in marimo; please file an issue to add support
    # %%writefile {p}
    # Hello world
    # I have nothing to say
    return


@app.cell
def _(p):
    txt = p.read_text()
    print(txt)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2.4 Downloading data
    """)
    return


@app.cell
def _():
    import requests
    from IPython.display import Image

    return Image, requests


@app.cell
def _(requests):
    response = requests.get(
        "https://static-maps.yandex.ru:443/1.x",
        params={
            "size": "400,400",  # size of map
            "ll": "-0.1275,51.51",  # longitude & latitude of centre
            "z": 12,  # zoom level
            "l": "sat",  # map layer (satellite image)
            "lang": "en_US",  # language
        },
        timeout=60,
    )
    return (response,)


@app.cell
def _(Image, response):
    Image(response.content)
    return


@app.cell
def _(requests):
    sun_spots = requests.get("http://www.sidc.be/silso/INFO/snmtotcsv.php", timeout=60).text

    sun_spots.split('\n')[:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2.5 Data analysis example
    """)
    return


@app.cell
def _():
    from typing import Tuple

    return (Tuple,)


@app.cell
def _():
    import geopy

    return (geopy,)


@app.cell
def _(geopy):
    geocoder = geopy.geocoders.Nominatim(user_agent="student")
    geocoder.geocode("Cambridge", exactly_one=False)
    return (geocoder,)


@app.cell
def _(Tuple, geocoder):
    def geolocate(place: str) -> Tuple[float, float]:
        return geocoder.geocode(place, exactly_one=False)[0][1]

    return (geolocate,)


@app.cell
def _(geolocate):
    paris_loc = geolocate("Singapore")
    print(paris_loc)
    return


@app.cell
def _():
    from staticmap import StaticMap, CircleMarker

    return CircleMarker, StaticMap


@app.cell
def _(CircleMarker, StaticMap, geolocate):
    def map_of_location(place: str, zoom=12, size=(400, 400)):
        lat, lon = geolocate(place)
        m = StaticMap(size[0], size[1], url_template='https://tile.openstreetmap.org/{z}/{x}/{y}.png')
        m.add_marker(CircleMarker((lon, lat), 12, 5))
        return m.render(zoom=zoom, center=(lon, lat))

    return (map_of_location,)


@app.cell
def _(map_of_location):
    map_sg = map_of_location("Singapore", zoom=12)
    map_sg
    return (map_sg,)


@app.cell
def _(map_sg):
    type(map_sg)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Extra: Pytest inside notebook
    """)
    return


@app.cell
def _():
    from pytest import approx
    import ipytest
    ipytest.autoconfig()
    return


@app.cell
def _():
    # magic command not supported in marimo; please file an issue to add support
    # %%ipytest -qq -vv
    # 
    # 
    # def test_example():
    #     assert 1 == 1
    # 
    # 
    # def test_example2():
    #     assert 0.7 == approx(0.7 + 1e-6, rel=1e-5)
    return


if __name__ == "__main__":
    app.run()
