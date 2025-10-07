# Question Answering and Information Extraction

## Context
Question answering systems are fundamental to many AI applications including chatbots, search engines, educational tools, and information extraction pipelines. This problem demonstrates building a versatile QA system that can handle various types of questions and extract structured information from unstructured text.

## Problem Statement
Implement a comprehensive question answering and information extraction system that:
1. Answer free-form questions with optional context documents
2. Extract specific categories of information from unstructured text
3. Perform fact-checking and claim verification with uncertainty handling
4. Generate educational quizzes based on provided content
5. Demonstrate effective prompt engineering for different reasoning styles and output formats

## Requirements
- Support both contextual and general knowledge question answering
- Handle uncertainty appropriately when information is insufficient
- Extract configurable categories of information (dates, names, locations, etc.)
- Provide balanced fact-checking with confidence assessments
- Generate educational quizzes with variable difficulty levels
- Maintain clear separation between different QA functions
- Include robust error handling and fallback mechanisms
- Support multiple LLM providers with consistent interfaces

## Assumptions
- Context documents (when provided) are treated as authoritative sources
- Extraction categories can be mapped to predefined prompt templates
- Output format is primarily plain text with optional structured enumeration
- No external retrieval systems required - pure prompt-based reasoning
- Input questions and contexts are reasonable in scope and complexity

## For Examiner

### Difficulty Level
Intermediate

### Expected Time
40-50 minutes

### Key Concepts Being Tested
- Context-aware prompt engineering
- Information extraction techniques
- Uncertainty handling in AI systems
- Educational content generation
- Modular system design with clear separation of concerns
- Error handling and graceful degradation

### Hints (if needed)
- Emphasize uncertainty handling in system prompts for question answering
- Use configurable extraction categories via mapping dictionaries
- Design separate roles for each function type (QA, extraction, fact-checking)
- Consider how context availability changes prompt structure
- Think about educational best practices for quiz generation

### Solution Approach Plan
1. Implement contextual vs. general question answering with branching logic
2. Create configurable information extraction using category mappings
3. Design fact-checking with balanced assessment and uncertainty expression
4. Build quiz generation with difficulty and question count parameters
5. Implement proper context handling and prompt optimization
6. Add comprehensive error handling and user feedback
7. Provide diverse examples demonstrating all capabilities

## Example Input/Output
```
Input: 
- Question: "What are the main benefits of renewable energy?"
- Context: "Solar and wind energy reduce carbon emissions..."

Output: 
- Contextual answer based on provided information
- Uncertainty acknowledgment when context is insufficient
- Clear, well-structured response format
```
