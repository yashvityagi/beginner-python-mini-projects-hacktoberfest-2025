"""
Simple News Headlines Web Scraper

A beginner-friendly web scraper that extracts news headlines from multiple
popular news websites using BeautifulSoup and requests.

Author: Spartan1-1-7
Created: October 2025
"""

import requests
from bs4 import BeautifulSoup
import time
import csv
import json
from datetime import datetime
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class NewsHeadlineScraper:
    """
    A simple web scraper for extracting news headlines from various news websites.
    """
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.headlines = []
        
        # News sources configuration
        self.news_sources = {
            'bbc': {
                'url': 'https://www.bbc.com/news',
                'headline_selector': 'h3[data-testid="card-headline"]',
                'link_selector': 'a[data-testid="internal-link"]'
            },
            'reuters': {
                'url': 'https://www.reuters.com',
                'headline_selector': '[data-testid="Heading"]',
                'link_selector': 'a[data-testid="Link"]'
            },
            'cnn': {
                'url': 'https://edition.cnn.com',
                'headline_selector': '.container__headline',
                'link_selector': '.container__link'
            }
        }
    
    def fetch_page(self, url: str, timeout: int = 10) -> Optional[BeautifulSoup]:
        """
        Fetch and parse a web page.
        
        Args:
            url (str): The URL to fetch
            timeout (int): Request timeout in seconds
            
        Returns:
            BeautifulSoup: Parsed HTML content or None if failed
        """
        try:
            logger.info(f"Fetching: {url}")
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching {url}: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error while fetching {url}: {str(e)}")
            return None
    
    def extract_headlines_from_source(self, source_name: str) -> List[Dict[str, str]]:
        """
        Extract headlines from a specific news source.
        
        Args:
            source_name (str): Name of the news source
            
        Returns:
            List[Dict]: List of headline dictionaries
        """
        if source_name not in self.news_sources:
            logger.warning(f"Unknown news source: {source_name}")
            return []
        
        source_config = self.news_sources[source_name]
        soup = self.fetch_page(source_config['url'])
        
        if not soup:
            return []
        
        headlines = []
        
        try:
            # Extract headlines using CSS selectors
            headline_elements = soup.select(source_config['headline_selector'])
            
            for element in headline_elements[:20]:  # Limit to top 20 headlines
                headline_text = element.get_text(strip=True)
                
                if headline_text and len(headline_text) > 10:  # Filter out short/empty headlines
                    # Try to find associated link
                    link = None
                    parent = element.find_parent('a')
                    if parent and parent.get('href'):
                        link = parent.get('href')
                        if link.startswith('/'):
                            link = source_config['url'] + link
                    
                    headline_data = {
                        'source': source_name.upper(),
                        'headline': headline_text,
                        'link': link,
                        'scraped_at': datetime.now().isoformat()
                    }
                    headlines.append(headline_data)
            
            logger.info(f"Extracted {len(headlines)} headlines from {source_name}")
            
        except Exception as e:
            logger.error(f"Error extracting headlines from {source_name}: {str(e)}")
        
        return headlines
    
    def scrape_all_sources(self) -> List[Dict[str, str]]:
        """
        Scrape headlines from all configured news sources.
        
        Returns:
            List[Dict]: Combined list of all headlines
        """
        all_headlines = []
        
        for source_name in self.news_sources:
            headlines = self.extract_headlines_from_source(source_name)
            all_headlines.extend(headlines)
            
            # Be respectful to servers - add delay between requests
            time.sleep(2)
        
        self.headlines = all_headlines
        logger.info(f"Total headlines scraped: {len(all_headlines)}")
        return all_headlines
    
    def save_to_json(self, filename: str = None) -> str:
        """
        Save headlines to JSON file.
        
        Args:
            filename (str): Output filename (optional)
            
        Returns:
            str: Filename of saved file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"news_headlines_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.headlines, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Headlines saved to {filename}")
            return filename
            
        except Exception as e:
            logger.error(f"Error saving to JSON: {str(e)}")
            raise
    
    def save_to_csv(self, filename: str = None) -> str:
        """
        Save headlines to CSV file.
        
        Args:
            filename (str): Output filename (optional)
            
        Returns:
            str: Filename of saved file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"news_headlines_{timestamp}.csv"
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                if self.headlines:
                    writer = csv.DictWriter(f, fieldnames=self.headlines[0].keys())
                    writer.writeheader()
                    writer.writerows(self.headlines)
            
            logger.info(f"Headlines saved to {filename}")
            return filename
            
        except Exception as e:
            logger.error(f"Error saving to CSV: {str(e)}")
            raise
    
    def display_headlines(self, limit: int = 10) -> None:
        """
        Display headlines in the console.
        
        Args:
            limit (int): Number of headlines to display
        """
        if not self.headlines:
            print("No headlines available. Run scrape_all_sources() first.")
            return
        
        print(f"\n=== TOP {min(limit, len(self.headlines))} NEWS HEADLINES ===\n")
        
        for i, headline in enumerate(self.headlines[:limit], 1):
            print(f"{i:2d}. [{headline['source']}] {headline['headline']}")
            if headline.get('link'):
                print(f"    Link: {headline['link']}")
            print()
    
    def get_headlines_by_source(self, source: str) -> List[Dict[str, str]]:
        """
        Filter headlines by news source.
        
        Args:
            source (str): News source name
            
        Returns:
            List[Dict]: Filtered headlines
        """
        return [h for h in self.headlines if h['source'].lower() == source.lower()]


def main():
    """
    Main function to demonstrate the news scraper functionality.
    """
    print("News Headlines Web Scraper")
    print("=" * 50)
    
    # Initialize scraper
    scraper = NewsHeadlineScraper()
    
    try:
        # Scrape headlines from all sources
        print("Scraping news headlines...")
        headlines = scraper.scrape_all_sources()
        
        if headlines:
            # Display headlines
            scraper.display_headlines(15)
            
            # Save to files
            json_file = scraper.save_to_json()
            csv_file = scraper.save_to_csv()
            
            print(f"\nResults saved to:")
            print(f"- JSON: {json_file}")
            print(f"- CSV: {csv_file}")
            
            # Show summary by source
            print(f"\nSummary by source:")
            for source in scraper.news_sources:
                source_headlines = scraper.get_headlines_by_source(source)
                print(f"- {source.upper()}: {len(source_headlines)} headlines")
        
        else:
            print("No headlines were scraped. Please check your internet connection and try again.")
    
    except KeyboardInterrupt:
        print("\nScraping interrupted by user.")
    except Exception as e:
        logger.error(f"Unexpected error in main: {str(e)}")
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()