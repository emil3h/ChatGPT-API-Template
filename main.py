# create .env and add key OPENAI_API_KEY="key"
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def ask_question():
    # user to input
    user_question = input("Enter your question: ")

    # custom prompt 
    custom_prompt = f'''
    Your assistance is requested solely for my journey in mastering the Swift programming language. 
    While I acknowledge your proficiency in other programming languages, 
    I kindly ask that all responses be tailored exclusively to Swift-related inquiries. 
    Please refrain from offering advice or examples in any other programming language. 
    Thank you for your understanding and cooperation in facilitating my Swift learning experience.

    User Question: {user_question}
    '''

    # Generate completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": custom_prompt,
            }
        ],
        model="gpt-4"
    )

    # Display the response
    print(chat_completion.choices[0].message.content)

if __name__ == "__main__":
    ask_question()