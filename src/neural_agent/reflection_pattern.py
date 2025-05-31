import os
from pprint import pprint
from groq import Groq
from dotenv import load_dotenv
from IPython.display import display_markdown
from pathlib import Path

load_dotenv(Path(__file__).parent.parent.parent / '.env')  # Updated path for package structure

print("GROQ_API_KEY exists:", os.getenv("GROQ_API_KEY") is not None)
# load_dotenv()

client = Groq()

generation_chat_history = [{
    "role": "system",
    "content": """You are an exprt football analyst
    Your task is to Generate the best content possible for the user's request. If the user provides critique,"
    respond with a revised version of your previous attempt."""
}]

generation_chat_history.append(
    {
        "role": "user",
        "content": "What is the best way to play football?"
    }
)

mergesort_code = client.chat.completions.create(
    messages = generation_chat_history,
    model = "llama3-70b-8192"
).choices[0].message.content

generation_chat_history.append(
    {
        "role": "assistant",
        "content": mergesort_code
    }
)

# display_markdown(mergesort_code, raw=True)
print(mergesort_code)