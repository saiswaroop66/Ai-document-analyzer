import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_summary(text, summary_length):
    """
    Generate an AI summary using the Groq API.

    Args:
        text (str): Document text.
        summary_length (str): Short, Medium, or Detailed.

    Returns:
        str: Generated summary.
    """

    # Prevent sending huge documents
    max_chars = 12000
    if len(text) > max_chars:
        text = text[:max_chars]

    prompts = {
        "Short": (
            "Summarize the following document in 5-7 concise bullet points."
        ),
        "Medium": (
            "Summarize the following document in a few well-structured paragraphs. "
            "Include the key ideas and important details."
        ),
        "Detailed": (
            "Provide a detailed summary of the following document. "
            "Use headings and bullet points where appropriate."
        ),
    }

    prompt = f"""
You are an expert AI document summarizer.

{prompts.get(summary_length)}

Document:

{text}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional document summarizer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_completion_tokens=800
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating summary:\n\n{e}"