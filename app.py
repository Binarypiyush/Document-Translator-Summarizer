import streamlit as st
from transformers import MarianMTModel, MarianTokenizer, T5Tokenizer, T5ForConditionalGeneration
import torch
import speech_recognition as sr
import PyPDF2

# Set up the page
st.set_page_config(page_title="🌍 Multi-Lingual Translator & Summarizer", layout="wide")
st.title("🌍 Document Translator & Summarizer")

# Cache translation model
@st.cache_resource
def load_translation_model(model_name):
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    return model, tokenizer

# Cache summarization model
@st.cache_resource
def load_summarization_model():
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    return tokenizer, model

# Translation function
def translate_text(text, src_lang, tgt_lang):
    if src_lang == tgt_lang:
        return text
    try:
        model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
        model, tokenizer = load_translation_model(model_name)
        tokenized = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated = model.generate(**tokenized)
        return tokenizer.decode(translated[0], skip_special_tokens=True)
    except Exception as e:
        return f"Translation Error: {e}"

# Summarization function
def summarize_text(text):
    try:
        sum_tokenizer, sum_model = load_summarization_model()
        input_text = "summarize: " + text
        inputs = sum_tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = sum_model.generate(**inputs)
        return sum_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    except Exception as e:
        return f"Summarization Error: {e}"

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''.join([page.extract_text() or '' for page in reader.pages])
        return text.strip() or "No readable text found."
    except Exception as e:
        return f"PDF Error: {e}"

# Voice input
def voice_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening... please speak now.")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Could not understand audio."
        except sr.RequestError:
            return "Speech recognition service failed."

# Language map
languages = {"English": "en", "Hindi": "hi", "French": "fr", "Spanish": "es"}

# Layout UI
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📄 Upload or Enter Text")
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if pdf_file:
        extracted = extract_text_from_pdf(pdf_file)
        st.success("✅ PDF text extracted!")
        st.text_area("Extracted Text", value=extracted, key="pdf_text", height=150)
    else:
        default_input = st.text_area("Enter your text manually", key="manual_input", height=150)

    if st.button("🎤 Speak Now"):
        spoken_text = voice_to_text()
        st.session_state["manual_input"] = spoken_text
        st.success("🗣️ Voice input recognized!")

with col2:
    st.subheader("🌐 Translate & Summarize")
    source_lang = st.selectbox("Source Language", list(languages.keys()), index=0)
    target_lang = st.selectbox("Target Language", list(languages.keys()), index=1)

    input_text = st.session_state.get("pdf_text") or st.session_state.get("manual_input") or ""

    if st.button("🚀 Translate and Summarize"):
        if not input_text.strip():
            st.error("❌ Please provide input text first.")
        else:
            with st.spinner("Translating..."):
                translated = translate_text(input_text, languages[source_lang], languages[target_lang])
                st.success("✅ Translation Complete")

            with st.expander("📘 Translated Text", expanded=True):
                st.write(translated)

            with st.spinner("Summarizing Original..."):
                orig_summary = summarize_text(input_text)

            with st.spinner("Summarizing Translated..."):
                trans_summary = summarize_text(translated)

            with st.expander("🧠 Summary of Original Text"):
                st.write(orig_summary)

            with st.expander("🧠 Summary of Translated Text"):
                st.write(trans_summary)
