import localutils as lutil

# Define in which intervals (in minutes) the data should be divided
# The interval can be set to -1 to display all data at once
interval = 5

# File from which the location data is obtained
data_to_read = "random.gpx"

# If you are using "path" as the option you can adjust the properties for drawing the line:
line_color = "red"
line_width = 4
line_opacity = 1.0

# If you are using "heatmap" as the option you can adjust the properties for each heatmap entry
heatmap_opacity = 0.5
heatmap_radius = 25

# Define to which user the data belongs (will be changed afterwards in the project)
username = "testuser"

# Define the name of the html file where your results will be displayed
main_html_name = "indexpage"

# Define which method you want to use to display your data
# Options: "heatmap" "path"
method = "path"

#################################################
line_data = [line_color, line_width, line_opacity]
heatmap_data = [heatmap_opacity, heatmap_radius]
lutil.parse_with_interval (interval, username, main_html_name, method, data_to_read, line_data, heatmap_data)
