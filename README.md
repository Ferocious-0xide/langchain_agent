# Agentic Workflow Framework

A flexible and extensible framework for building autonomous agent-based workflows in Python.

## Overview

This framework provides a foundation for creating autonomous workflows using specialized agents that can perceive, decide, and act. It's designed to be modular, allowing teams to easily create new agents and workflows for various use cases.

## Features

- Base agent framework with perceive-decide-act cycle
- Modular agent system for easy extension
- Built-in agents for common tasks:
  - Input processing
  - Web content retrieval
  - Text summarization
  - File storage
- Workflow orchestration system
- Async support for parallel processing
- Comprehensive error handling
- Easy integration with OpenAI and other APIs

## Project Structure

```
├── README.md
├── bin
│   └── start-jupyter          # Script to start Jupyter environment
├── docs
│   ├── agents.md             # Documentation for available agents
│   ├── workflows.md          # Documentation for workflow creation
│   └── examples.md           # Example use cases and implementations
├── notebooks
│   └── example.ipynb         # Interactive examples and tutorials
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── agents
│   │   ├── __init__.py
│   │   ├── base.py          # Base agent class
│   │   ├── input.py         # Input processing agent
│   │   ├── retrieval.py     # Web content retrieval agent
│   │   ├── summarization.py # Content summarization agent
│   │   └── storage.py       # File storage agent
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py      # Configuration management
│   ├── core
│   │   ├── __init__.py
│   │   └── workflow.py      # Workflow orchestration
│   └── utils
│       ├── __init__.py
│       ├── async_helpers.py # Async utility functions
│       └── logging.py       # Logging configuration
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── test_agents
    └── test_workflows
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/agentic-workflow.git
cd agentic-workflow
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
export OPENAI_API_KEY="your_openai_api_key"
export NEWS_API_KEY="your_news_api_key"
```

## Quick Start

Here's a simple example of creating and running a research workflow:

```python
from src.agents import InputAgent, RetrievalAgent, SummarizationAgent
from src.core.workflow import Workflow

# Create agents
input_agent = InputAgent(name="InputAgent")
retrieval_agent = RetrievalAgent(name="RetrievalAgent")
summarization_agent = SummarizationAgent(name="SummarizationAgent")

# Create workflow
agents = [input_agent, retrieval_agent, summarization_agent]
workflow = Workflow(agents)

# Run workflow
topic = "AI in Healthcare"
results = workflow.run(topic)
```

## Creating Custom Agents

To create a custom agent, inherit from the base Agent class:

```python
from src.agents.base import Agent

class CustomAgent(Agent):
    def perceive(self, input_data):
        self.data = input_data

    def decide(self):
        # Add your decision logic here
        return processed_data

    def act(self):
        result = self.decide()
        return result
```

## Running Tests

Run the test suite using pytest:

```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for their API
- Langchain for workflow inspiration
- News API for content retrieval capabilities