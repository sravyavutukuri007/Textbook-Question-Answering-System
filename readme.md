# 📘 Textbook Question Answering System (RAG)

## 📌 Overview

This project is a **Textbook Question Answering System** built using a **Retrieval-Augmented Generation (RAG)** approach.
It allows users to ask questions in natural language and receive accurate answers **strictly based on the content of a given textbook PDF**.

Instead of training a model from scratch, the system retrieves relevant sections from the textbook and uses a language model to generate clear, contextual answers. This makes the system efficient, reliable, and suitable for large documents.

---

## ✨ Features

* Ask **conceptual, factual, and descriptive** questions
* Answers are generated **only from the textbook**
* Handles **unseen questions** if related concepts exist
* Uses **semantic search** for accurate retrieval
* Paragraph-based, easy-to-understand answers
* Simple and interactive **Streamlit web interface**

---

## 🛠️ Tech Stack

* **Python**
* **LangChain & LangGraph** – RAG workflow and tool-based reasoning
* **OpenAI API (GPT-4o-mini)** – Answer generation
* **OpenAI Embeddings** – Text vectorization
* **FAISS** – Vector database for similarity search
* **PyPDFLoader** – PDF loading and processing
* **Streamlit** – Frontend interface

---

## ⚙️ How the System Works

1. The textbook PDF is loaded and split into smaller chunks.
2. Each chunk is converted into vector embeddings.
3. Embeddings are stored in a FAISS vector database.
4. When a user asks a question:
   * Relevant chunks are retrieved using semantic search.
   * The retrieved context is passed to the language model.
5. The model generates an answer **based only on the retrieved content**.
6. The answer is displayed in the Streamlit interface.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-github-repo-url>
cd rag_langgraph_demo
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add OpenAI API Key

Add your API key directly inside `rag_pipeline.py`:

```python
import os
os.environ["OPENAI_API_KEY"] = "your_api_key_here"
```

*(For demo purposes only. Do not expose keys in public repositories.)*

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📂 Project Structure

```
rag_langgraph_demo/
│
├── app.py                 # Streamlit frontend
├── rag_pipeline.py        # RAG backend logic
├── chapters_1_to_15.pdf   # Textbook PDF
├── requirements.txt
├── venv/
└── README.md
```

---

## 📌 Use Cases

* Textbook-based learning assistants
* Exam preparation tools
* Academic content exploration
* Digital study companions

---

## 📝 Notes

* The system does **not train a new model**.
* Answers are generated using a **retrieval-based approach**.
* Works efficiently on standard hardware.

---

## 📄 License

This project is intended for **educational and demonstration purposes**.

---

