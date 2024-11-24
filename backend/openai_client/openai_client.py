import os
import dotenv
import ast
import logging
from pydantic import BaseModel
from openai import OpenAI

# Load environment variables
dotenv.load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Text(BaseModel):
    string: str

def culturize(instance):
    logging.info("Starting the culturized function.")

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    translated_text = instance.translated_text
    logging.info(f"Translated text received: {translated_text}")

    filter = (
        "Given the following text: " + translated_text +
        ", identify a maximum of three of the most culturally significant objects. Provide them as a JSON array of strings."
    )
    logging.info("Sending request to OpenAI for significant objects.")

    try:
        filter_response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": filter}
            ], 
            frequency_penalty=-0.5,
            max_completion_tokens=1000,
            response_format=Text,
        )

        logging.info(f"FILTER RESPONSE: {filter_response}")


        filter_response_content = filter_response.choices[0].message.parsed.string

        logging.info(f"Filter response received: {filter_response_content}")
    except Exception as e:
        logging.error(f"Error during OpenAI request for filter: {e}")
        return
    
    cultural_significance = (
        "ChatGPT: [SHORTEN: For each of the following objects in the following list: " + filter_response_content +
        ", explain the cultural significance of that object in a few words]"
    )

    try: 
        cultural_response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": cultural_significance}
            ], 
            frequency_penalty=-0.5,
            max_completion_tokens=2000,
            response_format=Text,
        )
        logging.info(f"CULTURE RESPONSE: {cultural_response}")

        cultural_response_content = cultural_response.choices[0].message.parsed.string

        logging.info(f"Cultural response received: {cultural_response_content}")
    except Exception as e:
        logging.error(f"Error during OpenAI request for culture: {e}")
        return


    instance.cultural_significance = cultural_response_content
    logging.info("Culturized function completed successfully.")
