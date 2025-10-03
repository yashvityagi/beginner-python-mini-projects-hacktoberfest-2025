# Simple News Headlines Web Scraper

A beginner-friendly web scraper built with Python that extracts news headlines from multiple popular news websites including BBC, Reuters, and CNN. The scraper uses BeautifulSoup for HTML parsing and provides clean, structured output in both JSON and CSV formats.

## Features

- **Multi-source scraping**: Scrapes headlines from BBC, Reuters, and CNN
- **Respectful scraping**: Implements delays between requests and proper headers
- **Multiple output formats**: Saves results in JSON and CSV formats
- **Error handling**: Robust error handling with logging
- **Configurable**: Easy to add new news sources
- **Production-ready**: Includes proper logging, error handling, and rate limiting

## Project Structure

```
Spartan1-1-7-make-a-simple-web-scraper-for-news-headlines/
├── news_scraper.py          # Main scraper implementation
├── demo.py                 # Quick demo script
├── example.py              # Usage examples
├── test_scraper.py         # Unit tests
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── scraper.log           # Log file (created when running)
```

## Installation

1. **Clone or download the project**
   ```bash
   cd src/Spartan1-1-7-make-a-simple-web-scraper-for-news-headlines/
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### Quick Demo

For a quick demonstration of the scraper:

```bash
python demo.py
```

This will attempt to scrape from all configured sources and show the results.

### Basic Usage

Run the scraper with default settings:

```bash
python news_scraper.py
```

This will:
- Scrape headlines from all configured news sources
- Display the top 15 headlines in the console
- Save results to timestamped JSON and CSV files
- Create a log file with scraping details

### Using as a Python Module

```python
from news_scraper import NewsHeadlineScraper

# Initialize the scraper
scraper = NewsHeadlineScraper()

# Scrape headlines from all sources
headlines = scraper.scrape_all_sources()

# Display headlines
scraper.display_headlines(10)

# Save to files
scraper.save_to_json("my_headlines.json")
scraper.save_to_csv("my_headlines.csv")

# Get headlines from specific source
bbc_headlines = scraper.get_headlines_by_source("bbc")
```

## Sample Output

```
News Headlines Web Scraper
==================================================
Scraping news headlines...
2025-10-03 10:30:15 - INFO - Fetching: https://www.bbc.com/news
2025-10-03 10:30:17 - INFO - Extracted 18 headlines from bbc
2025-10-03 10:30:19 - INFO - Fetching: https://www.reuters.com
2025-10-03 10:30:21 - INFO - Extracted 15 headlines from reuters
2025-10-03 10:30:23 - INFO - Fetching: https://edition.cnn.com
2025-10-03 10:30:25 - INFO - Extracted 12 headlines from cnn
2025-10-03 10:30:25 - INFO - Total headlines scraped: 45

=== TOP 15 NEWS HEADLINES ===

 1. [BBC] Breaking: Major climate summit begins in Dubai
    Link: https://www.bbc.com/news/science-environment-67123456

 2. [REUTERS] Global markets rise on inflation data
    Link: https://www.reuters.com/markets/global-markets-rise-123456

 3. [CNN] Tech giant announces new AI breakthrough
    Link: https://edition.cnn.com/2025/10/03/tech/ai-breakthrough

Results saved to:
- JSON: news_headlines_20251003_103025.json
- CSV: news_headlines_20251003_103025.csv

Summary by source:
- BBC: 18 headlines
- REUTERS: 15 headlines
- CNN: 12 headlines
```

## Configuration

### Adding New News Sources

To add a new news source, modify the `news_sources` dictionary in the `NewsHeadlineScraper` class:

```python
self.news_sources = {
    'your_source': {
        'url': 'https://example-news-site.com',
        'headline_selector': '.headline-class',  # CSS selector for headlines
        'link_selector': '.link-class'           # CSS selector for links
    }
}
```

### Customizing Output

The scraper supports various customization options:

- **Limit headlines per source**: Modify the slice `[:20]` in `extract_headlines_from_source()`
- **Change delay between requests**: Modify `time.sleep(2)` in `scrape_all_sources()`
- **Custom file names**: Pass filename parameters to `save_to_json()` and `save_to_csv()`

## Error Handling

The scraper includes comprehensive error handling:

- **Network errors**: Handles connection timeouts and HTTP errors
- **Parsing errors**: Graceful handling of malformed HTML
- **File I/O errors**: Proper error reporting for file operations
- **Logging**: All activities are logged to `scraper.log`

## Dependencies

- **beautifulsoup4**: HTML parsing and web scraping
- **requests**: HTTP library for making web requests
- **lxml**: Fast XML and HTML parser (optional but recommended)

## Best Practices Implemented

1. **Respectful scraping**: 2-second delays between requests
2. **Proper headers**: Uses realistic browser User-Agent
3. **Error resilience**: Continues scraping even if one source fails
4. **Data validation**: Filters out empty or very short headlines
5. **Logging**: Comprehensive logging for debugging and monitoring
6. **Clean code**: Well-documented with type hints and docstrings

## Limitations

- **Dynamic content**: May not work with JavaScript-heavy news sites
- **Rate limiting**: Some sites may block requests if scraping too frequently
- **Selector changes**: News sites may change their HTML structure over time

## Legal and Ethical Considerations

- Always respect robots.txt files
- Don't overload servers with too many requests
- Use scraped data responsibly and in accordance with site terms of service
- Consider using official APIs when available

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Author

**Spartan1-1-7**  
Created as part of Hacktoberfest 2025

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **No headlines scraped**: Check internet connection and verify news sites are accessible

3. **SSL errors**: Some networks may have SSL issues. Try running with:
   ```python
   import ssl
   ssl._create_default_https_context = ssl._create_unverified_context
   ```

4. **Empty output**: News site selectors may have changed. Check logs for specific errors.

### Getting Help

If you encounter issues:
1. Check the `scraper.log` file for detailed error messages
2. Verify all dependencies are correctly installed
3. Test with a single news source first
4. Check if the news websites are accessible from your network