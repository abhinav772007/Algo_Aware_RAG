# Algo-Aware RAG Tutor

A hallucination-safe, algorithm-aware tutoring system that explains data structures and algorithms using Retrieval-Augmented Generation (RAG) with structured knowledge routing, self-evaluation, and multi-algorithm support.

**Unlike generic chatbots, this system does not hallucinate. If required knowledge is missing, it explicitly refuses to answer.**

## Features

- 🎯 **Algorithm-Aware**: Supports multiple algorithms including BFS, DFS, Binary Search, Dijkstra, Merge Sort, Sliding Window, Two Pointers, and Union Find
- 🔍 **Structured Knowledge Retrieval**: Retrieves information from categorized knowledge bases (theory, code, complexity, edge cases)
- 🛡️ **Hallucination-Safe**: Explicitly refuses to answer when knowledge is missing, preventing misinformation
- 📊 **Self-Evaluation**: Built-in evaluation system that checks completeness, relevance, and hallucination
- 🎨 **Dual Interfaces**: Command-line interface (`app.py`) and web-based Streamlit UI (`ui.py`)
- 🔄 **Query Decomposition**: Intelligently breaks down complex queries into sub-queries for better retrieval

## Installation

### Prerequisites

- Python 3.8 or higher
- Google API Key for Gemini (set as environment variable `GOOGLE_API_KEY`)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Algo-Aware-Rag/Algo_Aware_RAG
```

2. Install dependencies:
```bash
pip install streamlit faiss-cpu sentence-transformers google-genai numpy
```

3. Set up your Google API key:
```bash
# Windows PowerShell
$env:GOOGLE_API_KEY="your-api-key-here"

# Linux/Mac
export GOOGLE_API_KEY="your-api-key-here"
```

4. Build the vector indexes:
```bash
python ingest/build_indexes.py
```

This will create FAISS indexes for all knowledge categories (theory, code, complexity, edge_cases) in the `indexes/` directory.

## Usage

### Web Interface (Recommended)

Launch the Streamlit web application:

```bash
streamlit run ui.py
```

Then open your browser to the URL shown (typically `http://localhost:8501`).

### Command-Line Interface

Run the command-line version:

```bash
python app.py
```

Enter your algorithm question when prompted.

## Example Queries

- "Explain how BFS works"
- "Show me the implementation of binary search"
- "What is the time complexity of Dijkstra's algorithm?"
- "Explain BFS and Binary Search with their edge cases"
- "How does merge sort work? Show me the code and complexity"

## Project Structure

```
Algo_Aware_RAG/
├── app.py                 # Command-line interface
├── ui.py                  # Streamlit web interface
├── data/                  # Knowledge base (algorithms data)
│   ├── bfs/
│   ├── dfs/
│   ├── binary_search/
│   └── ...
├── rag/                   # RAG pipeline components
│   ├── classifier.py      # Classifies query needs
│   ├── decomposer.py      # Decomposes queries
│   ├── retriever.py       # Retrieves relevant context
│   ├── assembler.py       # Assembles context
│   ├── generator.py       # Generates answers using Gemini
│   └── splitter.py        # Splits multi-algorithm queries
├── evaluation/            # Evaluation modules
│   ├── evaluator.py       # Main evaluator
│   ├── completeness.py    # Completeness checks
│   ├── hallucination.py   # Hallucination detection
│   └── relevance.py       # Relevance scoring
├── ingest/                # Index building
│   └── build_indexes.py   # Builds FAISS indexes
└── indexes/               # Generated vector indexes
    ├── theory.index
    ├── code.index
    ├── complexity.index
    └── edge_cases.index
```

## How It Works

1. **Query Classification**: Determines what types of information are needed (theory, code, complexity, edge cases)
2. **Query Decomposition**: Breaks down the query into category-specific sub-queries
3. **Knowledge Retrieval**: Uses FAISS vector search to retrieve relevant context from structured knowledge bases
4. **Context Assembly**: Combines retrieved contexts from different categories
5. **Answer Generation**: Uses Google Gemini to generate structured answers based on retrieved context
6. **Evaluation**: Self-evaluates the answer for completeness, relevance, and hallucination

## Technologies Used

- **Google Gemini API**: For answer generation
- **FAISS**: Vector similarity search
- **Sentence Transformers**: Text embeddings (all-MiniLM-L6-v2)
- **Streamlit**: Web interface
- **Python**: Core implementation

## Knowledge Base

The system includes structured knowledge for the following algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Binary Search
- Dijkstra's Algorithm
- Merge Sort
- Sliding Window Technique
- Two Pointers Technique
- Union Find (Disjoint Set Union)

Each algorithm has four knowledge categories:
- **Theory**: Conceptual explanation
- **Code**: Implementation examples
- **Complexity**: Time and space complexity analysis
- **Edge Cases**: Important edge cases and considerations


