import sys
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

from src.agents.input import InputAgent
from src.agents.retrieval import RetrievalAgent
from src.agents.summarization import SummarizationAgent
from src.core.workflow import Workflow
from src.config.settings import settings

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def setup_agents() -> Dict[str, Any]:
    """Create and configure the agents."""
    logger.info("Setting up agents...")
    agents = {
        'input': InputAgent(
            name="InputAgent",
            config={'min_length': 3, 'max_length': 100}
        ),
        'retrieval': RetrievalAgent(
            name="RetrievalAgent",
            config={'max_articles': 5}
        ),
        'summarization': SummarizationAgent(
            name="SummarizationAgent",
            config={
                'model': 'claude-3-opus-20240229',
                'max_tokens': 150
            }
        )
    }
    logger.info("Agents setup complete")
    return agents

def save_results(topic: str, results: list) -> str:
    """Save results to a JSON file."""
    logger.info("Saving results...")
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"research_{topic.replace(' ', '_')}_{timestamp}.json"
    filepath = output_dir / filename
    
    with filepath.open('w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    logger.info(f"Results saved to {filepath}")
    return str(filepath)

def main():
    """Run the research workflow."""
    try:
        if len(sys.argv) < 2:
            print("Usage: python main.py 'research topic'")
            sys.exit(1)
            
        topic = ' '.join(sys.argv[1:])
        logger.info(f"Starting research on topic: {topic}")
        print(f"\n🔍 Researching topic: {topic}")
        
        # Validate environment
        if not settings.validate()[0]:
            logger.error("Invalid configuration")
            print("❌ Error: Please check your .env file and make sure all required API keys are set")
            sys.exit(1)
            
        # Setup and run workflow
        agents = setup_agents()
        workflow = Workflow(list(agents.values()))
        logger.info("Starting workflow execution")
        results = workflow.run(topic)
        
        # Save results
        output_file = save_results(topic, results)
        
        print(f"\n✅ Research complete! Results saved to: {output_file}")
        
        # Print summary
        print("\n📊 Summary:")
        print(f"Topic: {topic}")
        print(f"Articles processed: {len(results)}")
        print("\n📑 Article Summaries:")
        for idx, article in enumerate(results, 1):
            print(f"\n{idx}. {article['title']}")
            print(f"Source: {article['source']}")
            print(f"Summary: {article['summary'][:200]}...")
            
    except Exception as e:
        logger.error(f"Error in main: {str(e)}", exc_info=True)
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()