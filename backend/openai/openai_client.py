import os
import dotenv
dotenv.load_dotenv()  # Load environment variables from .env

from openai import OpenAI

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "What is the sagrada familia?."
        }
    ]
)

print(completion.choices[0].message)