from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt=PromptTemplate(
    template="Generate 5 intresting facts about this {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model=ChatGoogleGenerativeAI(
    model='gemini-2.0-flash'
)

parser=StrOutputParser()

chain=prompt | model | parser | prompt2 | model | parser

res=chain.invoke({'topic':'cloud computing'})

print(res)

chain.get_graph().print_ascii()