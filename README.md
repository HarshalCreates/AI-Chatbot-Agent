# 🤖 AI Chatbot Agent

A full-stack AI chatbot system using **LangGraph**, powered by **LLMs from Groq/OpenAI** and enhanced with **Tavily search**. This project features a real-time Streamlit frontend and a FastAPI backend for smooth, scalable, agent-driven interactions.

![image](https://github.com/user-attachments/assets/1ece781f-4c22-4fdb-bdbc-748289950370)


---

## 🚀 Features

- ✨ Customizable AI agents (via system prompt)
- 🔄 Choose between **Groq** or **OpenAI** models
- 🔍 Optional real-time web search (Tavily)
- 💬 Chat interface powered by **Streamlit**
- ⚙️ Backend API built with **FastAPI**
- 🔐 Secret management via `.env` file
- 🧠 Uses **LangGraph’s ReAct agent** pattern

---

## 🧱 Tech Stack

| Layer      | Tech                         |
|------------|------------------------------|
| Frontend   | Streamlit                    |
| Backend    | FastAPI                      |
| LLMs       | OpenAI, Groq (LLaMA 3)       |
| Search     | Tavily                       |
| Agent Logic| LangGraph + LangChain        |
| Secrets    | Python-dotenv + `.env`       |

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/HarshalCreates/AI-Chatbot-Agent.git
cd AI-Chatbot-Agent
```
2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Set up your .env file

Create a .env file with your API keys:

```bash
OPENAI_API_KEY=your-openai-key
GROQ_API_KEY=your-groq-key
TAVILY_API_KEY=your-tavily-key
```
🔒 Important: Never share this .env file publicly!

## 🖥️ Running the App
🌐 Start the FastAPI backend:
```bash
uvicorn main:app --reload
```
📲 Launch the Streamlit frontend:
```bash
streamlit run app.py
```
Then go to http://localhost:8501 in your browser.


## 📌 Notes
🔐 Do not push .env files or secret keys to GitHub.

💡 Add a screenshot.png or preview GIF for a visual readme.

🚀 You can deploy the backend with Render, Vercel (with API Gateway), or Railway.

🧠 You can extend this with memory, vector stores, or LangChain tools.

## 📃 License
MIT License © 2025 HarshalCreates

## 🙌 Acknowledgments
LangGraph

LangChain

Streamlit

FastAPI

Tavily

Groq

