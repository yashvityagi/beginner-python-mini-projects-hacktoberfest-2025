"""
Example usage of the News Headlines Web Scraper

This script demonstrates various ways to use the NewsHeadlineScraper class.
"""

from news_scraper import NewsHeadlineScraper
import json


def example_basic_usage():
    """Basic scraping example"""
    print("=== Basic Usage Example ===")
    
    scraper = NewsHeadlineScraper()
    headlines = scraper.scrape_all_sources()
    
    if headlines:
        print(f"Successfully scraped {len(headlines)} headlines")
        scraper.display_headlines(5)  # Show top 5
    else:
        print("No headlines were scraped")


def example_single_source():
    """Scrape from a single news source"""
    print("\n=== Single Source Example ===")
    
    scraper = NewsHeadlineScraper()
    bbc_headlines = scraper.extract_headlines_from_source('bbc')
    
    if bbc_headlines:
        print(f"BBC Headlines ({len(bbc_headlines)}):")
        for i, headline in enumerate(bbc_headlines[:3], 1):
            print(f"{i}. {headline['headline']}")


def example_custom_output():
    """Custom file output example"""
    print("\n=== Custom Output Example ===")
    
    scraper = NewsHeadlineScraper()
    headlines = scraper.scrape_all_sources()
    
    if headlines:
        # Save with custom filenames
        json_file = scraper.save_to_json("custom_headlines.json")
        csv_file = scraper.save_to_csv("custom_headlines.csv")
        
        print(f"Saved to custom files: {json_file}, {csv_file}")


def example_filter_by_source():
    """Filter headlines by source"""
    print("\n=== Filter by Source Example ===")
    
    scraper = NewsHeadlineScraper()
    all_headlines = scraper.scrape_all_sources()
    
    if all_headlines:
        # Get headlines from each source
        for source in ['bbc', 'reuters', 'cnn']:
            source_headlines = scraper.get_headlines_by_source(source)
            print(f"{source.upper()}: {len(source_headlines)} headlines")


if __name__ == "__main__":
    print("News Scraper Examples")
    print("=" * 50)
    
    try:
        example_basic_usage()
        example_single_source()
        example_custom_output()
        example_filter_by_source()
        
    except KeyboardInterrupt:
        print("\nExamples interrupted by user")
    except Exception as e:
        print(f"Error running examples: {e}")