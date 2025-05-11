## base env
```
pip install -U langsmith openai
```
## Create an API key
https://smith.langchain.com/


## Set up your environment
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY="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"
#The example uses OpenAI, but it's not necessary if your code uses another LLM provider
export OPENAI_API_KEY="password"