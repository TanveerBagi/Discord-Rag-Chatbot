# Discord-Rag-Chatbot


A smart Discord chatbot that uses Retrieval-Augmented Generation (RAG) to answer user queries by retrieving relevant data from documents and generating concise responses using a DeepSeek LLM.

---

## 🚀 Features

- 🔗 Connects directly to Discord via bot commands
- 📚 Retrieves document content using ChromaDB vector store
- 🧠 Uses sentence-transformer embeddings (`all-MiniLM-L6-v2`)
- 🤖 Responds to queries using an integrated LLM
- 📊 Integrated with Prometheus for observability metrics
- 📁 Supports `.docx` documents

---

## 📂 Project Structure

<pre> ``` Discord-RAG-Chatbot/ ├── main.py # Discord bot handler ├── llm.py # RAG logic: retrieval + LLM response ├── database.py # Document parsing & vector DB storage ├── observability_metrics.py # Prometheus metrics ├── requirements.txt # Project dependencies ├── logs/ # Logging output └── documents/ # DOCX files for knowledge base ``` </pre>


---

## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/discord-rag-chatbot.git
cd discord-rag-chatbot
```
### 2. Install dependencies
```bash
git clone https://github.com/your-username/discord-rag-chatbot.git
cd discord-rag-chatbot
```
NOTE:- The project needs Python3.10 or higher to run properly

### 3. Prepare Documents
Place your .docx files inside the documents/ folder.

### 4. Run 



