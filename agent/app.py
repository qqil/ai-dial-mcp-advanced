import asyncio
import json
import os

from agent.clients.custom_mcp_client import CustomMCPClient
from agent.clients.mcp_client import MCPClient
from agent.clients.dial_client import DialClient
from agent.models.message import Message, Role


DIAL_API_KEY = os.getenv("DIAL_API_KEY", "")

async def main():
    #TODO:
    # 1. Take a look what applies DialClient
    # 2. Create empty list where you save tools from MCP Servers later
    # 3. Create empty dict where where key is str (tool name) and value is instance of MCPClient or CustomMCPClient
    # 4. Create UMS MCPClient, url is `http://localhost:8006/mcp` (use static method create and don't forget that its async)
    # 5. Collect tools and dict [tool name, mcp client]
    # 6. Do steps 4 and 5 for `https://remote.mcpservers.org/fetch/mcp`
    # 7. Create DialClient, endpoint is `https://ai-proxy.lab.epam.com`
    # 8. Create array with Messages and add there System message with simple instructions for LLM that it should help to handle user request
    # 9. Create simple console chat (as we done in previous tasks)
    
    tools = []
    tool_name_client_map = {}

    # UMS MCP Client
    ums_mcp_client = await CustomMCPClient.create("http://localhost:8006/mcp")
    ums_tools = await ums_mcp_client.get_tools()
    tools.extend(ums_tools)

    # Fetch MCP Client
    fetch_mcp_client = await MCPClient.create("https://remote.mcpservers.org/fetch/mcp")
    fetch_tools = await fetch_mcp_client.get_tools()
    tools.extend(fetch_tools)

    # Map tool name to MCP client
    for tool in ums_tools:
        tool_name_client_map[tool["function"]["name"]] = ums_mcp_client
        print(f"Registered tool: `{tool['function']['name']}`")
    
    for tool in fetch_tools:
        tool_name_client_map[tool["function"]["name"]] = fetch_mcp_client
        print(f"Registered tool: `{tool['function']['name']}`")
    
    dial_client = DialClient(
        api_key=DIAL_API_KEY,
        endpoint="https://ai-proxy.lab.epam.com",
        tools=tools,
        tool_name_client_map=tool_name_client_map
    )

    messages = [
        Message(
            role=Role.SYSTEM,
            content="You are an assistant for handling user management operations. You have access to tools that allow you to create, update, delete, and search for users in the system. Use these tools to fulfill user requests related to user management."
        )
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        messages.append(Message(role=Role.USER, content=user_input))
        await dial_client.get_completion(messages)


if __name__ == "__main__":
    asyncio.run(main())


# Check if Arkadiy Dobkin present as a user, if not then search info about him in the web and add him