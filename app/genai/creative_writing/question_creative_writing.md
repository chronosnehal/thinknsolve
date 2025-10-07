# Creative Writing and Content Generation

## Context
Content creation is a major application of AI in marketing, publishing, and creative industries. This problem involves building a system that can generate various types of content including stories, blog posts, product descriptions, and writing improvements using AI capabilities.

## Problem Statement
Implement a comprehensive content generation system that leverages LLM capabilities to:
1. Generate creative stories with genre and length control
2. Create blog posts with configurable tone and target audience
3. Generate compelling product descriptions from feature lists
4. Improve existing writing for better clarity, style, or engagement
5. Demonstrate effective prompt engineering for different content types

## Requirements
- Support multiple content generation types (stories, blogs, product descriptions, writing improvement)
- Implement configurable parameters for genre, tone, audience, and style
- Maintain consistent quality and appropriate tone for each content type
- Handle various input formats and produce well-structured output
- Support multiple LLM providers with clean error handling
- Provide clear separation between different content generation functions

## Assumptions
- LLM providers return plain text responses
- Length descriptors are heuristic guidelines rather than strict limits
- No content persistence or database storage required
- Network connectivity available for API calls
- Input content is reasonable in scope and appropriate

## For Examiner

### Difficulty Level
Intermediate

### Expected Time
30-45 minutes

### Key Concepts Being Tested
- Prompt engineering for creative vs. structured content
- Parameter-driven content generation
- Clean code architecture with separation of concerns
- Error handling and user experience design
- Understanding of different content types and their requirements

### Hints (if needed)
- Design role-specific system prompts for each content type
- Use parameter mapping to translate user inputs into prompt guidance
- Consider how to structure prompts for consistent output quality
- Think about how different content types require different approaches

### Solution Approach Plan
1. Create separate functions for each content generation type
2. Design parameter mapping systems for genre, tone, and style
3. Implement role-specific system prompts for each function
4. Build proper message structures with system and user content
5. Add comprehensive error handling and user feedback
6. Provide diverse examples in the main demonstration block

## Example Input/Output
```
Input: 
- Story prompt: "A librarian discovers magical books"
- Genre: "fantasy"
- Length: "short"

Output: 
- 200-400 word fantasy story with engaging characters and plot
- Professional formatting and narrative structure
```
