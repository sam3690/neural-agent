"""Neural Agent - A Groq-powered football analysis agent."""

import sys
from pathlib import Path
# import neural_agent.reflection_pattern
import reflection_pattern

# Add the src directory to Python path
src_path = Path(__file__).parent.parent
sys.path.insert(0, str(src_path))

# Import the reflection_pattern module to execute it

def main():
    """Main entry point for the neural agent."""
    print("Starting Neural Agent...")
    # The reflection_pattern module will execute automatically when imported
    # since your original code runs at module level

if __name__ == "__main__":
    main()