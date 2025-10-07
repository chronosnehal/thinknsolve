#!/usr/bin/env python3
"""
Sentiment Analysis and Classification - Solution Implementation

Description: A comprehensive sentiment analysis system demonstrating advanced prompt engineering
techniques for reliable sentiment classification using LLMs.
"""

from typing import List, Dict, Tuple

# For GenAI problems ONLY - import LLM client
from app.utils.config import LLMClientManager

def classify_sentiment_with_prompt_engineering(text: str, provider: str = "openrouter") -> str:
    """
    Classify sentiment using carefully engineered prompts for maximum accuracy.

    Args:
        text: Customer review text to analyze
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Sentiment classification: "Positive", "Negative", or "Neutral"
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": """You are an expert sentiment analysis specialist with years of experience in customer feedback classification.

Your task is to classify customer reviews into exactly one of these three categories:
- Positive: Reviews expressing satisfaction, praise, or positive experiences
- Negative: Reviews expressing dissatisfaction, complaints, or negative experiences  
- Neutral: Reviews that are balanced, factual, or express mixed/no clear sentiment

IMPORTANT GUIDELINES:
1. Focus on the overall emotional tone and customer satisfaction level
2. Consider context - a complaint followed by praise may still be positive overall
3. Neutral reviews often contain factual statements without strong emotional indicators
4. Even mild expressions of satisfaction should be classified as Positive
5. Even mild expressions of dissatisfaction should be classified as Negative

RESPONSE FORMAT: Respond with ONLY the classification word: Positive, Negative, or Neutral

EXAMPLES:
- "Great product, works perfectly!" → Positive
- "Terrible experience, waste of money" → Negative  
- "Product arrived on time, standard quality" → Neutral
- "Had some issues initially but customer service fixed everything" → Positive"""
        },
        {
            "role": "user",
            "content": f"Classify this customer review: {text}"
        }
    ]

    response = client.chat(messages).strip()

    # Ensure response is one of the expected values
    if response in ["Positive", "Negative", "Neutral"]:
        return response
    else:
        # Fallback parsing for edge cases
        response_lower = response.lower()
        if "positive" in response_lower:
            return "Positive"
        elif "negative" in response_lower:
            return "Negative"
        else:
            return "Neutral"

def batch_sentiment_classification(reviews: List[str], provider: str = "openrouter") -> List[Tuple[str, str]]:
    """
    Classify sentiment for multiple customer reviews and return results.

    Args:
        reviews: List of customer review texts
        provider: LLM provider ("openai", "openrouter")

    Returns:
        List of tuples containing (review_text, sentiment_classification)
    """
    results = []
    for review in reviews:
        sentiment = classify_sentiment_with_prompt_engineering(review, provider)
        results.append((review, sentiment))

    return results

def analyze_sentiment(text: str, provider: str = "openrouter") -> Dict[str, str]:
    """
    Analyze the sentiment of a given text with detailed output.

    Args:
        text: Text to analyze
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Dictionary with sentiment, confidence, and explanation
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": "You are a sentiment analysis expert. Analyze the sentiment of the given text and respond with ONLY a JSON object containing 'sentiment' (positive/negative/neutral), 'confidence' (high/medium/low), and 'explanation' (brief reason)."
        },
        {
            "role": "user",
            "content": f"Analyze the sentiment of this text: {text}"
        }
    ]

    response = client.chat(messages)

    # Try to parse JSON response, fallback to simple format
    try:
        import json
        return json.loads(response)
    except:
        return {
            "sentiment": "unknown",
            "confidence": "low",
            "explanation": response
        }

