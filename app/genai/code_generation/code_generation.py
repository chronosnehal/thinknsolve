#!/usr/bin/env python3
"""
Code Generation and Review System - Solution Implementation

Description: A system that generates code from natural language descriptions,
explains how code works, and provides code review feedback using LLM capabilities.
"""

# For GenAI problems ONLY - import LLM client
from app.utils.config import LLMClientManager

def generate_code(problem_description: str, language: str = "python", provider: str = "openrouter") -> str:
    """
    Generate code based on a problem description.

    Args:
        problem_description: Description of the coding problem
        language: Programming language for the solution
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Generated code
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": f"You are an expert {language} programmer. Generate clean, well-commented code that solves the given problem. Include error handling where appropriate."
        },
        {
            "role": "user",
            "content": f"Write {language} code to solve this problem:\n\n{problem_description}"
        }
    ]

    return client.chat(messages)

def explain_code(code: str, provider: str = "openrouter") -> str:
    """
    Explain how a piece of code works.

    Args:
        code: The code to explain
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Code explanation
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": "You are a helpful programming tutor. Explain code clearly and concisely, breaking down complex concepts."
        },
        {
            "role": "user",
            "content": f"Please explain how this code works:\n\n```\n{code}\n```"
        }
    ]

    return client.chat(messages)

def review_code(code: str, provider: str = "openrouter") -> str:
    """
    Review code for potential improvements and issues.

    Args:
        code: The code to review
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Code review with suggestions
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": "You are an experienced code reviewer. Analyze the code for potential bugs, performance issues, best practices, and suggest improvements."
        },
        {
            "role": "user",
            "content": f"Please review this code and provide feedback:\n\n```\n{code}\n```"
        }
    ]

    return client.chat(messages)

def main():
    """Main function to demonstrate the solution"""
    # Example problem
    problem = """
    Create a function that takes a list of numbers and returns the second largest number.
    Handle edge cases like empty lists or lists with duplicate numbers.
    """

    try:
        print("=== Code Generation and Review System ===\n")

        # Generate code
        print("Generating code...")
        code = generate_code(problem, "python", "openrouter")
        print("Generated Code:")
        print(code)
        print("\n" + "="*50 + "\n")

        # Explain the code
        print("Explaining code...")
        explanation = explain_code(code)
        print("Code Explanation:")
        print(explanation)
        print("\n" + "="*50 + "\n")

        # Review the code
        print("Reviewing code...")
        review = review_code(code)
        print("Code Review:")
        print(review)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
