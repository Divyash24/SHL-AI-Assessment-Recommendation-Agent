# SHL AI Assessment Recommendation Agent

An AI-powered assessment recommendation system developed for the **SHL Generative AI Internship Assignment**.

The application recommends the most relevant SHL assessments based on hiring requirements using **Retrieval-Augmented Generation (RAG)**, **FAISS Vector Search**, **Sentence Transformers**, **Google Gemini**, and **FastAPI**.

---

# Features

- AI-powered SHL assessment recommendations
- Retrieval-Augmented Generation (RAG)
- Semantic search using FAISS
- Sentence Transformer embeddings
- Google Gemini 2.5 Flash integration
- Multi-turn conversation support
- Follow-up question generation for incomplete hiring requirements
- FastAPI REST API
- SHL API specification compliant response format

---

# Tech Stack

- Python 3.12
- FastAPI
- Google Gemini API
- Sentence Transformers
- FAISS
- NumPy
- Pydantic
- python-dotenv

---

# Project Structure

```
SHL AI AGENT/
│
├── app/
│   ├── models/
│   │   ├── request.py
│   │   └── response.py
│   │
│   ├── rag/
│   │   ├── embeddings.py
│   │   ├── loader.py
│   │   ├── preprocessor.py
│   │   ├── prompts.py
│   │   └── retriever.py
│   │
│   ├── services/
│   │   ├── chat_service.py
│   │   └── gemini_services.py
│   │
│   ├── api.py
│   └── config.py
│
├── data/
│   ├── shl_product_catalog.json
│   └── shl_product_catalog_clean.json
│
├── evaluation/
│   └── public_traces/
│
├── scripts/
│   ├── build_index.py
│   ├── test_gemini.py
│   └── test_retriever.py
│
├── vector_store/
│   ├── faiss.index
│   └── metadata.pkl
│
├── docs/
├── main.py
├── requirements.txt
├── README.md
└── .env
```

---

# Architecture

```
                 User Query
                      │
                      ▼
               FastAPI (/chat)
                      │
                      ▼
          Multi-turn Conversation Handler
                      │
                      ▼
      Sentence Transformer Embeddings
                      │
                      ▼
             FAISS Vector Search
                      │
                      ▼
        Top Relevant SHL Assessments
                      │
                      ▼
        Google Gemini (Answer Generation)
                      │
                      ▼
             Final Recommendation
```

---

# API Endpoints

## GET /

Returns the API status.

Example Response

```json
{
  "message": "SHL AI Recommendation API is running 🚀"
}
```

---

## GET /health

Returns application health status.

Example Response

```json
{
  "status": "ok"
}
```

---

## POST /chat

### Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a Backend Software Engineer with 5 years of experience."
    }
  ]
}
```

### Response

```json
{
  "reply": "Recommended assessments...",
  "recommendations": [
    {
      "name": "C++ Programming (New)",
      "url": "https://www.shl.com/...",
      "test_type": "Assessment"
    }
  ],
  "end_of_conversation": true
}
```

---

# Multi-turn Conversation

The application supports multi-turn conversations.

When sufficient hiring information is unavailable, the assistant asks follow-up questions instead of returning recommendations.

Example:

User:

```
I want to hire a developer.
```

Assistant:

```
Which role are you hiring for?
```

User:

```
Java Developer
```

Assistant:

```
What experience level are you hiring for?
```

User:

```
Around 5 years.
```

Assistant:

Returns the recommended SHL assessments.

---

# Retrieval Pipeline

1. Load SHL Product Catalog
2. Clean and preprocess assessment data
3. Generate sentence embeddings
4. Store embeddings in FAISS
5. Retrieve Top-K relevant assessments
6. Generate final recommendation using Google Gemini

---

# Running the Project

## Clone Repository

```bash
git clone <repository-url>
cd SHL-AI-AGENT
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Build Vector Store

```bash
python scripts/build_index.py
```

---

## Run Server

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# Future Improvements

- Hybrid retrieval using BM25 + FAISS
- Assessment reranking
- Streaming Gemini responses
- Docker deployment
- Persistent conversation memory

---

# Author

**Divyash Saxena**

B.Tech Computer Science (AI & ML)

JSS Academy of Technical Education, Noida

---

# License

This project was developed as part of the SHL Generative AI Internship Assignment.