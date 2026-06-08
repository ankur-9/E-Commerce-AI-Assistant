# 🛒 E-Commerce AI Assistant (Gen AI RAG project using LLama3.3 and GROQ)

This is POC of an intelligent chatbot tailored for an e-commerce platform, enabling seamless user interactions by accurately identifying the intent behind user queries. It leverages real-time access to the platform's database, allowing it to provide precise and up-to-date responses.

The assistant can:

* 💬 Answer customer FAQs using Retrieval-Augmented Generation (RAG)
* 🔍 Search products using natural language queries
* 🧠 Automatically identify user intent and route requests to the appropriate workflow

---

## 🚀 Features

### 💬 FAQ Assistant (RAG-Based)

Handles customer support and policy-related questions.

#### Example Queries

* Is online payment available?
* What is the return policy?
* How long does delivery take?

#### How It Works

✅ FAQ data stored in CSV

✅ Embeddings generated and stored in ChromaDB

✅ Semantic similarity search retrieves relevant FAQs

✅ Context passed to Groq LLM

✅ Natural language answer generated

---

### 🛍️ Product Search Assistant (Text-to-SQL)

Allows users to search products using conversational language.

#### Example Queries

* Show me all Nike shoes below ₹3000
* List Samsung phones under ₹20,000
* Show laptops with 16GB RAM

#### How It Works

✅ LLM converts natural language into SQL

✅ SQL executed on product database

✅ Matching products retrieved

✅ Product data provided as context

✅ LLM generates user-friendly response

---

### 🧠 Intent Classification

The chatbot automatically determines user intent using **Semantic Router**.

| Intent  | Description                         |
| ------- | ----------------------------------- |
| 💬 FAQ  | Policy & platform-related questions |
| 🛍️ Product | Product search and database queries |

---

## 🏗️ System Architecture

```text
User Query
    │
    ▼
🧠 Semantic Router
    │
 ┌──┴─────────────┐
 │                │
 ▼                ▼

💬 FAQ Route     🛍️ SQL Route

ChromaDB         Text-to-SQL
Similarity       Generation
Search

Retrieve FAQ     Execute SQL

Generate         Retrieve Products
Answer

        ▼
 🤖 Groq LLM
        ▼
 Final Response
```

---

## 🛠️ Tech Stack

### 🤖 Generative AI

* Groq LLM
* ChromaDB
* Semantic Router
* Embeddings
* Prompt Engineering

### 💻 Backend

* Python
* SQLite

### 🎨 Frontend

* Streamlit

### 📊 Data Processing

* Pandas
* CSV Processing

### 🌐 Data Collection

* Web Scraping (Flipkart Product Dataset)

---

## 🎯 Key GenAI Concepts Demonstrated

* 🔹 Retrieval-Augmented Generation (RAG)
* 🔹 Vector Embeddings
* 🔹 Semantic Search
* 🔹 Intent Classification
* 🔹 Text-to-SQL
* 🔹 Prompt Engineering
* 🔹 Context Grounding
* 🔹 LLM-Powered Conversational Interfaces

---

## 📂 Project Structure

```text
project/
│
├── app/
│   ├── main.py              # Streamlit application entry point
│   ├── router.py            # Intent classification using Semantic Router
│   ├── faq.py               # FAQ retrieval pipeline using ChromaDB
│   ├── sql.py               # Text-to-SQL workflow and product retrieval
│   │
│   └── resources/
│       └── faq_data.csv     # FAQ knowledge base
│
├── web_scraping/
│   └── scrape_products.py   # Product data scraping and ingestion
│
├── requirements.txt
└── README.md
```


---

## 📸 Demo

<img width="1283" height="803" alt="ecommBot2" src="https://github.com/user-attachments/assets/4b2e4a66-de01-405a-af4e-61e2b0787483" />


### Suggested Screenshots

* Home Screen
* FAQ Query Example
* Product Search Example
* Semantic Router Workflow

---

## 📚 Learning Outcomes

This project demonstrates how modern AI applications combine:

🧠 LLMs for reasoning

📖 RAG for knowledge retrieval

🗄️ Vector Databases for semantic search

🔀 Semantic Routing for intent classification

🛍️ Text-to-SQL for structured data access

to build an intelligent e-commerce assistant capable of handling both customer support and product discovery workflows.

---

⭐ If you found this project interesting, feel free to star the repository!
