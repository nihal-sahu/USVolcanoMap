import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
html = """<h2>Volcano Information:</h2>
<b> Name: </b><a href="https://www.google.com/search?q=%%22%s Volcano%%22" target="_blank"> %s Volcano </a> <br>
<b> Type: </b>%s <br>
<b> Elevation: </b>%s m
"""

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
volcano_type = list(data["TYPE"])

def color_change(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location = [37.0902, -95.7129], zoom_start = 4, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")

fg.add_child(folium.GeoJson(data = open("world.json", "r", encoding = "utf-8-sig").read(), 
style_function = lambda x: {"fillColor": "yellow" if x["properties"]["POP2005"] < 10000000
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000
else "red"}))

for lt, ln, el, nam, vol_ty in zip(lat, lon, elev, name, volcano_type):
    iframe = folium.IFrame(html = html % (nam, nam, vol_ty, el), width = "270x", height = "135px")
    fg.add_child(folium.CircleMarker(location = [lt, ln], radius = 10, popup = folium.Popup(iframe), fill_color = color_change(el), color = "grey", fill_opacity = 0.8))

map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("Map1.html")



