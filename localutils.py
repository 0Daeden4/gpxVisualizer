from folium.plugins import HeatMap
from folium import PolyLine

from gpxplotter import create_folium_map, read_gpx_file
import interfacemaker as ifm

def name_format(time, username):
    month = time.month
    day = time.day
    hour = time.hour
    minute = time.minute
    second = time.second
    # format filename to your liking
    return username + f"-m{month}-d{day}-{hour}_{minute}"

def save_file(data, map, filename, method, line_data):
    map.fit_bounds(data)
    if (method == "heatmap"):
        HeatMap(data, name="Heatmap", radius=30).add_to(map)
    elif (method == "path"):
        PolyLine(data, color=line_data[0], weight=line_data[1], opacity=line_data[2]).add_to(map)
    map.save(f"{filename}.html")



def parse_with_interval (interval, username, main_html_name, method, gpx_to_read, line_data):
    # Support for multiple tracks
    for track in read_gpx_file(gpx_to_read):
        file_names = []
        username = username
        for i, segment in enumerate(track["segments"]):
            data = []
            switch = 0
            prev_minute = -1
            map = create_folium_map(tiles="openstreetmap")

            # to make users data distinct from each other
            # placeholder
            name = ""
            for lat, lon, time in zip(segment["lat"], segment["lon"], segment["time"]):
                minute = time.minute
                data.append([lat,lon])

                # for initially naming the file
                if switch == 0:
                    name = name_format(time, username)
                    print("switch: ",name)
                    file_names.append(name)
                    switch = 1

                # change different map interval in minutes to your liking
                if (minute%interval == 0) & (minute != prev_minute):
                    save_file(data, map, name, method, line_data)
                    map = create_folium_map(tiles="openstreetmap")
                    prev_minute = minute
                    data = []
                    name = name_format(time, username)
                    print("inteval: ",name)
                    file_names.append(name)

            save_file(data, map, name, method, line_data)
            break
        #print(file_names)
        ifm.create_index_page(main_html_name, file_names)
