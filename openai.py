import requests
import json
from dotenv import load_dotenv

load_dotenv()


def complete_chat(api_key, content):
    process_content = f"You are a translate bot, please translate the following content to english (Please keep the markdown format):\n\n{content}"
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": process_content}],
        "temperature": 0.7
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    json_response = response.json()

    if response.status_code == 200:
        return json_response['choices'][0]['message']['content']
    else:
        return "Error: " + json_response["error"]["message"]
