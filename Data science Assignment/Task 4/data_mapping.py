
import pandas as pd
import os

# -------- CATEGORY RULE FUNCTION --------
def map_category(keyword, url):
    keyword = str(keyword).lower()
    url = str(url).lower()

    # REAL ESTATE
    if "magicbricks" in url or "property" in keyword or "flat" in keyword:
        return "Real Estate", extract_location(keyword)

    # FOOD
    if "zomato" in url or "swiggy" in url:
        return "Food / Restaurants", extract_food(keyword)

    # SERVICES
    if "sulekha" in url or "indiamart" in url:
        return "Services", extract_service(keyword, url)

    # EDUCATION
    if "school" in keyword or "college" in keyword or "coaching" in keyword:
        return "Education", "Educational Services"

    # HEALTHCARE
    if "hospital" in keyword or "clinic" in keyword or "pharmacy" in keyword:
        return "Healthcare", "Medical Services"

    return "Others", "General"


# -------- SUB CATEGORY HELPERS --------
def extract_location(keyword):
    words = keyword.split()
    return words[-1].capitalize() if len(words) > 1 else "Location"

def extract_food(keyword):
    food_words = ["pizza", "burger", "cafe", "restaurant", "biryani"]
    for food in food_words:
        if food in keyword:
            return food.capitalize()
    return "Restaurant"

def extract_service(keyword, url):
    if "play" in keyword:
        return "Play Schools"
    if "repair" in keyword:
        return "Repair Services"
    if "consultant" in keyword:
        return "Consulting"
    return "General Services"


# -------- PROCESS FILE --------
def process_file(input_file):
    df = pd.read_excel(input_file)

    categories = []
    subcategories = []

    for _, row in df.iterrows():
        cat, subcat = map_category(row["Keyword"], row["URL"])
        categories.append(cat)
        subcategories.append(subcat)

    df.insert(0, "Category", categories)
    df.insert(1, "Sub-Category", subcategories)

    output_file = "UPDATED_" + os.path.basename(input_file)
    df.to_excel(output_file, index=False)

    print(f"✅ Completed: {output_file}")


# -------- RUN --------
file_name = "Positions.sulekha.com.xlsx"  # CHANGE FILE NAME HERE
process_file(file_name)
