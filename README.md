# 🍕 Pizza Restaurant QA Chatbot (LangChain + Ollama + Chroma)

This project is a simple conversational chatbot that answers questions about a pizza restaurant based on realistic customer reviews. It uses:

- **LangChain** for chaining the logic,
- **Ollama models** for embeddings and language understanding,
- **ChromaDB** for storing and retrieving relevant reviews using semantic similarity.

## 📁 Project Structure
├── main.py # Main chatbot loop 
├── vector.py # Vector store setup using Chroma and Ollama embeddings 
├── realistic_restaurant_reviews.csv # Dataset of restaurant reviews 
├── chrome_langchain_db/ # Folder where vector DB is persisted 
└── README.md # This file


## 🛠 Requirements

Install the dependencies using pip:

```bash
pip install langchain langchain-core langchain-ollama langchain-chroma pandas