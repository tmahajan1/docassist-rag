DocAssist: Intelligent Documentation Assistant (RAG-based)

🧠 Problem

In a cloud platform environment, engineers struggled to find relevant solutions in internal documentation.

This led to:
	•	High dependency on senior engineers / SMEs
	•	Large number of repetitive and low-quality support tickets
	•	Slower issue resolution
	•	Reduced productivity

The existing system relied on keyword-based search, which often failed to capture the actual intent behind queries.

⸻

🎯 Solution

Built a Retrieval-Augmented Generation (RAG) system to enable semantic search and conversational querying over internal documentation.

The system retrieves relevant information and generates answers grounded in documentation.

🏗️ Architecture
User → CLI Interface → RAG Pipeline

RAG Pipeline:
- Document Loading
- Chunking
- Embedding
- Vector Retrieval
- Prompt Construction
- LLM Response

⚙️ How It Works
	1.	Documents are loaded from the docs/ folder
	2.	Documents are split into smaller chunks
	3.	Each chunk is converted into an embedding vector
	4.	Query is also embedded
	5.	Top relevant chunks are retrieved using similarity search
	6.	Prompt is built using retrieved context
	7.	LLM generates a grounded answer


▶️ How to Run

pip install -r requirements.txt
python app/main.py

📌 Example Queries
	•	How to create NFS share?
	•	How is SMB diferent from NFS?
	•	Common issues while mounting SMB share?
