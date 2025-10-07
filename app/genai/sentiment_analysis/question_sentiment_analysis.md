# Sentiment Analysis and Classification

## Context
Sentiment analysis is crucial for businesses to understand customer feedback, social media monitoring, and market research. This problem demonstrates advanced prompt engineering techniques to achieve reliable sentiment classification using LLMs with various output formats and accuracy constraints.

## Problem Statement
Implement a comprehensive sentiment analysis system that demonstrates different LLM prompt engineering strategies:
1. Precise single-label classification with engineered constraints
2. JSON-formatted analytical sentiment output with confidence scores
3. Batch classification utilities for processing multiple texts
4. Comparative sentiment analysis between different texts
5. Showcase how explicit role definition and formatting constraints improve reliability

## Requirements
- Classify sentiment into exactly three categories: Positive, Negative, Neutral
- Implement robust prompt engineering with clear role definitions
- Handle edge cases and mixed sentiments appropriately
- Provide batch processing capabilities for multiple texts
- Generate JSON-formatted detailed analysis with confidence scores
- Include fallback mechanisms for malformed LLM responses
- Support multiple LLM providers with error handling
- Display results in formatted tables with summary statistics

## Assumptions
- Only three canonical sentiments for basic classification
- API latency acceptable for sequential processing (no parallelization required)
- JSON output may occasionally be malformed; fallback strategies needed
- Environment variables provide valid API keys
- Input texts are reasonable in length and appropriate for analysis

## For Examiner

### Difficulty Level
Intermediate to Advanced

### Expected Time
45-60 minutes

### Key Concepts Being Tested
- Advanced prompt engineering techniques
- LLM response reliability and consistency
- JSON parsing and error handling
- Batch processing design patterns
- System design with fallback mechanisms
- Output formatting and user experience

### Hints (if needed)
- Use explicit output constraints to reduce response drift
- Include few-shot examples to illustrate boundary cases
- Implement post-processing to enforce canonical output labels
- Consider how to handle mixed or ambiguous sentiments
- Design prompts that establish clear expertise context

### Solution Approach Plan
1. Design role-specific system prompts with clear expertise context
2. Implement single-text classification with strict output constraints
3. Build batch processing using sequential calls for clarity
4. Create JSON-formatted analysis with confidence scoring
5. Add comparison functionality for differential analysis
6. Implement robust parsing with fallback mechanisms
7. Design formatted output display with summary statistics
8. Test with diverse text samples including edge cases

## Example Input/Output
```
Input: "Great product, works perfectly but delivery was slow"
Output: 
- Classification: "Positive"
- JSON Analysis: {"sentiment": "positive", "confidence": "medium", "explanation": "Overall positive despite delivery concern"}
- Formatted display with summary statistics
```
