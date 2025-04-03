from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama2")

template = """
Your are an expert in answering question about a pizza restaurant

here are some relevant reviews: {reviews}
here is the questio to answer: {queestion}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


while True:
    question = input("ask your question (q to quit): ")
    if question == "q":
        break

result = chain.invoke({"review": [], "question": question})
print(result)