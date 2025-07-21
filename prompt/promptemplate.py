from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

temp = PromptTemplate(
    template='What is {topic}',
    input_variables=['topic']
)

prompt = temp.invoke({'topic':'GenAi'})

result = model.invoke(prompt)

print(result.content)