# DocQuery AI
DocQuery AI is an AI-powered document question-answering system that enables users to upload PDF documents and ask questions in natural language. The system uses Retrieval-Augmented Generation (RAG), semantic search, vector embeddings, and Google's Gemini LLM to generate accurate answers from uploaded documents.

## Features

* Upload PDF documents
* Extract text using PyPDF2
* Automatic document chunking
* Generate embeddings using Sentence Transformers
* Store embeddings in FAISS vector database
* Semantic search for relevant document retrieval
* Gemini LLM integration for intelligent answer generation
* Query history storage using SQLite
* FastAPI backend APIs
* React-based frontend interface

## Tech Stack

### Backend
* Python
* FastAPI
* PyPDF2
* Sentence Transformers
* FAISS
* SQLite
* Gemini API

### Frontend
* React
* Vite
* Axios
* CSS

---

## Project Architecture
User Upload PDF
→ Text Extraction
→ Document Chunking
→ Embedding Generation
→ FAISS Vector Storage
→ User Query
→ Semantic Search
→ Relevant Context Retrieval
→ Gemini LLM
→ Final Answer

---

## Installation
### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

Run Backend:

```bash
uvicorn main:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```




## Author

Divya Sharma

B.Tech Computer Science Engineering
