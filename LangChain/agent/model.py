from langchain_openai import ChatOpenAI

# 模型实例化
inference_server_url = "http://localhost:8000/v1"

model = ChatOpenAI(
    model="gemma",
    openai_api_key="password",
    openai_api_base=inference_server_url,
    max_tokens=1024,
    temperature=0,
    model_kwargs={
        "functions": [
            {
                "enable_auto_tool_choice": True,
                "tool_call_parser": True
            }
        ]
    }
)
