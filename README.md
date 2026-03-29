# 🚀 RAG-Based Question Generator

A Retrieval-Augmented Generation (RAG) based system that generates high-quality questions from input topics or text using vector search and Large Language Models (LLMs).

---

## 📌 Overview

This project leverages a modular RAG pipeline to generate meaningful and context-aware questions. It combines semantic search (via vector embeddings) with LLM-based generation to produce relevant and structured questions.

---

## 🧠 Features

* 🔍 Semantic retrieval using vector embeddings
* ⚡ Integration with Pinecone for fast vector search
* 🤖 LLM-based question generation (Gemini/OpenAI)
* 🧩 Modular architecture (easy to extend and maintain)
* ✅ Question validation and classification
* 🔒 Secure API key handling using environment variables

---

## 🏗️ Project Structure

```
rag-question-generator/
│
├── app/
│   ├── services/
│   │   ├── embedder.py        # Generates embeddings
│   │   ├── retriever.py       # Retrieves relevant context (Pinecone)
│   │   ├── generator.py       # Generates questions using LLM
│   │   ├── classifier.py      # Classifies question type
│   │   └── validator.py       # Validates generated questions
│   │
│   ├── utils/
│   │   ├── safe_gemini.py     # Safe wrapper for LLM calls
│   │   └── text_utils.py
│   │
│   └── config.py              # Environment & configuration
│
├── main.py                    # Entry point
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Tech Stack

* **Python**
* **Pinecone** (Vector Database)
* **LLMs** (Gemini / OpenAI)
* **Embeddings** (Sentence Transformers / similar)
* **FastAPI / Script-based backend**

---

## 🔄 How It Works

1. User provides input text or topic
2. Text is converted into embeddings
3. Relevant context is retrieved from Pinecone
4. LLM generates questions using retrieved context
5. Questions are classified and validated

---

## 📥 Example

**Input:**

```
Machine Learning Basics
```

**Output:**

```
1. What is supervised learning?
2. What is the difference between overfitting and underfitting?
3. Explain the concept of training and testing data.
```

---

## 🚀 Getting Started

### 1. Clone the repository

```
git clone https://github.com/yourusername/RAG-Based-Question-Generator.git
cd RAG-Based-Question-Generator
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file using `.env.example`:

```
PINECONE_API_KEY=your_key_here
PINECONE_HOST=your_host_here
GEMINI_API_KEY=your_key_here
```

---

### 5. Run the project

```
python main.py
```

---

## 🔐 Security

* API keys are stored securely using environment variables
* `.env` file is excluded from version control

---

## 🎯 Future Improvements

* Add web interface (Streamlit/React)
* Support multiple question types (MCQ, subjective)
* Improve ranking and filtering of generated questions
* Add evaluation metrics for question quality

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📬 Contact

For queries or collaboration, feel free to reach out.

---

⭐ If you found this project useful, consider giving it a star!
