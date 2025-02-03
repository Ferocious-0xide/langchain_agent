from typing import Any, Dict, List
from anthropic import Anthropic
from .base import Agent
from src.config.settings import settings

class SummarizationAgent(Agent):
    """Agent for summarizing articles using Anthropic's API."""
    
    def __init__(self, name: str, config: Dict = None):
        super().__init__(name, config)
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        self.model = self.config.get('model', 'claude-3-opus-20240229')
        self.max_tokens = self.config.get('max_tokens', 150)
        
    def perceive(self, articles: List[Dict[str, str]]) -> None:
        """
        Store the articles for summarization.
        
        Args:
            articles (List[Dict[str, str]]): List of articles to summarize
        """
        self.state['articles'] = articles
        self.logger.info(f"Preparing to summarize {len(articles)} articles")

    def _create_summary_prompt(self, article: Dict[str, str]) -> str:
        """
        Create a prompt for article summarization.
        
        Args:
            article (Dict[str, str]): Article to summarize
            
        Returns:
            str: Formatted prompt
        """
        return f"""Please summarize the following article concisely and objectively.

Title: {article['title']}
Source: {article['source']}
Content: {article['content']}

Provide a clear, factual summary that captures the main points and key findings."""

    def decide(self) -> List[Dict[str, Any]]:
        """
        Generate summaries for all articles.
        
        Returns:
            List[Dict[str, Any]]: List of articles with summaries
        """
        summarized_articles = []
        
        for article in self.state['articles']:
            try:
                prompt = self._create_summary_prompt(article)
                
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=self.max_tokens,
                    temperature=0.5,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )
                
                summary = response.content[0].text
                
                summarized_article = {
                    **article,
                    'summary': summary
                }
                summarized_articles.append(summarized_article)
                self.logger.info(f"Successfully summarized article: {article['title']}")
                
            except Exception as e:
                self.logger.error(f"Error summarizing article {article['title']}: {str(e)}")
                # Include the article but note the summarization failure
                summarized_article = {
                    **article,
                    'summary': f"Error generating summary: {str(e)}"
                }
                summarized_articles.append(summarized_article)
                
        return summarized_articles

    def act(self) -> List[Dict[str, Any]]:
        """
        Process and return the summarized articles.
        
        Returns:
            List[Dict[str, Any]]: Processed articles with summaries
        """
        summarized_articles = self.decide()
        self.logger.info(f"Completed summarization of {len(summarized_articles)} articles")
        return summarized_articles