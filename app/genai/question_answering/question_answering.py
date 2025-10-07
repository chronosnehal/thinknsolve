#!/usr/bin/env python3
"""
Question Answering and Information Extraction - Solution Implementation

Description: A comprehensive question answering system that handles various types of questions,
extracts information, performs fact-checking, and generates educational quizzes.
"""

from app.utils.config import LLMClientManager

def answer_question(question: str, context: str = "", provider: str = "openrouter") -> str:
    """
    Answer a question, optionally using provided context.

    Args:
        question: The question to answer
        context: Optional context to help answer the question
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Answer to the question
    """
    client = LLMClientManager.create_client(provider)

    if context:
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant that answers questions based on the provided context. If the context doesn't contain enough information, say so and provide the best answer you can."
            },
            {
                "role": "user",
                "content": f"Context: {context}\n\nQuestion: {question}"
            }
        ]
    else:
        messages = [
            {
                "role": "system",
                "content": "You are a knowledgeable assistant. Provide accurate, helpful answers to questions. If you're not certain about something, acknowledge the uncertainty."
            },
            {
                "role": "user",
                "content": question
            }
        ]

    return client.chat(messages)

def extract_key_information(text: str, info_type: str = "main_points", provider: str = "openrouter") -> str:
    """
    Extract specific types of information from text.

    Args:
        text: Text to analyze
        info_type: Type of information to extract (main_points, dates, names, facts, etc.)
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Extracted information
    """
    client = LLMClientManager.create_client(provider)

    extraction_prompts = {
        "main_points": "Extract the main points and key information",
        "dates": "Extract all dates and time references",
        "names": "Extract all names of people, places, and organizations",
        "facts": "Extract factual claims and statistics",
        "action_items": "Extract action items and next steps",
        "keywords": "Extract important keywords and technical terms"
    }

    prompt = extraction_prompts.get(info_type, f"Extract {info_type}")

    messages = [
        {
            "role": "system",
            "content": f"You are an information extraction specialist. {prompt} from the given text. Present the results in a clear, organized format."
        },
        {
            "role": "user",
            "content": f"Text to analyze:\n\n{text}"
        }
    ]

    return client.chat(messages)

def fact_check(claim: str, provider: str = "openrouter") -> str:
    """
    Fact-check a claim or statement.

    Args:
        claim: The claim to fact-check
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Fact-check analysis
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": "You are a fact-checker. Analyze claims for accuracy based on your knowledge. Provide a balanced assessment, note any uncertainties, and suggest where to verify information."
        },
        {
            "role": "user",
            "content": f"Please fact-check this claim: {claim}"
        }
    ]

    return client.chat(messages)

def generate_quiz(topic: str, difficulty: str = "medium", num_questions: int = 5, provider: str = "openrouter") -> str:
    """
    Generate a quiz on a given topic.

    Args:
        topic: Quiz topic
        difficulty: Difficulty level (easy, medium, hard)
        num_questions: Number of questions to generate
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Generated quiz
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": f"You are an educational content creator. Generate a {difficulty} level quiz with {num_questions} questions about the given topic. Include a mix of question types and provide answers at the end."
        },
        {
            "role": "user",
            "content": f"Create a quiz about: {topic}"
        }
    ]

    return client.chat(messages)

def main():
    """Main function to demonstrate the solution"""
    try:
        print("=== Question Answering and Information Extraction System ===\n")

        # Answer a general question
        question = "What are the main benefits of using renewable energy sources?"
        print("Answering general question...")
        answer = answer_question(question, provider="openrouter")
        print("Q:", question)
        print("A:", answer)
        print("\n" + "="*50 + "\n")

        # Extract information from text
        sample_text = """
        The quarterly meeting will be held on March 15th, 2024, at 2:00 PM in Conference Room B. 
        Attendees include John Smith (CEO), Sarah Johnson (CTO), and Mike Davis (CFO). 
        Key agenda items are: Q1 financial review, new product launch timeline, and hiring plans for Q2. 
        The company reported 25% revenue growth and plans to hire 50 new employees.
        """

        print("Extracting key information from sample text...")
        key_info = extract_key_information(sample_text, "main_points")
        print("Key Information Extracted:")
        print(key_info)
        print("\n" + "="*50 + "\n")

        # Fact-check a claim
        claim = "The Great Wall of China is visible from space with the naked eye."
        print("Fact-checking claim...")
        fact_result = fact_check(claim)
        print("Claim:", claim)
        print("Fact-check result:", fact_result)
        print("\n" + "="*50 + "\n")

        # Generate a quiz
        print("Generating educational quiz...")
        quiz = generate_quiz("Python programming basics", "medium", 3)
        print("Generated Quiz:")
        print(quiz)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
