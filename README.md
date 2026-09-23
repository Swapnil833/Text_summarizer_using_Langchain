# 📝 Text Summarizer using LangChain

A **Generative AI-based Text Summarizer** built with **LangChain** that automatically extracts content from **YouTube videos and web pages**, validates the provided URL, and generates a concise summary using an LLM.

## ✨ Features

* 🔗 **URL Validation** — Checks whether the provided link is valid before processing.
* ▶️ **YouTube Summarization** — Uses `YoutubeLoader` to extract content from YouTube videos.
* 🌐 **Web Page Summarization** — Uses `WebBaseLoader` to extract content from regular websites.
* 🤖 **LLM-Powered Summarization** — Generates a concise summary from the extracted content.
* 🦜🔗 **LangChain** — Handles document loading, processing, and LLM integration.
* 🖥️ **Streamlit Interface** — Provides a simple interface for entering URLs and viewing summaries.

## 🛠️ Tech Stack

| Technology        | Purpose                                           |
| ----------------- | ------------------------------------------------- |
| **Python**        | Core programming language                         |
| **LangChain**     | LLM application framework and document processing |
| **YoutubeLoader** | Extracts transcript/content from YouTube videos   |
| **WebBaseLoader** | Extracts content from web pages                   |
| **LLM**           | Generates the final summary                       |
| **Streamlit**     | Interactive web interface                         |

## 🔄 How It Works

```text
User Enters URL
       ↓
   Validate URL
       ↓
  Is URL Valid?
    ↙       ↘
  No         Yes
  ↓           ↓
Error     Identify Link Type
              ↓
       ┌──────┴──────┐
       ↓             ↓
   YouTube        Website
       ↓             ↓
YoutubeLoader   WebBaseLoader
       ↓             ↓
       └──────┬──────┘
              ↓
       Extract Content
              ↓
        Process Content
              ↓
             LLM
              ↓
       Generate Summary
              ↓
       Display Summary
```

## 🚀 Getting Started

### 1) Clone the Repository

```bash
git clone <your-repository-url>
cd Text-Summarizer
```

### 2) Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 3) Install Dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure API Key

Create a `.env` file and add the required LLM API key:

```env
OPENAI_API_KEY=your_api_key
```

### 5) Run the Application

```bash
streamlit run app.py
```

## 📖 How to Use

1. Launch the Streamlit application.
2. Enter a **YouTube or website URL**.
3. The application first **validates the URL**.
4. If the URL is invalid, an error is displayed.
5. If the URL is valid, the application identifies the link type.
6. For a **YouTube link**, `YoutubeLoader` is used to retrieve the video content/transcript.
7. For a **website link**, `WebBaseLoader` is used to extract the webpage content.
8. The extracted content is passed to the LLM.
9. The application generates and displays the **final summary**.

## 🧠 LangChain Workflow

```text
URL
 ↓
URL Validation
 ↓
┌──────────────────┐
│  Link Detection  │
└────────┬─────────┘
         ↓
 ┌───────┴────────┐
 ↓                ↓
YoutubeLoader   WebBaseLoader
 ↓                ↓
 └───────┬────────┘
         ↓
  Extracted Content
         ↓
    LLM Processing
         ↓
      Summary
```

## 🎯 Use Cases

* Summarizing YouTube videos
* Quickly understanding web articles
* Extracting key information from websites
* Creating concise notes from online content
* Research and learning assistance

