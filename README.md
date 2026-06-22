# 🤖 AI Academic Assistant

A Retrieval-Augmented Generation (RAG) based AI assistant that allows users to upload documents (PDFs) and interact with them using natural language. The system extracts information from uploaded documents, creates embeddings, stores them in a vector database, and generates intelligent answers using Large Language Models.

---

## 🚀 Project Overview

AI Academic Assistant is a GenAI-powered learning assistant designed to help students understand study materials faster.

Users can:

- Upload PDF documents
- Ask questions from their documents
- Get AI-generated answers
- Maintain user accounts
- Store chat history
- Access the system through APIs and frontend interface

The project uses **RAG (Retrieval Augmented Generation)** architecture to provide accurate answers based on uploaded content.

---

# 🏗️ System Architecture

             User
              |
              |
        Frontend UI
              |
              |
          FastAPI
              |
  ------------------------
  |                      |

  Authentication RAG Pipeline
| |
SQLite DB ChromaDB
|
Embeddings Model
|
LLM Model



---

# ✨ Features

## 🔐 Authentication

- User Registration
- User Login
- JWT Authentication
- Secure password hashing


## 📄 Document Processing

- Upload PDF files
- Extract text from documents
- Split text into chunks
- Generate embeddings
- Store vectors in ChromaDB


## 🧠 AI Question Answering

- Ask questions from uploaded PDFs
- Retrieve relevant document sections
- Generate context-aware answers


## 💾 Database

Stores:

- User information
- Chat history
- Sessions


---

# 🛠️ Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication


## AI / Machine Learning

- Retrieval Augmented Generation (RAG)
- ChromaDB
- Sentence Transformers
- LLM Integration
- Embeddings


## Frontend

- HTML
- CSS
- JavaScript



