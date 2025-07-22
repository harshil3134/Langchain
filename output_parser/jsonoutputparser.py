from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)
parser=JsonOutputParser()

template=PromptTemplate(
    template="Give me 5 points on {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain= template | model | parser

res=chain.invoke({'topic':'quantam physics'})

print(res)