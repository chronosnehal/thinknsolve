#!/usr/bin/env python3
"""
Text Summarizer - Solution Implementation

Description: A text summarization system that produces concise summaries of long-form content
using configurable LLM clients with support for different summary lengths and styles.
"""

from typing import List

# For GenAI problems ONLY - import LLM client
from app.utils.config import LLMClientManager

def summarize_text(text: str, provider: str = "openrouter", max_words: int = 100) -> str:
    """
    Summarize a given text using the specified LLM provider.

    Args:
        text: The text to summarize
        provider: LLM provider ("openai", "openrouter")
        max_words: Maximum words in the summary

    Returns:
        Summarized text
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": f"You are a text summarization expert. Create concise, accurate summaries that capture the main points and key information. Keep summaries under {max_words} words while preserving essential details. Be neutral and factual."
        },
        {
            "role": "user",
            "content": f"Please summarize the following text:\n\n{text}"
        }
    ]

    return client.chat(messages)

def summarize_multiple_texts(texts: List[str], provider: str = "openrouter", max_words: int = 100) -> List[str]:
    """
    Summarize multiple texts using the specified LLM provider.

    Args:
        texts: List of texts to summarize
        provider: LLM provider ("openai", "openrouter")
        max_words: Maximum words per summary

    Returns:
        List of summarized texts
    """
    summaries = []
    for i, text in enumerate(texts, 1):
        print(f"Summarizing text {i}/{len(texts)}...")
        summary = summarize_text(text, provider, max_words)
        summaries.append(summary)

    return summaries

def create_executive_summary(content: str, provider: str = "openrouter") -> str:
    """
    Create an executive summary suitable for business documents.

    Args:
        content: The content to summarize
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Executive summary
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": "You are a business analyst creating executive summaries. Focus on key insights, actionable items, and strategic implications. Use professional language suitable for senior management."
        },
        {
            "role": "user",
            "content": f"Create an executive summary for the following content:\n\n{content}"
        }
    ]

    return client.chat(messages)

def main():
    """Main function to demonstrate the solution"""
    sample_text = """
    Artificial Intelligence (AI) has become one of the most transformative technologies of the 21st century. 
    From healthcare to finance, transportation to entertainment, AI is revolutionizing how we work, live, and 
    interact with the world around us. Machine learning algorithms can now process vast amounts of data to 
    identify patterns, make predictions, and automate complex tasks that were once thought to require human 
    intelligence. 
    
    In healthcare, AI is being used to diagnose diseases more accurately and develop personalized treatment 
    plans. In finance, algorithmic trading and fraud detection systems powered by AI are protecting billions 
    of dollars in transactions daily. Autonomous vehicles are beginning to transform transportation, promising 
    safer roads and more efficient traffic flow.
    
    However, as AI becomes more prevalent, important questions arise about ethics, privacy, job displacement, 
    and the need for responsible development and deployment of these powerful technologies. The challenge for 
    society is to harness the benefits of AI while mitigating potential risks and ensuring that these 
    technologies serve humanity's best interests.
    """

    additional_texts = [
        "Climate change represents one of the most pressing challenges facing humanity today. Rising global temperatures, melting ice caps, and increasingly frequent extreme weather events are clear indicators that our planet's climate system is undergoing rapid change.",
        "The rise of remote work has fundamentally changed how businesses operate. Companies are discovering that distributed teams can be just as productive as traditional office-based teams, leading to cost savings and improved work-life balance for employees."
    ]

    try:
        print("=== Text Summarization System ===\n")

        # Single text summarization
        print("Summarizing single text...")
        summary = summarize_text(sample_text, "openrouter", 75)
        print("Original text length:", len(sample_text.split()), "words")
        print("Summary:")
        print(summary)
        print("\n" + "="*50 + "\n")

        # Multiple text summarization
        print("Summarizing multiple texts...")
        summaries = summarize_multiple_texts(additional_texts, "openrouter", 50)
        for i, summary in enumerate(summaries, 1):
            print(f"Summary {i}:")
            print(summary)
            print()
        print("="*50 + "\n")

        # Executive summary
        print("Creating executive summary...")
        exec_summary = create_executive_summary(sample_text, "openrouter")
        print("Executive Summary:")
        print(exec_summary)

    except Exception as e:
        print(f"Error: {e}")
        print("Make sure your API key is properly configured in environment variables.")

if __name__ == "__main__":
    main()
