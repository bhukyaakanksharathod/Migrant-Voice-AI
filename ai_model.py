import ollama


MODEL_NAME = "gemma3:1b"


def get_ai_response(question):
    """
    Send the user's question to Ollama
    and return the AI-generated response.
    """

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": """
You are Migrant Voice AI, a helpful and friendly AI assistant.

Your purpose is to help migrants understand useful information
about living in a new place.

Give simple, clear and respectful answers.
Avoid complicated language.
If you are unsure about something, clearly say so.
"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"AI Error: {e}"