def compare_sentiments(text1: str, text2: str, provider: str = "openrouter") -> str:
    """
    Compare sentiments between two texts.

    Args:
        text1: First text
        text2: Second text
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Comparison analysis
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": "You are a sentiment analysis expert. Compare the sentiments of two texts and explain the differences."
        },
        {
            "role": "user",
            "content": f"Compare the sentiments of these two texts:\n\nText 1: {text1}\n\nText 2: {text2}"
        }
    ]

    return client.chat(messages)

def display_sentiment_results_table(results: List[Tuple[str, str]]) -> None:
    """
    Display sentiment classification results in a formatted table.

    Args:
        results: List of tuples containing (review_text, sentiment_classification)
    """
    print("\n" + "="*100)
    print("CUSTOMER REVIEW SENTIMENT CLASSIFICATION RESULTS")
    print("="*100)
    print(f"{'#':<3} {'Review':<70} {'Sentiment':<15}")
    print("-"*100)

    for i, (review, sentiment) in enumerate(results, 1):
        # Truncate long reviews for table display
        display_review = review if len(review) <= 67 else review[:67] + "..."

        # Color coding for terminal output
        sentiment_display = sentiment
        if sentiment == "Positive":
            sentiment_display = f"✅ {sentiment}"
        elif sentiment == "Negative":
            sentiment_display = f"❌ {sentiment}"
        else:
            sentiment_display = f"➖ {sentiment}"

        print(f"{i:<3} {display_review:<70} {sentiment_display:<15}")

    print("-"*100)

    # Summary statistics
    sentiments = [result[1] for result in results]
    positive_count = sentiments.count("Positive")
    negative_count = sentiments.count("Negative")
    neutral_count = sentiments.count("Neutral")
    total = len(sentiments)

    print(f"\nSUMMARY:")
    print(f"Total Reviews: {total}")
    print(f"Positive: {positive_count} ({positive_count/total*100:.1f}%)")
    print(f"Negative: {negative_count} ({negative_count/total*100:.1f}%)")
    print(f"Neutral: {neutral_count} ({neutral_count/total*100:.1f}%)")

def main():
    """Main function to demonstrate the solution"""
    # Sample customer reviews for testing
    sample_reviews = [
        "Absolutely amazing product! Exceeded all my expectations and arrived quickly.",
        "Worst purchase I've ever made. Poor quality and terrible customer service.",
        "Product works as described. Delivery was on time. Standard experience overall.",
        "Love this item! Great value for money and my family enjoys using it daily.",
        "Had some initial issues but the support team resolved everything promptly. Very satisfied now.",
        "Completely defective item. Requesting full refund. Very disappointed with this brand.",
        "Decent product for the price point. Nothing extraordinary but does the job adequately.",
        "Outstanding quality and craftsmanship! Highly recommend to anyone considering this purchase.",
        "Mixed feelings about this. Some features work well, others could be improved significantly.",
        "Total waste of money. Broke after one week of normal use. Poor build quality."
    ]

    try:
        print("=== Sentiment Analysis and Prompt Engineering System ===\n")
        provider = "openrouter"
        print(f"Using provider: {provider.upper()}")

        print("\n" + "="*80)
        print("1. SINGLE-LABEL CLASSIFICATION WITH PROMPT ENGINEERING")
        print("="*80)

        # Demonstrate single classification with detailed output
        test_text = "Great product, works perfectly but delivery was slow"
        print(f"Test Text: '{test_text}'")

        classification = classify_sentiment_with_prompt_engineering(test_text, provider)
        print(f"Classification Result: {classification}")

        print("\n" + "="*80)
        print("2. JSON-FORMATTED DETAILED ANALYSIS")
        print("="*80)

        # Demonstrate detailed JSON analysis
        detailed_analysis = analyze_sentiment(test_text, provider)
        print(f"Detailed Analysis: {detailed_analysis}")

        print("\n" + "="*80)
        print("3. COMPARATIVE SENTIMENT ANALYSIS")
        print("="*80)

        # Demonstrate comparison between texts
        text1 = "Amazing product! Love everything about it!"
        text2 = "Terrible quality, completely disappointed with this purchase."

        print(f"Text 1: '{text1}'")
        print(f"Text 2: '{text2}'")

        comparison = compare_sentiments(text1, text2, provider)
        print(f"Comparison Analysis:\n{comparison}")

        print("\n" + "="*80)
        print("4. BATCH PROCESSING WITH FORMATTED RESULTS")
        print("="*80)

        # Classify all sample reviews
        print("Processing multiple customer reviews...")
        results = batch_sentiment_classification(sample_reviews, provider)

        # Display results in tabular format
        display_sentiment_results_table(results)

        print("\n" + "="*80)
        print("5. PROMPT ENGINEERING TECHNIQUES DEMONSTRATED")
        print("="*80)
        print("✅ Role-specific system prompts with expertise context")
        print("✅ Explicit output constraints to reduce response drift")
        print("✅ Few-shot examples illustrating boundary cases")
        print("✅ Post-processing to enforce canonical output labels")
        print("✅ Handling of mixed or ambiguous sentiments")
        print("✅ JSON-formatted responses with confidence scoring")
        print("✅ Batch processing with summary statistics")
        print("✅ Comparative analysis capabilities")

        print(f"\n🎉 All sentiment analysis features completed successfully using {provider.upper()}!")

    except Exception as e:
        print(f"❌ Error during sentiment classification: {e}")
        print("Make sure your API key is properly configured in environment variables.")
        print("\nTroubleshooting tips:")
        print("• Check if your API key is valid and has sufficient credits")
        print("• Try switching to a different model if getting 502 errors")
        print("• Verify your internet connection")

if __name__ == "__main__":
    main()
