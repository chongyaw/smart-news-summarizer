# Import code from another python script file
import secrets

import openai

# Summarize text using OpenAI
# May incurs cost
# Check at https://platform.openai.com/usage

openai.api_key = secrets.openaiapikey

def summarize(text):
    prompt = f"Summarize this paragraph: {text}"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
