# Code Generation and Review System

## Context
In modern software development, AI-powered code generation tools are becoming essential for productivity. This problem simulates building a system that can generate code from natural language descriptions, explain how the code works, and provide code review feedback.

## Problem Statement
Implement a system that leverages LLM capabilities to:
1. Generate source code for programming tasks based on natural language descriptions
2. Provide educational explanations of how generated code works
3. Perform lightweight code reviews with improvement suggestions
4. Support multiple programming languages and maintain clean prompt engineering practices

## Requirements
- Generate syntactically correct code in specified programming languages
- Provide clear, educational explanations suitable for learning
- Offer constructive code review feedback with specific improvement suggestions
- Handle edge cases and provide appropriate error handling in generated code
- Maintain separation of concerns between generation, explanation, and review functions
- Support configurable LLM providers (OpenAI, Azure OpenAI, OpenRouter)

## Assumptions
- LLM providers are configured correctly with valid API keys
- Generated code does not need to be executed automatically
- Focus is on prompt engineering clarity and code structure
- Network connectivity is available for API calls
- Input descriptions are reasonable in scope and complexity

## For Examiner

### Difficulty Level
Intermediate

### Expected Time
45-60 minutes

### Key Concepts Being Tested
- Prompt engineering for code generation tasks
- System design with separation of concerns
- LLM integration and error handling
- Code quality and documentation practices
- Multi-step AI workflows

### Hints (if needed)
- System prompts should establish clear roles and output expectations
- Keep user prompts minimal and focused on the specific task
- Consider including requirements for comments and error handling
- Structure prompts to produce consistent, parseable output

### Solution Approach Plan
1. Create separate functions for generation, explanation, and review
2. Design role-specific system prompts for each function
3. Implement proper message structuring (system + user messages)
4. Add error handling and fallback mechanisms
5. Provide comprehensive example usage in main block
6. Test with various programming languages and complexity levels

## Example Input/Output
```
Input: "Create a Python function that validates email addresses using regex"
Output: 
- Generated code with proper regex pattern and validation logic
- Explanation of how regex components work
- Review suggestions for edge cases and optimization
```
