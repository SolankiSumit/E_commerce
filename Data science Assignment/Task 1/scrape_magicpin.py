from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

print("🚀 Starting advanced gym scraper...")

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=chrome_options)
all_gyms = set()

def extract_gyms_from_page(soup):
    """Extract gym names using multiple strategies"""
    gyms = set()
    
    # Strategy 1: Look for all clickable text elements
    for element in soup.find_all(['a', 'div', 'span', 'h3', 'h4', 'p']):
        text = element.get_text(strip=True)
        
        if not text or len(text) < 4 or len(text) > 150:
            continue
        
        # Gym-related keywords
        gym_keywords = ["gym", "fitness", "yoga", "workout", "sports", "aerobics", "crossfit", 
                       "pilates", "zumba", "boxing", "martial", "dance", "trainer", "studio", 
                       "center", "club", "health", "training", "strength"]
        
        # Product/skip keywords
        skip_keywords = ["vest", "glove", "shirt", "pant", "shoe", "dress", "nike", "adidas", 
                        "levis", "puma", "decathlon", "amazon", "flipkart", "myntra", "bag", 
                        "towel", "legging", "short", "sausage", "chicken", "food", "toy", "bed", "protein"]
        
        # Check conditions
        has_gym = any(k in text.lower() for k in gym_keywords)
        skip_count = sum(1 for k in skip_keywords if k in text.lower())
        has_price = "₹" in text
        is_product_listing = any(p in text.lower() for p in ["pack of", "set of", "combo", "bundle", "offer", "rs", "off"])
        
        # Add if it looks like a gym
        if has_gym and skip_count == 0 and not is_product_listing and not has_price:
            gyms.add(text.strip())
    
    # Strategy 2: Look in data attributes and JSON
    scripts = soup.find_all('script')
    for script in scripts:
        if script.string:
            # Look for business names in JSON data
            matches = re.findall(r'"name"\s*:\s*"([^"]{5,120})"', script.string)
            for match in matches:
                if any(k in match.lower() for k in ["gym", "fitness", "yoga", "sports"]):
                    if not any(k in match.lower() for k in ["vest", "bag", "shoe", "dress", "nike"]):
                        gyms.add(match)
    
    return gyms

