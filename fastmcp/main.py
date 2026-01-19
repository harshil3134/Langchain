from dotenv import load_dotenv
from langchain_groq import ChatGroq
from fastmcp import FastMCP
from typing import List
import math


load_dotenv()

llm=ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
)

mcp=FastMCP("Mathematics operator")

@mcp.tool
def add(a:float,b:float)->float:
    "addition of two numbers"
    return a+b

@mcp.tool
def multiply(a:float,b:float)->float:
    "multiplication of two number"
    return a*b

@mcp.tool
def multiplyn(nums:List[float])->float:
    "multiplication of n numbers"
    return math.prod(nums)


@mcp.resource("resource://todayexpense")
def get_todays_expense() -> dict:
    "Returns todays expense"
    return {
    "18/02/2026":120,
    "19/02/2026":320,
    "20/02/2026":1450,
    "21/02/2026":2120,
    "22/02/2026":20,
    "23/02/2026":190,
    }