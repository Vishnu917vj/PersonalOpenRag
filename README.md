# 🚀 Personal Open RAG

A lightweight, production-ready Retrieval-Augmented Generation (RAG) API built with **FastAPI**, **Pinecone**, **OpenRouter**, and a **self-hosted BAAI embedding service**. This project is designed to build your own personal AI assistant over custom data with a simple and extensible architecture.

## ✨ Features

* 🚀 FastAPI REST API
* 🔍 Semantic Search using Pinecone
* 🤖 OpenRouter Free Models for response generation
* 🧠 Self-hosted BAAI embedding service
* 📚 Simple document ingestion API
* 📄 Retrieval with source attribution
* ⚡ Lightweight architecture with no conversation memory
* 🐳 Docker support for easy deployment

---

## 🏗️ Architecture

The workflow is intentionally simple:

```text
User Question
      │
      ▼
Generate Query Embedding
(Self-hosted BAAI Model)
      │
      ▼
Pinecone Vector Search
(Top 10 Similar Chunks)
      │
      ▼
Build Prompt
(Context + User Question)
      │
      ▼
OpenRouter Free LLM
      │
      ▼
Answer + Retrieved Sources
```

There is **no conversation memory**, **no agents**, and **no complex pipelines**—just a clean and efficient RAG workflow.

---

## 🛠 Tech Stack

* FastAPI
* Python
* Pinecone Vector Database
* OpenRouter
* Self-hosted BAAI Embedding API
* Docker
* Railway

---

## 📂 Dataset

The repository already contains a sample personal dataset:

```
cleaned_data.xlsx
```

which contains Question/Answer pairs.

To convert and ingest this dataset into Pinecone, simply use:

```
ingest_data.py
```

This script prepares the dataset in the correct format for the indexing API.

---

## 🌐 Live Services

### Personal Open RAG API

https://personalopenrag-production.up.railway.app

---

### Self-hosted Embedding Service

https://openembedd-production.up.railway.app/

Repository:

https://github.com/Vishnu917vj/OpenEmbedd

The embedding service uses:

```
BAAI/bge-small-en-v1.5
```

which produces **384-dimensional embeddings**.

---

## 🧠 Vector Database

This project uses **Pinecone**.

Current configuration:

* Vector Dimension: **384**
* Metric: **Cosine Similarity**
* Retrieval: **Top 10 Similar Chunks**

---

## 🤖 LLM

Responses are generated using **OpenRouter's free models**.

The LLM receives:

* User Question
* Top 10 Retrieved Chunks

and generates the final answer.

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Vishnu917vj/PersonalOpenRag.git

cd PersonalOpenRag
```

---

## 2. Create a Virtual Environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file and add the following variables.

```env
APP_NAME=Personal Open RAG
APP_VERSION=1.0.0
DEBUG=True

OPENROUTER_API_KEY=

OPENROUTER_MODEL=

EMBEDDING_API=

PINECONE_API_KEY=

PINECONE_INDEX=

PINECONE_CLOUD=

PINECONE_REGION=
```

### Required Variables

* OPENROUTER_API_KEY
* EMBEDDING_API
* PINECONE_API_KEY
* PINECONE_INDEX

---

## 5. Run the Application

```bash
fastapi dev app/main.py
```

or

```bash
uvicorn app.main:app --reload
```

---

## 6. Open Swagger UI

```
http://localhost:8000/docs
```

From here you can test every endpoint directly from your browser.

---

# 📚 API Endpoints

## Health Check

```
GET /health
```

Checks whether the API is running correctly.

---

## Index Documents

```
POST /index
```

Indexes custom documents into Pinecone.

### Request

```json
{
    "namespace": "default",
    "documents": [
        {
            "id": "1",
            "text": "Question: What's your name?\nAnswer: My name is Vishnu."
        }
    ]
}
```

### Schema

```python
class Document(BaseModel):
    id: str
    text: str

class IndexRequest(BaseModel):
    namespace: str = "default"
    documents: list[Document]
```

### Response

```json
{
    "indexed": 1,
    "namespace": "default"
}
```

---

## Chat

```
POST /chat
```

Ask questions against your indexed knowledge base.

### Request

```json
{
    "message": "What's your name?",
    "namespace": "default"
}
```

### Response

```json
{
    "answer": "My name is Vishnu Amarapu.",
    "sources": [
        {
            "id": "1",
            "score": 0.93,
            "text": "Question: What's your name?\nAnswer: My name is Vishnu Amarapu."
        }
    ]
}
```

### Response Schema

```python
class Source(BaseModel):
    id: str
    score: float
    text: str

class RAGResponse(BaseModel):
    answer: str
    sources: list[Source]
```

---

# 📦 Deployment

This project can be deployed easily on Railway using the included Dockerfile.

Required environment variables should be configured in the Railway dashboard.

---

# 🔧 Customization

This project is intentionally generic and can be used for any custom RAG application.

Simply replace the dataset with your own Question/Answer pairs (or any short text snippets), index them into Pinecone, and start querying your personalized knowledge base.

Examples include:

* Personal AI Assistant
* Company Knowledge Base
* FAQ Bot
* Resume Assistant
* Product Documentation Search
* Internal Support Assistant

---

# Future Improvements

Some ideas for extending this project:

* Streaming Responses
* Hybrid Search
* Metadata Filtering
* Conversation Memory
* Authentication
* Admin Dashboard
* Web UI
* File Upload & Automatic Indexing
* Batch Embedding
* Re-ranking Models

---

# License

This project is open-source and intended as a simple reference implementation for building custom Retrieval-Augmented Generation (RAG) systems using FastAPI, Pinecone, OpenRouter, and self-hosted embeddings.

Contributions and improvements are welcome!
