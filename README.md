# 📰 NewsLens AI

**NewsLens AI** is a Multi-Agent AI-powered news analysis system built using **LangChain, Gemini, ChromaDB, Retrieval-Augmented Generation (RAG), and Streamlit**. The application helps users analyze news articles by generating concise summaries, detecting media bias, verifying factual consistency using retrieved knowledge, and performing safety analysis.

## 🚀 Live Demo
https://newslens-ai-production.up.railway.app/
---

# 🚀 Features

* 📝 AI-powered News Summarization
* ⚖️ Media Bias Detection
* ✅ Fact Verification using RAG
* 🛡️ Safety Analysis
* 📚 Retrieval-Augmented Generation (RAG)
* 🔍 Semantic Search using ChromaDB
* 🤖 Google Gemini Integration
* 🌐 Interactive Streamlit Interface

---

# 🏗️ Project Architecture

```text
User Input
     │
     ▼
Retrieve Relevant Context (ChromaDB)
     │
     ▼
Summarizer Agent
     │
     ├────────► Bias Agent
     ├────────► Verifier Agent
     └────────► Safety Agent
     │
     ▼
Display Results (Streamlit)
```

---

# 📂 Project Structure

```text
NewsLens-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── agents/
│   ├── summarizer.py
│   ├── bias_agent.py
│   ├── verifier.py
│   └── safety.py
│
├── rag/
│   ├── embeddings.py
│   ├── retrieve.py
│   └── vectordb.py
│
├── prompts/
│   ├── summary_prompt.py
│   ├── bias_prompt.py
│   ├── verifier_prompt.py
│   └── safety_prompt.py
│
├── data/
│   ├── news_docs/
│   └── embeddings/
│
└── utils/
```

---

# 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* Google Gemini API
* ChromaDB
* Google Generative AI Embeddings
* Retrieval-Augmented Generation (RAG)
* Python Dotenv

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/NewsLens-AI.git
cd NewsLens-AI
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key
GEMINI_MODEL=gemini-2.5-flash-lite
```

---

# 📚 Build the Vector Database

Run:

```bash
python -m rag.vectordb
```

This indexes the documents stored in:

```text
data/news_docs/
```

and creates the vector database inside:

```text
data/embeddings/
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# 📖 How It Works

1. User pastes a news article.
2. Relevant documents are retrieved from ChromaDB.
3. Retrieved context is combined with the article.
4. The Summarizer Agent generates a concise summary.
5. The Bias Agent analyzes potential media bias.
6. The Verifier Agent checks factual consistency using retrieved context.
7. The Safety Agent evaluates potentially unsafe or sensitive content.
8. Results are displayed in the Streamlit dashboard.

---

# 📸 Example Workflow

```
Paste News Article
        │
        ▼
Retrieve Context
        │
        ▼
Generate Summary
        │
        ▼
Bias Detection
        │
        ▼
Fact Verification
        │
        ▼
Safety Analysis
        │
        ▼
Display Results
```

---

# 🎯 Future Improvements

* Trust Score Generation
* Sentiment Analysis
* News Category Classification
* PDF Report Export
* Source Attribution
* Multi-language Support
* Real-time News Integration

---

# 👩‍💻 Author

**Pratishtha Singh**

Built as a GenAI + Multi-Agent + RAG project using LangChain and Google Gemini.

---

# 📄 License

This project is intended for educational and learning purposes.
