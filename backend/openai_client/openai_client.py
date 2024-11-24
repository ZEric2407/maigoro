import os
import dotenv
import ast
dotenv.load_dotenv()  # Load environment variables from .env

from openai import OpenAI

def analyze_cultural_significance(text_translation):
    client = OpenAI(
        api_key = os.environ.get("OPENAI_API_KEY")
    )

    translated_text = text_translation.translated_text

    filter = "Given the following text:"+ translated_text +", identify the most culturally significant words. Provide them as a JSON array of strings."

    filter_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": filter}
        ]
    )

    filtered_words = filter_response.choices[0].message['content']
    try:
        significant_words = ast.literal_eval(filtered_words)
    except Exception as e:
        print(f"Failed to parse the response: {filtered_words}")
        significant_words = []

    cultural_significance_list = []

    for i in significant_words:
        cultural_significance = "Given the following word:" + i + ", give the cultural significance of that word. Provide a consise explanation"

        cultural_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": cultural_significance}
            ]
        )

        cultural_significance_list.append(cultural_response.choices[0].message['content'])

    for j in range(len(significant_words)):
        cultural_answer =  significant_words[j]+ ": " + cultural_significance_list[j]
        print(cultural_answer)


"""completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "What is the sagrada familia?."
        }
    ]
)

print(completion.choices[0].message)"""