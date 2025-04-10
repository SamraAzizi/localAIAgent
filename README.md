# 🍕 Pizza Restaurant QA Chatbot (LangChain + Ollama + Chroma)

This project is a simple conversational chatbot that answers questions about a pizza restaurant based on realistic customer reviews. It uses:

- **LangChain** for chaining the logic,
- **Ollama models** for embeddings and language understanding,
- **ChromaDB** for storing and retrieving relevant reviews using semantic similarity.

## 📁 Project Structure
├── main.py                                # Main chatbot loop 
├── vector.py                              # Vector store setup using Chroma and Ollama embeddings 
├── realistic_restaurant_reviews.csv       # Dataset of restaurant reviews 
├── chrome_langchain_db/                   # Folder where vector DB is persisted 
└── README.md                               # This file


## 🛠 Requirements

Install the dependencies using pip:

```bash
pip install langchain langchain-core langchain-ollama langchain-chroma pandas

```

Also, make sure you have Ollama installed and running locally with the required models:

- `llama2`
- `mxbai-embed-large`

You can pull them using:

```bash
ollama pull llama2
ollama pull mxbai-embed-large
```


## Dataset

The chatbot uses a CSV file named realistic_restaurant_reviews.csv with the following columns:

- Title
- Review
- Rating
- Date

Make sure this file is in the root directory before running the project.

## How To Run 
First, run vector.py to set up the vector store and load reviews (only once):

```bash

python vector.py
```
Then, start the chatbot using:

```bash
python main.py
```

Ask your questions about the pizza restaurant like:

```bash
ask your question (q to quit): What do people think about the service?
```

## How it Works
- Embeddings: Reviews are embedded using mxbai-embed-large.
- Vector Store: Embedded documents are stored and retrieved using Chroma.
- Prompting: A custom prompt combines retrieved reviews and the user’s question.
- LLM: llama2 is used to generate a relevant answer.

## Notes
- This app currently uses local Ollama models, so no API key is needed.
- The vector store is saved in chrome_langchain_db/, so embeddings are not recalculated every time.
- You can extend this by using a web interface or adding structured question understanding.

## Example Questions
- "Are the pizzas good here?"
- "How is the ambiance?"
- "Do people like the service?"
- "Is the restaurant clean?"