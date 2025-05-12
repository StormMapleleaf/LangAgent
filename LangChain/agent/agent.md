## Build an Agent

## base env 
```
pip install -qU "langchain[openai]"
pip install -U langchain-community langgraph tavily-python langgraph-checkpoint-sqlite
```

## API
```
export TAVILY_API_KEY="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"
```

## model
需要模型及其服务支持工具调用
```
vllm serve ./Llama-3.2-1B/ --served-model-name gemma --api-key password --port 8000 --max-model-len 4096 --enable-auto-tool-choice --tool-call-parser llama3_json --chat-template ~/LLM/vllm/examples/tool_chat_template_llama3.2_json.jinja
```

## 定义工具
```
from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults(max_results=2)
search_results = search.invoke("what is the weather in SF")
print(search_results)
# If we want, we can create other tools.
# Once we have all the tools we want, we can put them in a list that we will reference later.
tools = [search]
```