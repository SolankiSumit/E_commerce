import pandas as pd
import os
from pathlib import Path

# -------- CATEGORY RULE FUNCTION --------
def map_category(keyword, url):
    """Map keyword and URL to Category and Sub-Category"""
    keyword = str(keyword).lower().strip()
    url = str(url).lower().strip()

    # REAL ESTATE / JIOMART / MAGICBRICKS
    if "magicbricks" in url:
        return "Real Estate", extract_location(keyword)
    if "jiomart" in url:
        return "E-commerce", "Grocery & General"

    # E-COMMERCE
    if "indiamart" in url:
        return "E-commerce", "B2B Marketplace"

    # FOOD & DELIVERY
    if "zomato" in url:
        return "Food & Dining", extract_food(keyword)
    if "swiggy" in url:
        return "Food & Delivery", extract_food(keyword)

    # LOCAL SERVICES / MAGIC PIN
    if "magicpin" in url:
        return "Local Services", extract_magicpin_service(keyword)

    # KEYWORD-BASED DETECTION
    if "school" in keyword or "college" in keyword or "coaching" in keyword:
        return "Education", "Educational Services"
    if "hospital" in keyword or "clinic" in keyword or "pharmacy" in keyword:
        return "Healthcare", "Medical Services"
    if "repair" in keyword or "service" in keyword:
        return "Services", "Repair & Maintenance"
    if "play" in keyword or "playschool" in keyword:
        return "Education", "Play Schools"
    if "property" in keyword or "flat" in keyword or "apartment" in keyword:
        return "Real Estate", extract_location(keyword)

    return "Others", "General"


# -------- SUB CATEGORY HELPERS --------
def extract_location(keyword):
    """Extract location from keyword"""
    words = keyword.split()
    # Common location indicators
    location_words = ["near", "in", "at"]
    
    for i, word in enumerate(words):
        if word in location_words and i + 1 < len(words):
            return " ".join(words[i+1:]).capitalize()
    
    if len(words) > 1:
        return words[-1].capitalize()
    return "Location"


def extract_food(keyword):
    """Extract food type from keyword"""
    food_keywords = {
        "pizza": "Pizza",
        "burger": "Burgers",
        "cafe": "Cafe",
        "coffee": "Coffee Shop",
        "restaurant": "Restaurants",
        "biryani": "Biryani",
        "chinese": "Chinese",
        "north": "North Indian",
        "south": "South Indian",
        "fast food": "Fast Food",
        "dessert": "Desserts",
        "bakery": "Bakery",
        "sushi": "Sushi",
        "bar": "Bar & Lounge"
    }
    
    keyword_lower = keyword.lower()
    for food_key, food_label in food_keywords.items():
        if food_key in keyword_lower:
            return food_label
    
    return "Restaurants"


def extract_magicpin_service(keyword):
    """Extract service type from MagicPin keyword"""
    service_keywords = {
        "salon": "Salon & Spa",
        "spa": "Salon & Spa",
        "gym": "Fitness",
        "yoga": "Fitness",
        "doctor": "Healthcare",
        "clinic": "Healthcare",
        "cafe": "Food & Beverage",
        "restaurant": "Food & Beverage",
        "beauty": "Salon & Spa",
        "entertainment": "Entertainment",
        "movie": "Entertainment",
        "play": "Entertainment",
        "hotel": "Travel & Stay",
        "resort": "Travel & Stay"
    }
    
    keyword_lower = keyword.lower()
    for service_key, service_label in service_keywords.items():
        if service_key in keyword_lower:
            return service_label
    
    return "Local Services"


# -------- PROCESS FILE --------
def process_file(input_file):
    """Process a single Excel file and add Category & Sub-Category columns"""
    try:
        print(f"\n📄 Processing: {input_file}")
        
        # Read Excel file
        df = pd.read_excel(input_file)
        
        # Check if required columns exist
        if "Keyword" not in df.columns or "URL" not in df.columns:
            print(f"⚠️  Skipped: {input_file} - Missing 'Keyword' or 'URL' columns")
            return False
        
        categories = []
        subcategories = []

        # Map categories and sub-categories
        for _, row in df.iterrows():
            keyword = row.get("Keyword", "")
            url = row.get("URL", "")
            cat, subcat = map_category(keyword, url)
            categories.append(cat)
            subcategories.append(subcat)

        # Insert new columns at the beginning
        df.insert(0, "Category", categories)
        df.insert(1, "Sub-Category", subcategories)

        # Save updated file with UPDATED prefix
        output_file = input_file.replace(".xlsx", "_MAPPED.xlsx")
        df.to_excel(output_file, index=False)

        print(f"✅ Completed: {output_file}")
        print(f"   Total rows processed: {len(df)}")
        return True

    except Exception as e:
        print(f"❌ Error processing {input_file}: {str(e)}")
        return False


# -------- MAIN AUTOMATION --------
def main():
    """Process all Excel files in the current directory"""
    current_dir = Path(__file__).parent
    excel_files = list(current_dir.glob("Positions.*.xlsx"))
    
    if not excel_files:
        print("❌ No Excel files found with pattern 'Positions.*.xlsx'")
        return
    
    print(f"\n{'='*60}")
    print(f"🤖 DATA MAPPING AUTOMATION STARTED")
    print(f"{'='*60}")
    print(f"Found {len(excel_files)} file(s) to process")
    
    success_count = 0
    
    for excel_file in sorted(excel_files):
        if process_file(str(excel_file)):
            success_count += 1
    
    print(f"\n{'='*60}")
    print(f"✨ AUTOMATION COMPLETE")
    print(f"{'='*60}")
    print(f"Successfully processed: {success_count}/{len(excel_files)} files")
    print(f"\n📁 Output files created with '_MAPPED' suffix")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
