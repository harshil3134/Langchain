from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

llm=ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=GOOGLE_API_KEY
)

#invocation

response=llm.invoke("hey")

print(response.content)

#chaining 
from langchain_core.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate.from_template(
"""
hey what is syntax for printing in "{language}
and show me {number} of examples"
"""
)

chain=prompt | llm
while True:

    lang=input("enter language")
    num=input("num of eg required")
    if lang=='quit':
        break
    res=chain.invoke({
    "language":lang,
    "number":num
    })
    print('AI:',res.content)


