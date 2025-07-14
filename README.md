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

## 💡 How RAG Works (Quick Overview)
- User asks a question on Discord.
- Bot retrieves relevant document chunks from ChromaDB using embeddings.
- Retrieved context + query is passed to the LLM.
- LLM returns a complete, context-aware answer.

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
NOTE:- The project needs Python 3.10 or higher to run properly

### 3. Prepare Documents
Place your .docx files inside the documents/ folder.

### 4. Run database.py file after adding the necessary directories in the file
Run this file once for storing embeddings in the database

### 5. Add the requesty API key in the llm.py file

### 6. Add the Bot Token in the main.py file

### 7.Run metrics server
```bash
python observability_metrics.py
```
This exposes metrics at http://localhost:8000/metrics.

### 8. Start Prometheus
Configure Prometheus (prometheus.yml):
```yaml
global:
  scrape_interval: 5s
scrape_configs:
  - job_name: 'discord_rag_bot'
    static_configs:
      - targets: ['localhost:8000']
```

Run:
```bash
prometheus.exe --config.file=prometheus.yml
```

### 9. Run the bot
In the project directory terminal
```bash
python main.py
```

### 10. Interact on Discord
#Nexus <your question>

## 📊 Observability Metrics
This project uses Prometheus to monitor and expose key application metrics via an HTTP endpoint.

🔍 Metrics Tracked
Metric Name	Description:
user_query_count :	Total number of user queries processed
query_duration_seconds : Time taken (in seconds) to process a query

## 📍 Access the metrics at:
http://localhost:8000/metrics

These metrics can be scraped by Prometheus and visualized using Grafana or another dashboard tool.

##🧾 Logging
Logs help track application health and debugging information. This project uses the logging module along with rich for colorful console logs.

## 📁 Log Details
All logs are written to:
logs/chatbot.log

## 📝 Logged Information
- ✅ Incoming user queries
- 📄 Document deliverd successfully or not
- ⏱ Query latency
- ❗ API or system errors

The logs include timestamps and log levels (INFO, ERROR, etc.) for better traceability.
