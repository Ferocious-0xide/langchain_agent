🤖 Agentic Workflow Framework
<p align="center">
  <img src="assets/images/Agent_image.png" alt="Agent Logo">
</p>
<p align="center">
  A powerful, flexible framework for building autonomous agent-based workflows in Python.
</p>
<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python Version"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style: Black"></a>
</p>
✨ Overview
Build intelligent workflows using specialized agents that can perceive, decide, and act autonomously. Perfect for automating complex tasks and building AI-powered applications.
🚀 Features

🧠 Base agent framework with perceive-decide-act cycle
🔌 Modular agent system for easy extension
🛠️ Built-in agents for common tasks:

📥 Input processing
🌐 Web content retrieval
📝 Text summarization
💾 File storage


🎭 Workflow orchestration system
⚡ Async support for parallel processing
🛡️ Comprehensive error handling
🤝 Easy integration with Claude and other APIs

📊 Project Design

<p align="center">
  <img src="assets/images/Agent_mermaid.png" alt="Agent Mermaid Diagram">
</p>

## 📁 Project Structure

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

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.8+
- Virtual environment (recommended)
- OpenAI API key
- News API key (for retrieval agent)

### 💻 Installation

1. Clone this awesome repository:
```bash
git clone https://github.com/yourusername/agentic-workflow.git
cd agentic-workflow
```

2. Create your virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the magic dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
```bash
export OPENAI_API_KEY="your_openai_api_key"
export NEWS_API_KEY="your_news_api_key"
```

## 🏃‍♂️ Quick Start

Here's a simple example to get you started with creating and running a research workflow:

```python
from src.agents import InputAgent, RetrievalAgent, SummarizationAgent
from src.core.workflow import Workflow

# Create your agent squad 🤖
input_agent = InputAgent(name="InputAgent")
retrieval_agent = RetrievalAgent(name="RetrievalAgent")
summarization_agent = SummarizationAgent(name="SummarizationAgent")

# Assemble the dream team
agents = [input_agent, retrieval_agent, summarization_agent]
workflow = Workflow(agents)

# Let them loose!
topic = "AI in Healthcare"
results = workflow.run(topic)
```

## 🛠️ Creating Custom Agents

Want to create your own agent? It's as easy as inheriting from our base Agent class:

```python
from src.agents.base import Agent

class CustomAgent(Agent):
    def perceive(self, input_data):
        self.data = input_data

    def decide(self):
        # Add your galaxy-brain decision logic here
        return processed_data

    def act(self):
        result = self.decide()
        return result
```

## 🧪 Running Tests

Keep your code rock-solid with our test suite:

```bash
pytest tests/
```

## 🤝 Contributing

We love contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🌱 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💫 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 🚀 Push to the branch (`git push origin feature/amazing-feature`)
5. 🎉 Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

Special thanks to:
- 🤖 OpenAI for their amazing API
- ⛓️ Langchain for workflow inspiration
- 📰 News API for content retrieval capabilities

## 🤔 Need Help?

Have questions? Check out our [documentation](docs/) or open an issue!

---

<div align="center">
Made with ❤️ by the Agentic Workflow Team
</div>