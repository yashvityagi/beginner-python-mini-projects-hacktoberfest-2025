"""
Demo script to show the news scraper in action

This script provides a quick demonstration of the scraper capabilities.
"""

from news_scraper import NewsHeadlineScraper
import time


def demo_scraper():
    """Demonstrate the news scraper functionality"""
    print("News Headlines Web Scraper Demo")
    print("=" * 50)
    print("This demo will attempt to scrape headlines from news websites.")
    print("Note: Results may vary based on internet connection and website availability.\n")
    
    # Initialize scraper
    scraper = NewsHeadlineScraper()
    
    print("Initializing scraper...")
    print(f"Configured news sources: {list(scraper.news_sources.keys())}")
    print()
    
    # Try scraping from each source individually
    all_headlines = []
    
    for source in scraper.news_sources:
        print(f"Attempting to scrape from {source.upper()}...")
        try:
            headlines = scraper.extract_headlines_from_source(source)
            if headlines:
                print(f"✓ Successfully scraped {len(headlines)} headlines from {source}")
                all_headlines.extend(headlines)
                
                # Show first headline as sample
                if headlines:
                    print(f"  Sample: {headlines[0]['headline'][:80]}...")
            else:
                print(f"✗ No headlines scraped from {source}")
        except Exception as e:
            print(f"✗ Error scraping from {source}: {str(e)}")
        
        print()
        time.sleep(1)  # Brief pause between sources
    
    # Summary
    print(f"Demo completed!")
    print(f"Total headlines collected: {len(all_headlines)}")
    
    if all_headlines:
        print("\nSample headlines:")
        scraper.headlines = all_headlines
        scraper.display_headlines(5)
        
        # Save demo results
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        json_file = f"demo_headlines_{timestamp}.json"
        csv_file = f"demo_headlines_{timestamp}.csv"
        
        scraper.save_to_json(json_file)
        scraper.save_to_csv(csv_file)
        
        print(f"\nDemo results saved to:")
        print(f"- {json_file}")
        print(f"- {csv_file}")
    else:
        print("\nNo headlines were successfully scraped.")
        print("This could be due to:")
        print("- Internet connectivity issues")
        print("- Website structure changes")
        print("- Rate limiting or blocking")
        print("\nTry running the scraper again later.")


if __name__ == "__main__":
    try:
        demo_scraper()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\nDemo error: {str(e)}")
        print("Check scraper.log for detailed error information.")