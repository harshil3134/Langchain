from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_groq import ChatGroq
from langchain_core.messages import ToolMessage
import json
import asyncio

load_dotenv()

SERVERS={
        "math": {
        "transport": "http",
        "url": "http://localhost:8000/mcp"
    },
}


async def main():

    client=MultiServerMCPClient(SERVERS)
    tools=await client.get_tools()
    resources=await client.get_resources()  


    named_tools={}

    for tool in tools:
        named_tools[tool.name]=tool
    
    print("Tools :",named_tools.keys())
    print("Resources :",resources)  #

    for res in resources:
            for res in resources:
                print(f"Resource object: {res}")
                print(f"Resource type: {type(res)}")
                # Try accessing the blob content
                if hasattr(res, 'uri'):
                    print(f"Resource URI: {res.uri}")
                if hasattr(res, 'mime_type'):
                    print(f"MIME Type: {res.mime_type}")
                if hasattr(res, 'text'):
                    today_expense = res.text
                elif hasattr(res, 'data'):
                    today_expense = res.data
                print(f"Today's Expense: {today_expense}")

    llm=ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0,
    )
    llm_with_tools=llm.bind_tools(tools)

    while True:
        prompt=input("enter command")
        if prompt=="q":
            break


            # Add today's expense to context
        context_prompt = f"Today's expense data: {json.dumps(today_expense)}\n\nUser query: {prompt}"
        
        response=await llm_with_tools.ainvoke(context_prompt)
        if not getattr(response,"tool_calls",None):
            print("response ",response)
            return
        
        tool_messages=[]
        for tc in response.tool_calls:
            selected_tool=tc["name"]
            selected_tool_args=tc.get("args") or {}
            selected_tool_id=tc["id"]

            result=await named_tools[selected_tool].ainvoke(selected_tool_args)
            tool_messages.append(ToolMessage(tool_call_id=selected_tool_id,content=json.dumps(result)))

        final_response=await llm_with_tools.ainvoke([prompt,response,*tool_messages])
        print(f"final response {final_response.content}")

if __name__ == '__main__':
    asyncio.run(main())