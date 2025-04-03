from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama2")

template = """
Your are an expert in answering question about a pizza restaurant

here are some relevant reviews: {reviews}
"""