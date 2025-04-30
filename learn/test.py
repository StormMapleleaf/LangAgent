from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="deepseek-r1:1.5b")

print(llm.invoke("The first man on the moon was..."))