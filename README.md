# -mini-rag-assistant

📄 Mini RAG Assistant

A lightweight Retrieval-Augmented Generation (RAG) system that allows you to index a PDF and ask questions about its content using semantic search and an LLM.

⸻

🚀 Features
	•	📄 Index any PDF file
	•	✂️ Automatic text chunking
	•	🧠 Sentence embeddings using all-MiniLM-L6-v2
	•	🔎 FAISS vector search for semantic retrieval
	•	🤖 LLM-powered answers (Perplexity API)
	•	🧹 Clean formatted output (removes SDK artifacts)
	•	🔁 Multi-question session support
	•	📝 Automatic logging of all Q&A to file

⸻

🏗️ Architecture

PDF
  ↓
Text Extraction
  ↓
Chunking
  ↓
Embeddings (MiniLM)
  ↓
FAISS Index
  ↓
User Question → Embedding
  ↓
Top-K Similar Chunks Retrieved
  ↓
LLM Generates Answer
  ↓
Clean Output + Logged to File


⸻

📦 Project Structure

mini-rag-assistant/
│
├── main.py
├── src/
│   ├── loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── search.py
│   └── query_llm.py
│
├── data/
│   └── docs/
│
├── logs/
│
└── README.md


⸻

⚙️ Installation
	1.	Clone the repository:

git clone <your-repo-url>
cd mini-rag-assistant

	2.	Install dependencies:

pip install -r requirements.txt

	3.	Set your Perplexity API key:

export PERPLEXITY_API_KEY="your_api_key_here"

(Or configure it in your environment variables.)

⸻

🛠️ Usage

1️⃣ Build the index

python3 main.py

Then type:

build

Enter the path to your PDF:

data/docs/test.pdf

This creates a FAISS index from your document.

⸻

2️⃣ Ask questions

Run:

python3 main.py

Then type:

ask

You can now ask multiple questions.

Type:

exit

to end the session.

⸻

📝 Logging

All answers are automatically saved to:

logs/<pdf_name>_answers.txt

Each entry includes:
	•	Timestamp
	•	Question
	•	Clean formatted answer

⸻

🧠 Technologies Used
	•	Python
	•	FAISS (Facebook AI Similarity Search)
	•	Sentence Transformers
	•	HuggingFace
	•	Perplexity API
	•	Regular expressions for output cleaning

⸻

📌 Notes
	•	The embeddings.position_ids | UNEXPECTED warning is normal and can be ignored.
	•	Output is cleaned automatically to remove:
	•	[conversation_history:0]
	•	[web:2] style references
	•	Multi-question sessions are supported in a single run.

⸻

🔮 Future Improvements
	•	Strict document-only grounding mode
	•	Web UI with Streamlit
	•	PDF export of answers
	•	Conversation memory across sessions
	•	Metadata storage (page numbers, chunk IDs)
	•	Deployment as an online app

⸻

👨‍💻 Author

Built as a learning project to understand:
	•	RAG systems
	•	Embeddings
	•	Semantic search
	•	LLM integration
	•	AI system architecture

⸻
