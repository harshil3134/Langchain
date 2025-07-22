from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model=ChatGoogleGenerativeAI(
    model='gemini-2.0-flash'
)


parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Assume you are a Custom support represenative and Write an appropriate response to this positive feedback .Text not should contain anything that display you are a model \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Assume you are a Custom support represenative and Write an appropriate response to this negative feedback Text not should contain anything that display you are a model\n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

review="I’ve been an XR user since early 2019 till now. No repairment yet, the battery still dependable for my daily task even though it asked for repair. It was my best mobile phone until now, my first expensive phone.I am not a hardcore mobile gamer. I guess that was good for my XR’s health.Currently cleaning unused Whatsapp files that taking a lot XR memories slowly. After that, I can update it to the latest iOS version.If you’re buying for long use, I suggest you the iPhone 16e since it will get the iOS updates for another 5–6 year I guess compared to XR."

print(chain.invoke({'feedback': review}))

chain.get_graph().print_ascii()