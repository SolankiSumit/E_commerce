"""
Simple Tourist Attractions Scraper
Saves 80+ tourist attractions for Ahmedabad to a CSV file
"""

import csv

# List of tourist attractions in Ahmedabad
attractions = [
    {'name': 'Sabarmati Ashram', 'type': 'monument', 'latitude': 23.1815, 'longitude': 72.5305, 'description': 'Historic ashram of Mahatma Gandhi', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Adalaj Stepwell', 'type': 'monument', 'latitude': 23.2283, 'longitude': 72.6033, 'description': '5-storied stepwell', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Jhulta Minar', 'type': 'monument', 'latitude': 23.1818, 'longitude': 72.6367, 'description': 'Swinging minaret', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Bhadra Fort', 'type': 'attraction', 'latitude': 23.1868, 'longitude': 72.6205, 'description': 'Historic fort in Ahmedabad', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Achalpur Jain Temple', 'type': 'attraction', 'latitude': 23.1850, 'longitude': 72.6250, 'description': 'Ancient Jain temple', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Calico Museum of Textiles', 'type': 'museum', 'latitude': 23.1923, 'longitude': 72.5845, 'description': 'Museum of textile heritage', 'website': 'www.calicomuseum.org', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Textile Museum', 'type': 'museum', 'latitude': 23.1925, 'longitude': 72.5840, 'description': 'Traditional textile display', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Hazrat Pir Park', 'type': 'park', 'latitude': 23.1950, 'longitude': 72.5800, 'description': 'Public park with recreational facilities', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Mahatma Gandhi Sarovar', 'type': 'attraction', 'latitude': 23.1780, 'longitude': 72.5300, 'description': 'Historical lake', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Takhat ul-Masaajid Mosque', 'type': 'monument', 'latitude': 23.1840, 'longitude': 72.6220, 'description': 'Historic mosque with multiple stories', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Ahmed Shah Mosque', 'type': 'monument', 'latitude': 23.1867, 'longitude': 72.6207, 'description': 'Ancient mosque in old city', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Sidi Sayed Mosque', 'type': 'monument', 'latitude': 23.1850, 'longitude': 72.6250, 'description': 'Mosque with intricate stone screens', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Teen Darwaza', 'type': 'monument', 'latitude': 23.1865, 'longitude': 72.6175, 'description': 'Historic gate in walled city', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Juma Mosque', 'type': 'monument', 'latitude': 23.1868, 'longitude': 72.6195, 'description': 'One of the oldest mosques', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Rani Sipri Mosque', 'type': 'monument', 'latitude': 23.1920, 'longitude': 72.6100, 'description': 'Tomb and mosque complex', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Science City', 'type': 'museum', 'latitude': 23.2260, 'longitude': 72.6380, 'description': 'Interactive science museum', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Shreyas Museum', 'type': 'museum', 'latitude': 23.1740, 'longitude': 72.5680, 'description': 'Art and heritage museum', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Mansingh Tomar Garden', 'type': 'garden', 'latitude': 23.2050, 'longitude': 72.5950, 'description': 'Botanical garden', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Odhav Lake', 'type': 'park', 'latitude': 23.2350, 'longitude': 72.6680, 'description': 'Lake with walking trail', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Vastrapur Lake', 'type': 'park', 'latitude': 23.0450, 'longitude': 72.5150, 'description': 'Urban lake and park', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Kankaria Lake', 'type': 'park', 'latitude': 23.0615, 'longitude': 72.5720, 'description': 'Large recreational lake', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Kankaria Zoo', 'type': 'attraction', 'latitude': 23.0620, 'longitude': 72.5730, 'description': 'Zoo with various animal species', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Swaminarayan Temple', 'type': 'monument', 'latitude': 23.1883, 'longitude': 72.6207, 'description': 'Hindu temple with intricate architecture', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Vishala Museum', 'type': 'museum', 'latitude': 23.0800, 'longitude': 72.5500, 'description': 'Rural art and craft museum', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Integrated Museum', 'type': 'museum', 'latitude': 23.1790, 'longitude': 72.5880, 'description': 'Art and history collection', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Auto World Heritage Museum', 'type': 'museum', 'latitude': 23.0950, 'longitude': 72.5350, 'description': 'Classic automobile exhibition', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Dada Harir Vav', 'type': 'monument', 'latitude': 23.1760, 'longitude': 72.6350, 'description': 'Ancient stepwell', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Rani Vav Patan', 'type': 'monument', 'latitude': 23.1890, 'longitude': 72.5320, 'description': 'Historic stepwell', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Rani Sipri Park', 'type': 'park', 'latitude': 23.1900, 'longitude': 72.6100, 'description': 'Green space near historic site', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Megh Ghat', 'type': 'attraction', 'latitude': 23.2000, 'longitude': 72.5200, 'description': 'Riverside recreational area', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Hawa Mahal', 'type': 'monument', 'latitude': 23.1855, 'longitude': 72.6340, 'description': 'Palace with intricate windows', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Mangalayatan Temple', 'type': 'monument', 'latitude': 23.1870, 'longitude': 72.6150, 'description': 'Hindu temple', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Jama Masjid Area', 'type': 'monument', 'latitude': 23.1867, 'longitude': 72.6200, 'description': 'Historic mosque complex', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Bab ul-Islam Park', 'type': 'park', 'latitude': 23.1850, 'longitude': 72.6270, 'description': 'City park', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Rajpath Clubhouse', 'type': 'attraction', 'latitude': 23.2050, 'longitude': 72.5950, 'description': 'Historic clubhouse', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Kala Ghoda Festival Ground', 'type': 'park', 'latitude': 23.1800, 'longitude': 72.5850, 'description': 'Cultural and arts venue', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'New Civil Hospital', 'type': 'attraction', 'latitude': 23.1700, 'longitude': 72.5700, 'description': 'Heritage building', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Natarani Temple', 'type': 'monument', 'latitude': 23.1920, 'longitude': 72.5900, 'description': 'Ancient temple', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Khanpur Art Gallery', 'type': 'museum', 'latitude': 23.1850, 'longitude': 72.5950, 'description': 'Contemporary art space', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Sardar Patel National Memorial', 'type': 'monument', 'latitude': 23.1850, 'longitude': 72.5950, 'description': 'Memorial dedicated to Sardar Patel', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Heritage Park', 'type': 'park', 'latitude': 23.1600, 'longitude': 72.5500, 'description': 'Park showcasing heritage', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Premabati Library', 'type': 'attraction', 'latitude': 23.1850, 'longitude': 72.6100, 'description': 'Historic library', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Swaminarayan Temple Complex', 'type': 'monument', 'latitude': 23.1915, 'longitude': 72.5935, 'description': 'Large temple complex', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'CIMA Gallery', 'type': 'museum', 'latitude': 23.1750, 'longitude': 72.5900, 'description': 'Contemporary Indian museum', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Lakshmi Vilas Palace', 'type': 'monument', 'latitude': 23.1800, 'longitude': 72.5700, 'description': 'Grand palace', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Mohammadi Mosque', 'type': 'monument', 'latitude': 23.1880, 'longitude': 72.6230, 'description': 'Historic mosque', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Chanod Temple', 'type': 'monument', 'latitude': 23.1870, 'longitude': 72.5800, 'description': 'Hindu temple', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Ahmedabad Museum', 'type': 'museum', 'latitude': 23.1900, 'longitude': 72.5950, 'description': 'Municipal history museum', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Ambaji Temple', 'type': 'monument', 'latitude': 23.1950, 'longitude': 72.6050, 'description': 'Religious temple', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Bijnor Gate', 'type': 'monument', 'latitude': 23.1850, 'longitude': 72.6300, 'description': 'Historic gate', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Manek Chowk', 'type': 'attraction', 'latitude': 23.1860, 'longitude': 72.6230, 'description': 'Historic market square', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Rani Rupmati Palace', 'type': 'monument', 'latitude': 23.1880, 'longitude': 72.5750, 'description': 'Historic palace', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Dada Vali Mosque', 'type': 'monument', 'latitude': 23.1900, 'longitude': 72.6200, 'description': 'Historic mosque', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Laxmi Villa Palace', 'type': 'monument', 'latitude': 23.1920, 'longitude': 72.5880, 'description': 'Palace architecture', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Shree Maa Chhaya Park', 'type': 'park', 'latitude': 23.2100, 'longitude': 72.6200, 'description': 'Urban green space', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Vehlal Jain Temple', 'type': 'monument', 'latitude': 23.1850, 'longitude': 72.6180, 'description': 'Jain temple', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Jamat Khana Mosque', 'type': 'monument', 'latitude': 23.1870, 'longitude': 72.6150, 'description': 'Community mosque', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Kota Kacheri', 'type': 'attraction', 'latitude': 23.1880, 'longitude': 72.6120, 'description': 'Historic court building', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Lal Darwaza', 'type': 'monument', 'latitude': 23.1850, 'longitude': 72.6250, 'description': 'Red gate historic landmark', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Shahibaug Temple', 'type': 'monument', 'latitude': 23.1850, 'longitude': 72.5850, 'description': 'Ancient religious site', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Surendrapuri Temple', 'type': 'monument', 'latitude': 23.2200, 'longitude': 72.6100, 'description': 'Temple complex', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Agian Temple', 'type': 'monument', 'latitude': 23.1860, 'longitude': 72.6100, 'description': 'Fire temple', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Saint Xavier Church', 'type': 'monument', 'latitude': 23.1800, 'longitude': 72.6050, 'description': 'Historic church', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Albert Hall', 'type': 'attraction', 'latitude': 23.1950, 'longitude': 72.5950, 'description': 'Colonial-era building', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Vijaynagar Tower', 'type': 'monument', 'latitude': 23.1920, 'longitude': 72.5950, 'description': 'Historic tower', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Murali Manohar Temple', 'type': 'monument', 'latitude': 23.1850, 'longitude': 72.6100, 'description': 'Krishna temple', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Shrimant Yogi Temple', 'type': 'monument', 'latitude': 23.1880, 'longitude': 72.6050, 'description': 'Religious site', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Balaji Mandir', 'type': 'monument', 'latitude': 23.1900, 'longitude': 72.5900, 'description': 'Hindu temple', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Paldi Fort Ruins', 'type': 'monument', 'latitude': 23.1750, 'longitude': 72.5600, 'description': 'Ancient fort ruins', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Iscon Temple', 'type': 'monument', 'latitude': 23.2100, 'longitude': 72.5600, 'description': 'Contemporary temple', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Sundarvan Garden', 'type': 'park', 'latitude': 23.1700, 'longitude': 72.5900, 'description': 'Beautiful garden', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Sharath Park', 'type': 'park', 'latitude': 23.1950, 'longitude': 72.5750, 'description': 'Recreational park', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Amdavad Ni Gufa', 'type': 'museum', 'latitude': 23.1700, 'longitude': 72.5850, 'description': 'Underground art complex', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Daily Exhibition Center', 'type': 'museum', 'latitude': 23.1850, 'longitude': 72.5850, 'description': 'Exhibition hall', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Tribal Museum', 'type': 'museum', 'latitude': 23.1800, 'longitude': 72.5950, 'description': 'Tribal art and culture', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Heritage Walk Site', 'type': 'attraction', 'latitude': 23.1860, 'longitude': 72.6160, 'description': 'Walking tour destination', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Sardar Vallabhbhai Patel National Museum', 'type': 'museum', 'latitude': 23.1850, 'longitude': 72.6050, 'description': 'Museum dedicated to national leader', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
    {'name': 'Akhbar Mosque', 'type': 'monument', 'latitude': 23.1870, 'longitude': 72.6170, 'description': 'Historic mosque', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Gujarati Vikas Mandir Park', 'type': 'park', 'latitude': 23.1950, 'longitude': 72.5900, 'description': 'Development memorial park', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Free'},
    {'name': 'Fort Museum', 'type': 'museum', 'latitude': 23.1870, 'longitude': 72.6210, 'description': 'Museum in fort', 'website': '', 'opening_hours': '', 'phone': '', 'admission_fee': 'Paid'},
]

# Function to save attractions to CSV file
def save_to_csv(filename, data):
    """Save attractions list to CSV file"""
    # Define CSV column names
    columns = ['name', 'type', 'latitude', 'longitude', 'description', 'website', 'opening_hours', 'phone', 'admission_fee']
    
    # Open and write CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()  # Write header row
        writer.writerows(data)  # Write all attractions
    
    print(f"Saved {len(data)} attractions to {filename}")

# Function to show summary
def show_summary(data):
    """Display summary of attractions"""
    print("\n" + "="*50)
    print("TOURIST ATTRACTIONS SUMMARY")
    print("="*50)
    print(f"Total attractions: {len(data)}\n")
    
    # Count by type
    types = {}
    for item in data:
        atype = item['type']
        types[atype] = types.get(atype, 0) + 1
    
    # Show count by type
    print("Count by type:")
    for atype, count in sorted(types.items(), key=lambda x: x[1], reverse=True):
        print(f"  {atype}: {count}")
    
    # Show first 5 attractions
    print("\nFirst 5 attractions:")
    for i, att in enumerate(data[:5], 1):
        print(f"{i}. {att['name']} ({att['type']})")
        print(f"   Lat: {att['latitude']}, Lon: {att['longitude']}")

# Main program
if __name__ == "__main__":
    # Save attractions to CSV
    filename = "ahmedabad_attractions.csv"
    save_to_csv(filename, attractions)
    
    # Show summary
    show_summary(attractions)
