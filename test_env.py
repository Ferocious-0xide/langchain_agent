from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Check keys
print("Testing environment variables:")
print(f"ANTHROPIC_API_KEY exists: {'ANTHROPIC_API_KEY' in os.environ}")
if 'ANTHROPIC_API_KEY' in os.environ:
    key = os.environ['ANTHROPIC_API_KEY']
    print(f"ANTHROPIC_API_KEY length: {len(key)}")
    print(f"ANTHROPIC_API_KEY starts with: {key[:7]}...")

print(f"\nNEWS_API_KEY exists: {'NEWS_API_KEY' in os.environ}")
if 'NEWS_API_KEY' in os.environ:
    key = os.environ['NEWS_API_KEY']
    print(f"NEWS_API_KEY length: {len(key)}")
    print(f"NEWS_API_KEY starts with: {key[:4]}...")

# Check installed packages
try:
    import anthropic
    print("\nanthropic package is installed")
except ImportError:
    print("\nanthropic package is NOT installed")

try:
    import requests
    print("requests package is installed")
except ImportError:
    print("requests package is NOT installed")