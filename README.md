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

📊 Project Structure
graph TD
    A[Agentic Workflow Project] --> B[bin]
    A --> AS[assets]
    A --> C[docs]
    A --> D[notebooks]
    A --> E[src]
    A --> F[tests]
    A --> G[requirements.txt]
    A --> H[README.md]

    AS --> AS1[images]
    AS1 --> AS1_1[agent-logo.png]

    B --> B1[start-jupyter]

    C --> C1[agents.md]
    C --> C2[workflows.md]
    C --> C3[examples.md]

    D --> D1[example.ipynb]

    E --> E1[agents]
    E --> E2[config]
    E --> E3[core]
    E --> E4[utils]

    E1 --> E1_1[base.py]
    E1 --> E1_2[input.py]
    E1 --> E1_3[retrieval.py]
    E1 --> E1_4[summarization.py]
    E1 --> E1_5[storage.py]
    E1 --> E1_6[__init__.py]

    E2 --> E2_1[settings.py]
    E2 --> E2_2[__init__.py]

    E3 --> E3_1[workflow.py]
    E3 --> E3_2[__init__.py]

    E4 --> E4_1[async_helpers.py]
    E4 --> E4_2[logging.py]
    E4 --> E4_3[__init__.py]

    F --> F1[test_agents]
    F --> F2[test_workflows]
    F --> F3[conftest.py]
    F --> F4[__init__.py]

    style A fill:#f9f,stroke:#333,stroke-width:4px
    style AS fill:#bbf,stroke:#333,stroke-width:2px
    style E1 fill:#bbf,stroke:#333,stroke-width:2px
    style E2 fill:#bbf,stroke:#333,stroke-width:2px
    style E3 fill:#bbf,stroke:#333,stroke-width:2px
    style E4 fill:#bbf,stroke:#333,stroke-width:2px

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