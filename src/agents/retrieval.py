from typing import Any, Dict, List
import requests
from datetime import datetime, timedelta
from .base import Agent
from src.config.settings import settings

class RetrievalAgent(Agent):
    """Agent for retrieving articles from News API."""
    
    def __init__(self, name: str, config: Dict = None):
        super().__init__(name, config)
        self.api_key = settings.NEWS_API_KEY
        self.base_url = "https://newsapi.org/v2/everything"
        self.max_articles = self.config.get('max_articles', 5)
        
    def perceive(self, topic: str) -> None:
        """
        Store the topic for article retrieval.
        
        Args:
            topic (str): The research topic
        """
        self.state['topic'] = topic
        self.logger.info(f"Preparing to retrieve articles for topic: {topic}")

    def decide(self) -> requests.Response:
        """
        Construct and execute the API request.
        
        Returns:
            requests.Response: The API response
        """
        # Calculate date range for last 7 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        
        params = {
            'q': self.state['topic'],
            'apiKey': self.api_key,
            'language': 'en',
            'sortBy': 'relevancy',
            'pageSize': self.max_articles,
            'from': start_date.strftime('%Y-%m-%d'),
            'to': end_date.strftime('%Y-%m-%d')
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error retrieving articles: {str(e)}")
            raise

    def act(self) -> List[Dict[str, str]]:
        """
        Process the API response and return formatted articles.
        
        Returns:
            List[Dict[str, str]]: List of processed articles
        """
        response = self.decide()
        articles = response.json().get('articles', [])
        
        processed_articles = []
        for article in articles[:self.max_articles]:
            processed_article = {
                'title': article.get('title', ''),
                'url': article.get('url', ''),
                'content': article.get('content', article.get('description', '')),
                'source': article.get('source', {}).get('name', 'Unknown'),
                'published_at': article.get('publishedAt', '')
            }
            processed_articles.append(processed_article)
            
        self.logger.info(f"Retrieved {len(processed_articles)} articles")
        return processed_articles