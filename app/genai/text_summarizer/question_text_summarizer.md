# Text Summarization and Content Compression

## Context
Text summarization is essential for information processing in news, research, legal documents, and content curation. This problem demonstrates building a flexible summarization system that can adapt to different content types and summary requirements while maintaining key information integrity.

## Problem Statement
Implement a text summarizer that can take a long piece of text and generate a concise summary while maintaining the core message and important details. The solution should be configurable for different summary lengths and styles.

## Requirements
- Accept text input of varying lengths (minimum 500 characters)
- Generate summaries of configurable lengths (short: 1-2 sentences, medium: 3-5 sentences, long: 1 paragraph)
- Preserve key information and main themes
- Handle different text types (articles, reports, stories)
- Provide both extractive and abstractive summarization options
- Include confidence scoring for summary quality

## Assumptions
- Input text is in English
- Text is well-formatted and readable
- Maximum input length is 10,000 characters
- LLM API is available and configured

## For Examiner

### Difficulty Level
Intermediate

### Expected Time
45-60 minutes

### Key Concepts Being Tested
- Natural Language Processing fundamentals
- LLM prompt engineering
- Text preprocessing and cleaning
- API integration and error handling
- Configuration management
- User input validation

### Hints (if needed)
- Consider different prompting strategies for extractive vs abstractive summarization
- Think about how to validate summary quality
- Consider edge cases like very short input text
- Think about how to handle different text structures

### Solution Approach Plan
1. **Input Validation**: Validate text length and format
2. **Text Preprocessing**: Clean and prepare text for summarization
3. **Prompt Engineering**: Design effective prompts for different summary types
4. **LLM Integration**: Use the configured LLM client for summarization
5. **Post-processing**: Format and validate the generated summary
6. **Error Handling**: Handle API failures and edge cases
7. **Testing**: Provide examples with different text types and lengths

## Example Input/Output
```
Input: "Artificial intelligence (AI) has transformed numerous industries over the past decade. From healthcare to finance, AI technologies are being integrated to improve efficiency, accuracy, and decision-making processes. Machine learning algorithms can analyze vast datasets to identify patterns that humans might miss. In healthcare, AI assists in diagnostic imaging, drug discovery, and personalized treatment plans. The financial sector uses AI for fraud detection, algorithmic trading, and risk assessment. However, the rapid adoption of AI also raises concerns about job displacement, privacy, and ethical considerations. As we move forward, it's crucial to balance innovation with responsible AI development to ensure these technologies benefit society as a whole."

Output (Short): "AI has revolutionized industries like healthcare and finance through improved efficiency and pattern recognition, but raises concerns about job displacement and ethics that require responsible development."

Output (Medium): "Artificial intelligence has transformed industries over the past decade, particularly healthcare and finance. AI technologies improve efficiency through machine learning algorithms that analyze vast datasets and identify patterns humans might miss. In healthcare, AI assists with diagnostic imaging and personalized treatment, while finance uses it for fraud detection and risk assessment. However, rapid AI adoption raises concerns about job displacement, privacy, and ethics, making responsible development crucial for societal benefit."
```
