import google.generativeai as genai
import json
import os

# IMPORTANT: Replace 'YOUR_GEMINI_API_KEY' with your actual Gemini API Key.
# It's recommended to load this from an environment variable for security.
# Example: export GEMINI_API_KEY='your_key_here'
# For local testing, you can directly paste it here, but be careful not to commit it.
API_KEY = os.getenv("GEMINI_API_KEY", "add your key") # Replace with your key if not using env var

if not API_KEY:
    print("Error: GEMINI_API_KEY environment variable not set or API_KEY not provided.")
    print("Please set the GEMINI_API_KEY environment variable or replace '' with your key in the script.")
    exit()

genai.configure(api_key=API_KEY)

def generate_news_with_gemini(topic):
    """
    Generates news-like articles using the Gemini API based on a given topic.
    The response is structured as a JSON array of articles.
    """
    model = genai.GenerativeModel('gemini-2.0-flash')

    prompt = f"""Generate 3-5 short, distinct news articles about "{topic}".
    Each article should have a 'title', a 'summary' (2-3 sentences), and a 'category' (e.g., 'technology', 'politics', 'science', 'sports', 'health', 'business', 'environment', 'culture').
    Provide the output as a JSON array of objects.
    Example format:
    [
      {{
        "title": "Example Headline 1",
        "summary": "This is a brief summary of the first news article.",
        "category": "technology"
      }},
      {{
        "title": "Example Headline 2",
        "summary": "This is a brief summary of the second news article.",
        "category": "politics"
      }}
    ]
    """

    try:
        # Using generate_content with response_mime_type for structured output
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                response_mime_type="application/json",
                response_schema={
                    "type": "ARRAY",
                    "items": {
                        "type": "OBJECT",
                        "properties": {
                            "title": {"type": "STRING"},
                            "summary": {"type": "STRING"},
                            "category": {"type": "STRING"}
                        },
                        "propertyOrdering": ["title", "summary", "category"]
                    }
                }
            )
        )

        # The response.text will contain the JSON string
        json_string = response.text
        articles = json.loads(json_string)
        return articles

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    print("This script demonstrates generating news articles using the Gemini API.")
    print("It is a standalone script and does not directly interact with the HTML application.")
    print("-" * 60)

    user_topic = input("Enter a news topic (e.g., 'latest space discoveries', 'global economic trends'): ")

    if user_topic:
        print(f"\nGenerating news about '{user_topic}'...")
        generated_articles = generate_news_with_gemini(user_topic)

        if generated_articles:
            print("\n--- Generated News Articles ---")
            for i, article in enumerate(generated_articles):
                print(f"\nArticle {i+1}:")
                print(f"  Title: {article.get('title', 'N/A')}")
                print(f"  Category: {article.get('category', 'N/A')}")
                print(f"  Summary: {article.get('summary', 'N/A')}")
            print("\n-----------------------------")
        else:
            print("Failed to generate articles.")
    else:
        print("No topic entered. Exiting.")

