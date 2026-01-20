import requests
import pandas as pd

# ------------------ CONFIG ------------------
CITY_NAME = "Ahmedabad"
OVERPASS_URL = "https://overpass-api.de/api/interpreter"

# ------------------ OVERPASS QUERY ------------------
query = f"""
[out:json];
area["name"="{CITY_NAME}"]->.searchArea;
(
  node["tourism"="attraction"](area.searchArea);
  node["tourism"="museum"](area.searchArea);
  node["tourism"="park"](area.searchArea);
  node["tourism"="gallery"](area.searchArea);
  node["historic"="monument"](area.searchArea);
);
out body;
"""

print("Sending request to Overpass API...")

response = requests.post(OVERPASS_URL, data=query)

if response.status_code != 200:
    print("API request failed:", response.status_code)
    exit()

data = response.json()
elements = data.get("elements", [])

print("Total locations received:", len(elements))

# ------------------ DATA LISTS ------------------
names = []
types = []
latitudes = []
longitudes = []
cities = []

# ------------------ EXTRACT DATA ------------------
for place in elements:
    tags = place.get("tags", {})

    name = tags.get("name", "Not Available")

    if "tourism" in tags:
        place_type = tags["tourism"]
    elif "historic" in tags:
        place_type = tags["historic"]
    else:
        place_type = "Unknown"

    lat = place.get("lat")
    lon = place.get("lon")

    # Save only valid locations
    if lat and lon:
        names.append(name)
        types.append(place_type)
        latitudes.append(lat)
        longitudes.append(lon)
        cities.append(CITY_NAME)

# ------------------ CREATE DATAFRAME ------------------
df = pd.DataFrame({
    "Name": names,
    "Type": types,
    "Latitude": latitudes,
    "Longitude": longitudes,
    "City": cities
})

# Remove duplicates
df.drop_duplicates(inplace=True)

# ------------------ SAVE CSV ------------------
file_name = "tourist_attractions_ahmedabad.csv"
df.to_csv(file_name, index=False)

print("✅ Task 3 completed successfully")
print("✅ Total tourist attractions saved:", len(df))
print("✅ CSV file created:", file_name)
