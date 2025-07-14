from openai import OpenAI
from prompts import gather_info_prompt
import os

# Load API key from environment variable or fallback (not recommended for production)
api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")

# Create the OpenAI client once
client = OpenAI(api_key=api_key)

def get_technical_questions(user_info):
    """
    Generates technical interview questions using OpenAI's ChatCompletion API (v1.0+).

    Args:
        user_info (dict): Information like role, skills, experience, etc.

    Returns:
        str: Generated questions or error message.
    """
    prompt = gather_info_prompt(**user_info)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",

            # model="gpt-4",  # You can use "gpt-3.5-turbo" if preferred
            messages=[
                {"role": "system", "content": "You are a technical recruiter."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error generating questions: {str(e)}"
