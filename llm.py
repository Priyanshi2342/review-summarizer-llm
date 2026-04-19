import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def analyze_review(text):
    prompt = f"""
Analyze the sentiment of this review and summarize in one short sentence.

Return format:
Sentiment: Positive/Negative/Neutral
Summary: <one sentence>

Review: {text}
"""

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",  # ✅ FINAL FIX
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=60
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("ERROR:", e)
        return "API Error"