# verify_setup.py
import os
import sys
from pathlib import Path

def verify_setup():
    print("🔍 Verifying project setup...")
    
    # Check project structure
    required_dirs = ['src', 'src/agents', 'src/core', 'src/config', 'output']
    required_files = [
        'src/__init__.py',
        'src/agents/__init__.py',
        'src/core/__init__.py',
        'src/config/__init__.py',
        '.env',
        'requirements.txt'
    ]
    
    # Check directories
    print("\nChecking directories:")
    for dir_path in required_dirs:
        path = Path(dir_path)
        if path.exists() and path.is_dir():
            print(f"✅ {dir_path} exists")
        else:
            print(f"❌ {dir_path} missing")
            
    # Check files
    print("\nChecking files:")
    for file_path in required_files:
        path = Path(file_path)
        if path.exists() and path.is_file():
            print(f"✅ {file_path} exists")
        else:
            print(f"❌ {file_path} missing")
            
    # Check .env
    if Path('.env').exists():
        print("\nChecking .env configuration:")
        required_vars = ['ANTHROPIC_API_KEY', 'NEWS_API_KEY']
        for var in required_vars:
            if os.getenv(var):
                print(f"✅ {var} is set")
            else:
                print(f"❌ {var} is missing")
    
    # Check Python packages
    print("\nChecking required packages:")
    required_packages = ['anthropic', 'requests']
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is missing")

if __name__ == "__main__":
    verify_setup()