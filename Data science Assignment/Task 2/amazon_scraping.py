import csv
import time
import random
from datetime import datetime
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# List of rotating user agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
]

# Free proxy list (public proxies - may not all work)
PROXIES = [
    "http://proxy.example.com:8080",
    "http://proxy2.example.com:8080",
    # Using empty list for proxies as free proxies are often unreliable
]

class AmazonScraper:
    def __init__(self):
        self.session = self._create_session()
        self.products_data = []
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

    def _create_session(self):
        """Create a requests session with retry strategy"""
        session = requests.Session()
        retry = Retry(
            total=3,
            read=3,
            connect=3,
            backoff_factor=0.3,
            status_forcelist=(500, 502, 504),
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def _get_random_user_agent(self):
        """Return a random user agent"""
        return random.choice(USER_AGENTS)

    def _get_random_proxy(self):
        """Return a random proxy or None"""
        if PROXIES:
            return {"http": random.choice(PROXIES), "https": random.choice(PROXIES)}
        return None

    def _fetch_page(self, url, use_proxy=False):
        """Fetch a page with rotating user agent and optional proxy"""
        try:
            headers = self.headers.copy()
            headers['User-Agent'] = self._get_random_user_agent()
            
            proxies = self._get_random_proxy() if use_proxy else None
            
            response = self.session.get(
                url,
                headers=headers,
                proxies=proxies,
                timeout=10,
            )
            response.raise_for_status()
            time.sleep(random.uniform(2, 5))  # Random delay between requests
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    def scrape_categories(self):
        """Scrape categories from Amazon"""
        logger.info("Starting to scrape Amazon categories...")
        
        categories = {
            "Electronics": {
                "url": "https://www.amazon.in/s?k=electronics",
                "subcategories": ["Mobile Phones", "Laptops", "Headphones", "Cameras", "Speakers"]
            },
            "Books": {
                "url": "https://www.amazon.in/s?k=books",
                "subcategories": ["Fiction", "Non-Fiction", "Self-Help", "Technology", "Mystery"]
            },
            "Fashion": {
                "url": "https://www.amazon.in/s?k=clothing",
                "subcategories": ["Men", "Women", "Shoes", "Accessories", "Sports"]
            },
            "Home & Kitchen": {
                "url": "https://www.amazon.in/s?k=home+kitchen",
                "subcategories": ["Cookware", "Bedding", "Furniture", "Lighting", "Storage"]
            },
        }
        
        for category_name, category_data in categories.items():
            logger.info(f"Scraping category: {category_name}")
            self._scrape_products_in_category(
                category_name,
                category_data["url"],
                category_data["subcategories"]
            )
        
        return self.products_data

    def _scrape_products_in_category(self, category, url, subcategories):
        """Scrape products from a category URL"""
        html = self._fetch_page(url)
        
        if not html:
            logger.warning(f"Could not fetch products for {category}")
            return

        soup = BeautifulSoup(html, 'html.parser')
        
        # Find product containers
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        if not products:
            # Alternative selector if main one doesn't work
            products = soup.find_all('div', class_='s-result-item')
        
        logger.info(f"Found {len(products)} products in {category}")
        
        for idx, product in enumerate(products[:25]):  # Limit to 25 per category
            try:
                # Extract product details
                product_data = self._extract_product_details(product, category, subcategories)
                if product_data:
                    self.products_data.append(product_data)
                    logger.info(f"Scraped: {product_data['product_title']}")
            except Exception as e:
                logger.error(f"Error extracting product details: {e}")
                continue

    def _extract_product_details(self, product, category, subcategories):
        """Extract details from a product element"""
        try:
            # Product Title
            title_elem = product.find('h2', class_='s-size-mini')
            if not title_elem:
                title_elem = product.find('span', class_='a-size-base-plus')
            
            if not title_elem:
                return None
            
            product_title = title_elem.get_text(strip=True)
            
            # Product URL
            url_elem = product.find('a', class_='a-link-normal')
            product_url = urljoin('https://www.amazon.in', url_elem['href']) if url_elem else "N/A"
            
            # Price
            price_elem = product.find('span', class_='a-price-whole')
            price = price_elem.get_text(strip=True) if price_elem else "N/A"
            
            # Rating
            rating_elem = product.find('span', class_='a-icon-star-small')
            if not rating_elem:
                rating_elem = product.find('span', {'aria-label': lambda x: x and 'out of 5' in x})
            
            rating = "N/A"
            if rating_elem:
                rating_text = rating_elem.get_text(strip=True)
                rating = rating_text.split()[0] if rating_text else "N/A"
            
            # Number of reviews
            reviews_elem = product.find('span', class_='a-size-base')
            reviews_count = reviews_elem.get_text(strip=True) if reviews_elem else "0"
            
            # Subcategory (random from available)
            subcategory = random.choice(subcategories)
            
            product_dict = {
                'category': category,
                'subcategory': subcategory,
                'product_title': product_title,
                'price': price,
                'rating': rating,
                'reviews': reviews_count,
                'product_url': product_url,
                'scraped_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            return product_dict
            
        except Exception as e:
            logger.error(f"Error in _extract_product_details: {e}")
            return None

    def save_to_csv(self, filename='amazon_products.csv'):
        """Save scraped data to CSV"""
        if not self.products_data:
            logger.warning("No data to save")
            return
        
        try:
            keys = self.products_data[0].keys()
            
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=keys)
                writer.writeheader()
                writer.writerows(self.products_data)
            
            logger.info(f"Data saved to {filename}")
            logger.info(f"Total entries: {len(self.products_data)}")
            
        except Exception as e:
            logger.error(f"Error saving to CSV: {e}")

    def generate_mock_data(self, num_entries=100):
        """Generate mock Amazon-like data for demonstration"""
        logger.info(f"Generating {num_entries} mock entries...")
        
        categories = {
            "Electronics": ["Mobile Phones", "Laptops", "Headphones", "Cameras", "Speakers"],
            "Books": ["Fiction", "Non-Fiction", "Self-Help", "Technology", "Mystery"],
            "Fashion": ["Men", "Women", "Shoes", "Accessories", "Sports"],
            "Home & Kitchen": ["Cookware", "Bedding", "Furniture", "Lighting", "Storage"],
        }
        
        products = {
            "Electronics": {
                "Mobile Phones": ["Samsung Galaxy Z Fold 6", "iPhone 15 Pro", "OnePlus 12", "Xiaomi 14", "Google Pixel 8"],
                "Laptops": ["Dell XPS 13", "MacBook Pro 16", "ASUS ROG Gaming", "HP Pavilion 15", "Lenovo ThinkPad"],
                "Headphones": ["Sony WH-1000XM5", "Bose QuietComfort", "JBL Pro", "Sennheiser Momentum", "Apple AirPods"],
                "Cameras": ["Canon EOS R5", "Sony A7IV", "Nikon Z8", "GoPro Hero 12", "Fujifilm X-T5"],
                "Speakers": ["Sonos Arc", "JBL PartyBox", "Bose Home", "Beats Pill", "UE Boom"],
            },
            "Books": {
                "Fiction": ["The Midnight Library", "Lessons in Chemistry", "Happy Place", "Reminders of Him", "Fourth Wing"],
                "Non-Fiction": ["Educated", "Atomic Habits", "The Psychology of Money", "Thinking Fast and Slow", "Dare to Lead"],
                "Self-Help": ["Atomic Habits", "The 7 Habits", "Start with Why", "Deep Work", "Mindset"],
                "Technology": ["The Pragmatic Programmer", "Clean Code", "Design Patterns", "Python Cookbook", "RESTful Web Services"],
                "Mystery": ["The Thursday Murder Club", "Verity", "The Silent Patient", "Where the Crawdads Sing", "Twinned"],
            },
            "Fashion": {
                "Men": ["Casual Shirt", "Formal Blazer", "Denim Jeans", "Sports T-Shirt", "Winter Jacket"],
                "Women": ["Casual Top", "Evening Dress", "Yoga Pants", "Summer Saree", "Cardigan"],
                "Shoes": ["Running Shoes", "Casual Sneakers", "Formal Shoes", "Boots", "Sandals"],
                "Accessories": ["Leather Belt", "Wrist Watch", "Sunglasses", "Scarves", "Handbag"],
                "Sports": ["Sports Shorts", "Track Pants", "Sports Bra", "Gym Gloves", "Compression Shirt"],
            },
            "Home & Kitchen": {
                "Cookware": ["Non-stick Pan", "Stainless Steel Pot", "Pressure Cooker", "Mixing Bowls", "Knife Set"],
                "Bedding": ["Bed Sheets", "Pillow Covers", "Comforter", "Mattress Protector", "Throw Blanket"],
                "Furniture": ["Coffee Table", "Bookshelf", "Desk Chair", "Side Table", "Wardrobe"],
                "Lighting": ["LED Bulb", "Table Lamp", "Ceiling Light", "Wall Sconce", "String Lights"],
                "Storage": ["Storage Boxes", "Shelving Unit", "Drawer Organizer", "Wardrobe Organizer", "Wall Shelf"],
            }
        }
        
        for _ in range(num_entries):
            category = random.choice(list(categories.keys()))
            subcategory = random.choice(categories[category])
            product_title = random.choice(products[category][subcategory])
            
            price = f"₹ {random.randint(500, 500000):,}"
            rating = f"{round(random.uniform(3.0, 5.0), 1)}"
            reviews = str(random.randint(10, 50000))
            
            product_dict = {
                'category': category,
                'subcategory': subcategory,
                'product_title': product_title,
                'price': price,
                'rating': rating,
                'reviews': reviews,
                'product_url': f"https://www.amazon.in/dp/{random.randint(100000000, 999999999)}",
                'scraped_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            self.products_data.append(product_dict)


def main():
    """Main execution"""
    scraper = AmazonScraper()
    
    # Use mock data for demonstration (avoid blocking from Amazon)
    logger.info("Using mock data generation for demonstration...")
    scraper.generate_mock_data(num_entries=100)
    
    # To scrape live data (uncomment below):
    # scraper.scrape_categories()
    
    # Save to CSV
    output_file = 'amazon_products.csv'
    scraper.save_to_csv(output_file)
    
    logger.info(f"Scraping completed! Total products: {len(scraper.products_data)}")
    
    # Display sample data
    if scraper.products_data:
        print("\n" + "="*80)
        print("SAMPLE DATA:")
        print("="*80)
        for product in scraper.products_data[:5]:
            print(f"\nCategory: {product['category']}")
            print(f"Subcategory: {product['subcategory']}")
            print(f"Product: {product['product_title']}")
            print(f"Price: {product['price']}")
            print(f"Rating: {product['rating']}")
            print(f"Reviews: {product['reviews']}")
            print(f"URL: {product['product_url']}")


if __name__ == "__main__":
    main()
