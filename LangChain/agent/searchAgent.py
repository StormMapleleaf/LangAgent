# Import relevant functionality
from model import model
from langchain_core.messages import HumanMessage
from langchain_community.tools.tavily_search import TavilySearchResults

# Create a search tool using Tavily
search = TavilySearchResults(max_results=2)
search_results = search.invoke("旧金山今天的天气怎么样？")
print(search_results)
tools = [search]

# 模型调用工具
model_with_tools = model.bind_tools(tools)

response = model_with_tools.invoke([HumanMessage(content="旧金山今天的天气怎么样？")])

# print(f"ContentString: {response.content}")
# print(f"ToolCalls: {response.tool_calls}")
print(response)