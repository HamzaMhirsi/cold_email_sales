"""
Country to language mapping for multi-language email campaigns
"""

# Country to language mapping
COUNTRY_LANGUAGE_MAP = {
    # English-speaking countries
    "United States": "english",
    "United Kingdom": "english", 
    "Canada": "english",  # Default to English for Canada (can be overridden)
    "Australia": "english",
    "New Zealand": "english",
    "Ireland": "english",
    "South Africa": "english",
    "India": "english",
    "Singapore": "english",
    "Malaysia": "english",
    "Philippines": "english",
    "Nigeria": "english",
    "Kenya": "english",
    "Ghana": "english",
    "Zimbabwe": "english",
    "Botswana": "english",
    "Malta": "english",
    
    # Arabic-speaking countries
    "Saudi Arabia": "arabic",
    "United Arab Emirates": "arabic",
    "Egypt": "arabic",
    "Morocco": "arabic",
    "Algeria": "arabic",
    "Tunisia": "arabic",
    "Libya": "arabic",
    "Sudan": "arabic",
    "Jordan": "arabic",
    "Lebanon": "arabic",
    "Syria": "arabic",
    "Iraq": "arabic",
    "Kuwait": "arabic",
    "Qatar": "arabic",
    "Bahrain": "arabic",
    "Oman": "arabic",
    "Yemen": "arabic",
    "Palestine": "arabic",
    
    # French-speaking countries
    "France": "french",
    "Belgium": "french",
    "Switzerland": "french",
    "Luxembourg": "french",
    "Monaco": "french",
    "Senegal": "french",
    "Mali": "french",
    "Burkina Faso": "french",
    "Niger": "french",
    "Chad": "french",
    "Central African Republic": "french",
    "Cameroon": "french",
    "Equatorial Guinea": "french",
    "Gabon": "french",
    "Republic of the Congo": "french",
    "Democratic Republic of the Congo": "french",
    "Madagascar": "french",
    "Comoros": "french",
    "Djibouti": "french",
    "Ivory Coast": "french",
    "Côte d'Ivoire": "french",
    "Guinea": "french",
    "Togo": "french",
    "Benin": "french",
    "Rwanda": "french",
    "Burundi": "french",
    "Vanuatu": "french",
    "French Polynesia": "french",
    "New Caledonia": "french",
    "Haiti": "french",
    "Seychelles": "french",
}

def get_language_from_location(location):
    """
    Extract language from location string based on country mapping
    """
    if not location:
        return "english"
    
    location = location.strip()
    
    # Check for exact country matches
    for country, language in COUNTRY_LANGUAGE_MAP.items():
        if country.lower() in location.lower():
            return language
    
    # Check for common location patterns
    location_lower = location.lower()
    
    # Arabic regions/cities
    arabic_indicators = [
        "الرياض", "دبي", "الإمارات", "السعودية", "مصر", "الاسكندرية",
        "riyadh", "dubai", "abu dhabi", "doha", "kuwait", "cairo",
        "casablanca", "rabat", "tunis", "algiers", "baghdad", "amman"
    ]
    
    for indicator in arabic_indicators:
        if indicator in location_lower:
            return "arabic"
    
    # French regions/cities
    french_indicators = [
        "paris", "lyon", "marseille", "toulouse", "nice", "nantes",
        "strasbourg", "montpellier", "bordeaux", "lille", "rennes",
        "brussels", "geneva", "lausanne", "dakar", "abidjan",
        "kinshasa", "brazzaville", "yaoundé", "bamako", "ouagadougou"
    ]
    
    for indicator in french_indicators:
        if indicator in location_lower:
            return "french"
    
    # Default to English
    return "english"

def detect_language_from_csv_row(row):
    """
    Detect language from CSV row data
    """
    # Get location from the CSV (column index 6)
    location = row[6] if len(row) > 6 else ""
    return get_language_from_location(location)
