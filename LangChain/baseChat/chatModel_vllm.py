from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI

# 模型实例化
inference_server_url = "http://localhost:8000/v1"

llm = ChatOpenAI(
    model="gemma",
    openai_api_key="password",
    openai_api_base=inference_server_url,
    max_tokens=512,
    temperature=0,
)

# 模型调用
messages = [
    SystemMessage(
        content="You are a helpful Chinese assistant."
    ),
    HumanMessage(
        content="请解释什么是张量并行，什么是流水并行。"
    ),
]
# print(llm.invoke(messages))

# # 模板链接调用
# from langchain_core.prompts import ChatPromptTemplate

# prompt = ChatPromptTemplate(
#     [
#         (
#             "system",
#             "You are a helpful assistant that translates {input_language} to {output_language}.",
#         ),
#         ("human", "{input}"),
#     ]
# )

# chain = prompt | llm

# print(chain.invoke(
#     {
#         "input_language": "English",
#         "output_language": "Chinese",
#         "input": "I love programming.",
#     }
# ))

# 流式输出
for token in llm.stream(messages):
    print(token.content, end="")