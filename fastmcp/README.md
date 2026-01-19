# FastMCP Learning Project

A learning implementation of a Model Context Protocol (MCP) server using FastMCP framework.

## Overview

This project demonstrates how to:
- Build an MCP server with basic tools and resources
- Create an MCP client to interact with the server
- Integrate MCP with LangChain and LLMs (ChatGroq)
- Use static data in resources for testing

## Implementation Details

### Tools (in main.py)

1. **add(a: float, b: float) -> float**
   - Simple addition function for testing tool invocation
   - Decorated with `@mcp.tool`

2. **multiply(a: float, b: float) -> float**
   - Simple multiplication function for testing tool invocation
   - Decorated with `@mcp.tool`

3. **multiplyn(nums: List[float]) -> float**
   - Multiplies multiple numbers together
   - Demonstrates handling list inputs

### Resources (Static Data in main.py)

- **resource://todayexpense**: Mock expense data stored directly in the server
  ```python
  @mcp.resource("resource://todayexpense")
  def get_todays_expense() -> dict:
      "Returns todays expense"
      return {
          "18/02/2026": 120,
          "19/02/2026": 320,
          "20/02/2026": 1450,
          "21/02/2026": 2120,
          "22/02/2026": 20,
          "23/02/2026": 190,
      }
  ```
  
  **Note**: This is static test data for learning purposes.

## Learning Concepts

This project demonstrates:

### 1. **MCP Server (main.py)**
- How to define tools using `@mcp.tool` decorator
- How to define resources using `@mcp.resource` decorator
- How to expose functionality via HTTP transport

### 2. **MCP Client (client.py)**
- How to connect to an MCP server using `MultiServerMCPClient`
- How to retrieve available tools and resources
- How to invoke tools through the client

### 3. **LLM Integration**
- Binding MCP tools to a Language Model (ChatGroq)
- Using the LLM to decide which tools to call
- Passing tool results back to the LLM for final response

### 4. **Request-Response Flow**
```
User Input
    ↓
LLM (decides which tool to use)
    ↓
Tool Invocation (via MCP client)
    ↓
Tool Result
    ↓
LLM (processes result)
    ↓
Final Response
```

## Quick Start

### Prerequisites
- Python 3.11+
- `uv` package manager

### Setup

```bash
# Install dependencies
uv pip install fastmcp langchain-mcp-adapters langchain-groq python-dotenv
```

### Terminal 1: Start the MCP Server

```bash
cd /Users/hp/Developer/Langchain/fastmcp
fastmcp run main.py --transport http --host 0.0.0.0 --port 8000
```

### Terminal 2: Run the MCP Client

```bash
cd /Users/hp/Developer/Langchain/fastmcp
python3 client.py
```

### Try These Commands

```
enter command: What is 5 plus 3?
enter command: Multiply 10 and 20
enter command: Multiply the numbers 2, 3, and 4
enter command: q  # to exit
```

## File Structure

- **main.py**: MCP Server implementation
  - Defines tools (add, multiply, multiplyn)
  - Defines resources (todayexpense with static data)
  - Initializes FastMCP server with HTTP transport

- **client.py**: MCP Client implementation
  - Connects to the MCP server
  - Retrieves available tools and resources
  - Integrates with ChatGroq LLM
  - Handles user input and tool invocation loop

- **pyproject.toml**: Project configuration and dependencies

## Key Learnings

1. **Tools vs Resources**
   - Tools: Callable functions that perform actions
   - Resources: Static or dynamic data that can be accessed

2. **Transport Types**
   - HTTP: For remote servers or already-running processes
   - Stdio: For direct subprocess communication

3. **LLM Integration**
   - LLMs can be bound with tools using `bind_tools()`
   - LLMs automatically decide when to use tools
   - Tool results need to be processed by the LLM for final responses

4. **Error Handling**
   - Proper async/await patterns
   - Exception handling for network calls

