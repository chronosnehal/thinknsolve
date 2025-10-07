#!/usr/bin/env python3
"""
Creative Writing and Content Generation - Solution Implementation

Description: A comprehensive content generation system that creates stories, blog posts,
product descriptions, and writing improvements using LLM capabilities.
"""

from typing import List

# For GenAI problems ONLY - import LLM client
from app.utils.config import LLMClientManager

def generate_story(prompt: str, genre: str = "fantasy", length: str = "short", provider: str = "openrouter") -> str:
    """
    Generate a creative story based on a prompt.

    Args:
        prompt: Story prompt or theme
        genre: Story genre (fantasy, sci-fi, mystery, romance, etc.)
        length: Story length (short, medium, long)
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Generated story
    """
    client = LLMClientManager.create_client(provider)

    length_guidelines = {
        "short": "200-400 words",
        "medium": "500-800 words",
        "long": "1000+ words"
    }

    messages = [
        {
            "role": "system",
            "content": f"You are a creative writer specializing in {genre} stories. Write engaging, well-structured stories with compelling characters and vivid descriptions. Target length: {length_guidelines.get(length, '300-500 words')}."
        },
        {
            "role": "user",
            "content": f"Write a {genre} story based on this prompt: {prompt}"
        }
    ]

    return client.chat(messages)

def write_blog_post(topic: str, tone: str = "professional", target_audience: str = "general", provider: str = "openrouter") -> str:
    """
    Generate a blog post on a given topic.

    Args:
        topic: Blog post topic
        tone: Writing tone (professional, casual, humorous, etc.)
        target_audience: Target audience (general, technical, beginners, etc.)
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Generated blog post
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": f"You are a skilled content writer. Write engaging blog posts with a {tone} tone for {target_audience} audience. Include a compelling title, introduction, main points, and conclusion."
        },
        {
            "role": "user",
            "content": f"Write a blog post about: {topic}"
        }
    ]

    return client.chat(messages)

def generate_product_description(product_name: str, features: List[str], target_market: str = "general", provider: str = "openrouter") -> str:
    """
    Generate marketing copy for a product.

    Args:
        product_name: Name of the product
        features: List of product features
        target_market: Target market/audience
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Product description
    """
    client = LLMClientManager.create_client(provider)

    features_text = "\n".join([f"- {feature}" for feature in features])

    messages = [
        {
            "role": "system",
            "content": f"You are a marketing copywriter. Create compelling product descriptions that highlight benefits and appeal to the {target_market} market. Use persuasive language and focus on value."
        },
        {
            "role": "user",
            "content": f"Create a product description for '{product_name}' with these features:\n{features_text}"
        }
    ]

    return client.chat(messages)

def improve_writing(text: str, style: str = "clarity", provider: str = "openrouter") -> str:
    """
    Improve existing writing for better clarity, style, or engagement.

    Args:
        text: Original text to improve
        style: Improvement focus (clarity, engagement, professional, casual)
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Improved text
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": f"You are an expert editor. Improve the given text focusing on {style}. Maintain the original meaning while enhancing readability and impact."
        },
        {
            "role": "user",
            "content": f"Please improve this text for better {style}:\n\n{text}"
        }
    ]

    return client.chat(messages)

def main():
    """Main function to demonstrate the solution"""
    try:
        print("=== Creative Writing and Content Generation System ===\n")

        # Generate a short story
        story_prompt = "A librarian discovers that books in their library can transport readers to the worlds within them"
        print("Generating fantasy story...")
        story = generate_story(story_prompt, "fantasy", "short", "openrouter")
        print("Generated Story:")
        print(story)
        print("\n" + "="*50 + "\n")

        # Generate a blog post
        blog_topic = "The Benefits of Remote Work for Software Developers"
        print("Generating blog post...")
        blog_post = write_blog_post(blog_topic, "professional", "tech professionals")
        print("Generated Blog Post:")
        print(blog_post)
        print("\n" + "="*50 + "\n")

        # Generate product description
        product_features = [
            "Wireless charging capability",
            "24-hour battery life",
            "Noise-canceling technology",
            "Waterproof design",
            "Voice assistant integration"
        ]
        print("Generating product description...")
        product_desc = generate_product_description("SmartEars Pro", product_features, "tech enthusiasts")
        print("Product Description:")
        print(product_desc)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
