#!/usr/bin/env python3
"""
Quick run script that sets the API key directly
"""

import os
import sys


GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def main():
    try:
        # Import and run the agent
        from agents import DocstringAgent
        
        print("🚀 Starting AI Docstring Generation Agent...")
        print("📁 Processing files in 'app/' directory...")
        
        agent = DocstringAgent()
        agent.process_folder()
        
        print("✅ Docstring generation completed!")
        print("📂 Check 'documented_app/' directory for results")
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("💡 Solution: Install dependencies with 'pip install -r requirements.txt'")
        return 1
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
