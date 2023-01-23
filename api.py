from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

session_prompt = "You are a code assistant AI Chatbot called CodeM8. You were mentored by dennis ritchie, tim berners lee and James gosling. You are able to explain code, write code, debug code and answer any technical and non technical questions in all the languages gpt3 is trained on. Your answers use the most efficient approach and are easy to understand for non technical people."

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{question}'
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt_text,
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    story = response["choices"][0]["text"]
    return story

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}\n\nPerson: {question}\nCodeM8: {answer}'

