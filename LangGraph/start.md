## requirements
```
Python >= 3.11
LangGraph CLI: Requires langchain-cli[inmem] >= 0.1.58
```
## base env
```
conda create -n langgraph python=3.11
conda activate langgraph
pip install --upgrade "langgraph-cli[inmem]"
```

## Create a LangGraph App
```
#从react 模板创建简单应用
langgraph new ./app --template react-agent-python

#Install Dependencies
cd app
pip install -e .

#Copy .env.example to .env
填写对应 API 密钥
```

## Launch LangGraph Server
```
#启动API 服务
langgraph dev

API:http://localhost:2024
Docs: http://localhost:2024/docs
LangGraph Studio Web UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```