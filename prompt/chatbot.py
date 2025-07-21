from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')


model=ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    google_api_key=GOOGLE_API_KEY
)
chat_history=[
    SystemMessage(content="You are a helpful AI assistant")
]

while True:
    user_input=input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    result=model.invoke(user_input)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ',result.content)
print(chat_history)