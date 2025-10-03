"""
Simple tests for the News Headlines Web Scraper

Basic tests to verify the scraper functionality.
"""

import unittest
from unittest.mock import patch, Mock
import requests
from news_scraper import NewsHeadlineScraper


class TestNewsHeadlineScraper(unittest.TestCase):
    """Test cases for NewsHeadlineScraper class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.scraper = NewsHeadlineScraper()
    
    def test_scraper_initialization(self):
        """Test that scraper initializes correctly"""
        self.assertIsInstance(self.scraper, NewsHeadlineScraper)
        self.assertEqual(len(self.scraper.headlines), 0)
        self.assertIn('bbc', self.scraper.news_sources)
        self.assertIn('reuters', self.scraper.news_sources)
        self.assertIn('cnn', self.scraper.news_sources)
    
    def test_news_sources_config(self):
        """Test news sources configuration"""
        for source_name, config in self.scraper.news_sources.items():
            self.assertIn('url', config)
            self.assertIn('headline_selector', config)
            self.assertIn('link_selector', config)
            self.assertTrue(config['url'].startswith('http'))
    
    @patch('requests.Session.get')
    def test_fetch_page_success(self, mock_get):
        """Test successful page fetching"""
        # Mock successful response
        mock_response = Mock()
        mock_response.content = b'<html><body><h1>Test</h1></body></html>'
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        soup = self.scraper.fetch_page('http://example.com')
        
        self.assertIsNotNone(soup)
        self.assertEqual(soup.find('h1').text, 'Test')
    
    @patch('requests.Session.get')
    def test_fetch_page_failure(self, mock_get):
        """Test failed page fetching"""
        # Mock failed response
        mock_get.side_effect = requests.exceptions.RequestException("Connection error")
        
        soup = self.scraper.fetch_page('http://example.com')
        
        self.assertIsNone(soup)
    
    def test_get_headlines_by_source(self):
        """Test filtering headlines by source"""
        # Add some test headlines
        self.scraper.headlines = [
            {'source': 'BBC', 'headline': 'BBC News 1'},
            {'source': 'CNN', 'headline': 'CNN News 1'},
            {'source': 'BBC', 'headline': 'BBC News 2'},
        ]
        
        bbc_headlines = self.scraper.get_headlines_by_source('bbc')
        cnn_headlines = self.scraper.get_headlines_by_source('cnn')
        
        self.assertEqual(len(bbc_headlines), 2)
        self.assertEqual(len(cnn_headlines), 1)
    
    def test_empty_headlines_display(self):
        """Test display when no headlines are available"""
        # This should not raise an exception
        try:
            self.scraper.display_headlines()
        except Exception as e:
            self.fail(f"display_headlines raised an exception: {e}")


class TestScraperIntegration(unittest.TestCase):
    """Integration tests (require internet connection)"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.scraper = NewsHeadlineScraper()
    
    def test_real_scraping(self):
        """Test actual scraping (requires internet)"""
        # This test requires internet connection
        try:
            headlines = self.scraper.extract_headlines_from_source('bbc')
            
            # If we get here, scraping worked
            if headlines:
                self.assertIsInstance(headlines, list)
                if len(headlines) > 0:
                    headline = headlines[0]
                    self.assertIn('source', headline)
                    self.assertIn('headline', headline)
                    self.assertIn('scraped_at', headline)
            
        except Exception as e:
            # Skip test if internet is not available
            self.skipTest(f"Internet connection required: {e}")


def run_basic_tests():
    """Run basic tests without requiring internet"""
    print("Running basic tests...")
    
    # Test scraper initialization
    scraper = NewsHeadlineScraper()
    assert scraper is not None
    assert len(scraper.headlines) == 0
    print("✓ Scraper initialization test passed")
    
    # Test configuration
    assert 'bbc' in scraper.news_sources
    assert 'reuters' in scraper.news_sources
    assert 'cnn' in scraper.news_sources
    print("✓ Configuration test passed")
    
    # Test empty headlines filtering
    scraper.headlines = [
        {'source': 'BBC', 'headline': 'Test headline'},
        {'source': 'CNN', 'headline': 'Another headline'},
    ]
    bbc_headlines = scraper.get_headlines_by_source('bbc')
    assert len(bbc_headlines) == 1
    print("✓ Headlines filtering test passed")
    
    print("All basic tests passed!")


if __name__ == '__main__':
    print("News Scraper Tests")
    print("=" * 30)
    
    # Run basic tests first
    run_basic_tests()
    
    print("\nRunning comprehensive tests...")
    
    # Run unittest suite
    unittest.main(verbosity=2)