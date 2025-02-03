from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
import logging
from datetime import datetime

class Agent(ABC):
    """
    Abstract base class for all agents in the workflow.
    
    Attributes:
        name (str): Name of the agent
        state (Dict): Current state of the agent
        logger (logging.Logger): Logger instance for the agent
    """
    
    def __init__(self, name: str, config: Optional[Dict] = None):
        """
        Initialize the agent with a name and optional configuration.
        
        Args:
            name (str): Name of the agent
            config (Dict, optional): Configuration dictionary for the agent
        """
        self.name = name
        self.state = {}
        self.config = config or {}
        self.logger = self._setup_logger()
        
    def _setup_logger(self) -> logging.Logger:
        """Set up logging for the agent."""
        logger = logging.getLogger(f"agent.{self.name}")
        logger.setLevel(logging.INFO)
        return logger
        
    @abstractmethod
    def perceive(self, input_data: Any) -> None:
        """
        Process input data and update agent's state.
        
        Args:
            input_data: Input data to be processed
        """
        self.logger.info(f"Perceiving input data at {datetime.now()}")
        
    @abstractmethod
    def decide(self) -> Any:
        """
        Make decisions based on the current state.
        
        Returns:
            Decision result based on the agent's logic
        """
        self.logger.info(f"Making decision at {datetime.now()}")
        
    @abstractmethod
    def act(self) -> Any:
        """
        Perform actions based on the decision.
        
        Returns:
            Result of the action
        """
        self.logger.info(f"Performing action at {datetime.now()}")
    
    def run(self, input_data: Any) -> Any:
        """
        Execute the full perceive-decide-act cycle.
        
        Args:
            input_data: Input data to be processed
            
        Returns:
            Result of the action phase
        """
        try:
            self.logger.info(f"Starting agent cycle for {self.name}")
            self.perceive(input_data)
            decision = self.decide()
            self.state['last_decision'] = decision
            result = self.act()
            self.state['last_result'] = result
            self.logger.info(f"Completed agent cycle for {self.name}")
            return result
        except Exception as e:
            self.logger.error(f"Error in agent cycle: {str(e)}")
            raise
            
    def reset(self) -> None:
        """Reset the agent's state."""
        self.state = {}
        self.logger.info(f"Reset agent state for {self.name}")
        
    def get_state(self) -> Dict:
        """
        Get the current state of the agent.
        
        Returns:
            Dict containing the agent's current state
        """
        return self.state.copy()

    def __str__(self) -> str:
        """String representation of the agent."""
        return f"{self.__class__.__name__}(name={self.name})"