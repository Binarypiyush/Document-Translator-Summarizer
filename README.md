# Document-Translator-Summarizer

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=4B8BBE&width=500&lines=🌍+Multilingual+Translator+%26+Summarizer;Translate+%2F+Summarize+PDFs,+Voice,+Text!" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white" alt="Streamlit" />
  </a>
  <a href="https://huggingface.co">
    <img src="https://img.shields.io/badge/🤗%20Transformers-Hugging%20Face-yellow" alt="Transformers" />
  </a>
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python" />
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" />
  </a>
</p>

---

## 🌐 Multi-Lingual Translator & Summarizer

This is a Streamlit web app that lets users **translate and summarize** text from **PDF files**, **voice input**, or **manual input** using state-of-the-art NLP models from 🤗 Hugging Face. It supports multiple languages and provides both original and translated summaries.

---

### 🚀 Live Demo


```markdown
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://document-translator-summarizer-j3bbwwmjo2f2kjiylrzrqg.streamlit.app/)

✨ Features
📄 PDF Extraction – Upload PDF and extract readable text

🎤 Voice Input – Speak and convert to text using your mic

🌍 Language Translation – Translate between English, Hindi, French, and Spanish using MarianMT models

🧠 Summarization – Summarize original and translated texts with T5

🖥️ Streamlit UI – Interactive layout with real-time feedback

🌍 Supported Languages
English (en)

Hindi (hi)

French (fr)

Spanish (es)

🛠 Tech Stack
Frontend: Streamlit

NLP Models: Hugging Face Transformers

Voice Recognition: SpeechRecognition

PDF Text Extraction: PyPDF2

Backend: Python + Torch

📦 Installation
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/multilingual-translator-summarizer.git
cd multilingual-translator-summarizer
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Streamlit app
bash
Copy
Edit
streamlit run app.py

📁 Project Structure
bash
Copy
Edit
multilingual-translator-summarizer/
│
├── app.py                  # Main Streamlit app script
├── requirements.txt        # Required packages
├── README.md               # Project documentation
├── LICENSE                 # MIT License
└── .gitignore              # Files to ignore in Git
💡 Future Enhancements
OCR support for image-based PDFs

Auto language detection

Export summaries to PDF/TXT

Dark/light theme toggle

More language support

📄 License
This project is licensed under the MIT License.

🙌 Acknowledgements
🤗 Hugging Face

Streamlit

Google Speech-to-Text
