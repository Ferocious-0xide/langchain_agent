from typing import List, Any, Optional, Dict
import logging
from datetime import datetime
import asyncio
from src.agents.base import Agent

class Workflow:
    """
    Orchestrates the execution of multiple agents in a workflow.
    
    Attributes:
        agents (List[Agent]): List of agents in the workflow
        logger (logging.Logger): Logger instance for the workflow
        name (str): Name of the workflow
        state (Dict): Current state of the workflow
    """
    
    def __init__(self, 
                 agents: List[Agent], 
                 name: str = "default_workflow",
                 config: Optional[Dict] = None):
        """
        Initialize the workflow with a list of agents.
        
        Args:
            agents (List[Agent]): List of agents to execute in sequence
            name (str): Name of the workflow
            config (Dict, optional): Configuration for the workflow
        """
        self.agents = agents
        self.name = name
        self.config = config or {}
        self.state = {}
        self.logger = self._setup_logger()
        
    def _setup_logger(self) -> logging.Logger:
        """Set up logging for the workflow."""
        logger = logging.getLogger(f"workflow.{self.name}")
        logger.setLevel(logging.INFO)
        return logger
        
    def run(self, input_data: Any) -> Any:
        """
        Execute the workflow sequentially.
        
        Args:
            input_data: Initial input data for the workflow
            
        Returns:
            Result from the final agent in the workflow
        """
        try:
            self.logger.info(f"Starting workflow execution at {datetime.now()}")
            current_data = input_data
            
            for agent in self.agents:
                self.logger.info(f"Executing agent: {agent.name}")
                current_data = agent.run(current_data)
                self.state[agent.name] = agent.get_state()
                
            self.logger.info("Workflow completed successfully")
            return current_data
            
        except Exception as e:
            self.logger.error(f"Workflow failed: {str(e)}")
            raise
            
    async def run_async(self, input_data: Any) -> Any:
        """
        Execute the workflow with support for async agents.
        
        Args:
            input_data: Initial input data for the workflow
            
        Returns:
            Result from the final agent in the workflow
        """
        try:
            self.logger.info(f"Starting async workflow execution at {datetime.now()}")
            current_data = input_data
            
            for agent in self.agents:
                if hasattr(agent, 'run_async'):
                    current_data = await agent.run_async(current_data)
                else:
                    current_data = agent.run(current_data)
                self.state[agent.name] = agent.get_state()
                
            self.logger.info("Async workflow completed successfully")
            return current_data
            
        except Exception as e:
            self.logger.error(f"Async workflow failed: {str(e)}")
            raise
            
    def reset(self) -> None:
        """Reset the workflow and all agents to their initial state."""
        self.state = {}
        for agent in self.agents:
            agent.reset()
        self.logger.info("Workflow reset completed")
        
    def get_state(self) -> Dict:
        """
        Get the current state of the workflow.
        
        Returns:
            Dict containing the workflow's current state
        """
        return {
            'workflow_name': self.name,
            'agent_states': self.state.copy()
        }
        
    def __str__(self) -> str:
        """String representation of the workflow."""
        return f"Workflow(name={self.name}, agents={len(self.agents)})"