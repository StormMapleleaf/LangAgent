from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI

# 模型实例化
inference_server_url = "http://localhost:8000/v1"

model = ChatOpenAI(
    model="gemma",
    openai_api_key="password",
    openai_api_base=inference_server_url,
    max_tokens=256,
    temperature=0,
)

# 单次对话
# model.invoke([HumanMessage(content="你好")])

# 上下文记忆对话原理
# from langchain_core.messages import AIMessage

# print(model.invoke(
#     [
#         HumanMessage(content="Hi! I'm Bob"),
#         AIMessage(content="Hello Bob! How can I assist you today?"),
#         HumanMessage(content="What's my name?"),
#     ]
# ))

