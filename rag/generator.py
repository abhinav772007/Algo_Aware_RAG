import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_answer(context: str, query: str):
    prompt = f"""
You are an algorithm tutor.

Rules:
- Use ONLY the provided context.
- Do NOT hallucinate.
- If something is missing, say "Not found in context".
- Follow the structure exactly.

Context:
{context}

Question:
{query}

Output format:
1. Intuition
2. Algorithm Steps
3. Code
4. Dry Run
5. Complexity
6. Edge Cases
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    return response.text
