from typing import Any, Dict
from .base import Agent

class InputAgent(Agent):
    """Agent for processing and validating input topics."""
    
    def __init__(self, name: str, config: Dict = None):
        super().__init__(name, config)
        self.min_length = self.config.get('min_length', 3)
        self.max_length = self.config.get('max_length', 100)

    def perceive(self, input_data: str) -> None:
        """
        Process the input topic string.
        
        Args:
            input_data (str): The research topic
        """
        self.logger.info(f"Received input topic: {input_data}")
        if not isinstance(input_data, str):
            raise ValueError("Input must be a string")
        self.state['topic'] = input_data.strip()

    def decide(self) -> bool:
        """
        Validate the input topic.
        
        Returns:
            bool: True if topic is valid
        """
        topic = self.state.get('topic', '')
        
        if len(topic) < self.min_length:
            raise ValueError(f"Topic too short. Minimum length is {self.min_length}")
        
        if len(topic) > self.max_length:
            raise ValueError(f"Topic too long. Maximum length is {self.max_length}")
            
        self.logger.info(f"Topic '{topic}' validated successfully")
        return True

    def act(self) -> str:
        """
        Return the processed topic.
        
        Returns:
            str: The validated topic
        """
        self.decide()  # Validate before returning
        return self.state['topic']