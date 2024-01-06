import geopandas as gpd
import matplotlib.pyplot as plt

# Load cities dataset
cities = gpd.read_file(gpd.datasets.get_path("naturalearth_cities"))

# Filter for the desired cities
cities_filtered = cities[cities["name"].isin(["New York", "Los Angeles", "New Orleans"])]

# Get basemap from Natural Earth
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
usa = world[world.name == "United States"]

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))
usa.plot(ax=ax, color="lightgrey")
cities_filtered.plot(ax=ax, color="red", markersize=50, marker="*")

# Annotate cities
for index, row in cities_filtered.iterrows():
    ax.annotate(row["name"], xy=row.geometry.coords[0], xytext=(3, 3), textcoords="offset points", fontsize=9)

ax.set_title("City Locations on US Map")
plt.show()