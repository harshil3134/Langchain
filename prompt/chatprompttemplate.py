from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    temperature=0,
)

prompt_template=ChatPromptTemplate(
    [
    ('system','You are an a Helpful {domain} expert'),
    ('human','explain in simple terms,what is {topic}')
    ]
)

prompt=prompt_template.invoke({'domain':'cricket','topic':'Dusra'})

result=model.invoke(prompt)
print(result.content)