try:
    # Search strategy 1: Multiple keywords
    search_keywords = [
        "gym", "fitness center", "yoga studio", "workout", "sports center",
        "aerobics", "crossfit gym", "pilates studio", "zumba", "boxing gym",
        "martial arts", "dance studio", "fitness trainer", "health club"
    ]
    
    print("\n📋 Phase 1: Searching with multiple keywords...")
    for keyword in search_keywords:
        url = f"https://magicpin.in/Ahmedabad/search?query={keyword.replace(' ', '%20')}"
        print(f"\n🔎 Searching: {keyword}")
        
        try:
            driver.get(url)
            time.sleep(3)
            
            # Extremely aggressive scrolling
            for scroll_count in range(8):
                driver.execute_script("window.scrollBy(0, 1000);")
                time.sleep(0.8)
            
            soup = BeautifulSoup(driver.page_source, "html.parser")
            found = extract_gyms_from_page(soup)
            all_gyms.update(found)
            
            print(f"  ✓ Found {len(found)} new gyms (Total: {len(all_gyms)})")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    # Search strategy 2: Try category pages
    print("\n📋 Phase 2: Trying category-based URLs...")
    category_urls = [
        "https://magicpin.in/Ahmedabad/category?categoryName=Gyms",
        "https://magicpin.in/Ahmedabad/category?categoryName=Fitness",
        "https://magicpin.in/Ahmedabad/category?categoryName=Yoga",
    ]
    
    for url in category_urls:
        print(f"\n🔎 Category: {url.split('categoryName=')[-1]}")
        try:
            driver.get(url)
            time.sleep(3)
            
            # Scroll multiple times
            for _ in range(8):
                driver.execute_script("window.scrollBy(0, 1000);")
                time.sleep(0.8)
            
            soup = BeautifulSoup(driver.page_source, "html.parser")
            found = extract_gyms_from_page(soup)
            all_gyms.update(found)
            
            print(f"  ✓ Found {len(found)} gyms (Total: {len(all_gyms)})")
        except:
            pass
    
    # Search strategy 3: Location-based browsing
    print("\n📋 Phase 3: Browsing localities in Ahmedabad...")
    localities = ["Sarkhej", "Satellite", "Navrangpura", "C.G Road", "Thaltej", "Iscon", "Vastrapur"]
    for locality in localities:
        url = f"https://magicpin.in/Ahmedabad/{locality}/search?query=gym"
        print(f"\n🔎 Locality: {locality}")
        try:
            driver.get(url)
            time.sleep(2)
            
            for _ in range(5):
                driver.execute_script("window.scrollBy(0, 800);")
                time.sleep(0.6)
            
            soup = BeautifulSoup(driver.page_source, "html.parser")
            found = extract_gyms_from_page(soup)
            all_gyms.update(found)
            
            print(f"  ✓ Found {len(found)} gyms (Total: {len(all_gyms)})")
        except:
            pass
    
    # Clean and filter results - remove obvious products, keep only gyms/facilities
    filtered_gyms = set()
    
    for gym in all_gyms:
        gym_lower = gym.lower()
        
        # Skip if it contains product-related keywords
        product_keywords = ["printed", "wired", "smart watch", "smartwatch", "sunglasses", "earphone", 
                           "speaker", "headphone", "socks", "shirt", "jacket", "watch", "cover", "table", 
                           "sofa", "chair", "cushion", "necklace", "earring", "bangle", "wallet", "headband",
                           "earbuds", "mouse", "controller", "game", "video", "ice cream", "cookies", "salad", 
                           "sausage", "chicken", "food", "juice", "smoothie", "omelet", "bowl", "dish", "plate",
                           "microphone", "speaker", "sound bar", "wireless", "bluetooth", "gadget", "device"]
        
        # Skip if it's just product descriptions or "No results"
        if gym.startswith("No results") or gym.startswith("Try checking"):
            continue
        
        # Count product keywords
        product_count = sum(1 for kw in product_keywords if kw in gym_lower)
        
        # Keep only if it has gym keywords and minimal product keywords
        gym_keywords = ["gym", "fitness", "yoga", "center", "studio", "sports", "health", "training", "workout"]
        has_gym_keyword = any(kw in gym_lower for kw in gym_keywords)
        
        if has_gym_keyword and product_count == 0 and len(gym) > 5:
            # Also skip entries that are just location info
            if not any(phrase in gym_lower for phrase in ["km,", "open now", "save ", "opens in", "mins"]):
                filtered_gyms.add(gym.strip())
    
    # Remove duplicates
    filtered_gyms = sorted(list(set(filtered_gyms)))
    
    print(f"\n{'='*70}")
    print(f"✅ SCRAPING COMPLETE: Found {len(filtered_gyms)} actual gym facilities")
    print(f"{'='*70}\n")
    
    # Create DataFrame
    df = pd.DataFrame({
        "GYM Name": [g[:100] for g in filtered_gyms],
        "Address": ["Address not found"] * len(filtered_gyms),
        "Area": ["Ahmedabad"] * len(filtered_gyms),
        "City": ["Ahmedabad"] * len(filtered_gyms),
        "State": ["Gujarat"] * len(filtered_gyms),
        "Phone Number": [""] * len(filtered_gyms),
        "Timings": [""] * len(filtered_gyms)
    })
    
    # Save CSV
    df.to_csv("gyms_ahmedabad.csv", index=False)
    print(f"💾 Saved to gyms_ahmedabad.csv\n")
    
    if len(df) > 0:
        print(f"📋 Found {len(df)} gym facilities:\n")
        for idx, row in df.iterrows():
            print(f"{idx+1}. {row['GYM Name']}")
    else:
        print("⚠️  No gyms found")
    
finally:
    print(f"\n🔚 Closing browser...")
    driver.quit()
    print("✅ Done!")
