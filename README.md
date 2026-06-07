# LogicTrace AI 💻

An AI-powered educational debugging assistant designed to help beginner programmers identify, visualize, and understand hidden logical errors in their code .
Traditional compilers and IDEs excel at catching syntax issues but leave students completely stranded when code runs but produces incorrect results . LogicTrace AI bridges this gap by using a Large Language Model to serve as a virtual programming tutor that prioritizes conceptual learning over lazy copy-pasting .

## 🔗 Live Demo
👉 [LogicTrace AI Web App](https://logictrace-ai-t6nuwkofi69hadgwmadn8m.streamlit.app/)


## 💡 Features

* **Intent-Driven Debugging:** Compares faulty code directly against the user's explicit *Expected Behavior* statement to target the true algorithmic goal .
* **Socratic Feedback:** Intentionally constrains output to educational guidance, ensuring students learn the core computer science concepts instead of just copy-pasting generic fixes .
* **Variable Trace Simulation:** Simulates execution states over code blocks to explicitly illustrate how data values change incorrectly across cycles .
* **Structured Markdown Reporting:** Breaks down the analysis into strict, digestible pillars :
  1. 🔍 1. Where the Logic Broke (Problem & Error Identification) 
  2. 📊 2. What the Variables Are Doing (Variable Trace Simulation) 
  3. 🛠️ 3. How to Fix It (Suggested Guidance & Core Learning Explanations) 


## 🛠️ Tech Stack

* **Presentation Layer:** Streamlit (Python-native rapid UI generation framework) 
* **AI Orchestration Framework:** Google GenAI SDK (`google-generativeai` module) 
* **Core Model Engine:** `gemini-2.5-flash` (Optimized for speed, low latency, and structured formatting compliance) 
* **Deployment Target:** Streamlit Community Cloud 

---

## 🧠 Architecture

Below is the design layout and systemic data flow of the application tracking input ingestion through to response formatting :

![Architecture Diagram](neww.png)

## ⚙️ Setup & Local Installation 

### Prerequisites
1. Make sure you have Python 3.9+ installed on your computer.
2. **Gemini API Key:** You will need a free API key from Google AI Studio to run the backend engine .

### 1. Install Dependencies
Install the required software packages using your terminal:
```bash
pip install -r requirements.txt

### 2. Configure Your Local Backend Secrets
To run the application locally without exposing credentials on the frontend user interface, create a hidden configuration folder named `.streamlit` in your project root. Inside it, create a file named `secrets.toml` and add your secret token:
```toml
GEMINI_API_KEY = "your_actual_gemini_api_key_here"
### 3. Boot Up the Web Server
Launch your local instance of the application using Streamlit:
```bash
streamlit run app.py
