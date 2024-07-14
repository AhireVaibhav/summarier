import streamlit as st
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    return summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']

# Streamlit app layout
st.title("Text Summarization App")
st.write("Enter text to summarize:")

text = st.text_area("Input Text", height=200)

if st.button("Summarize"):
    if text:
        summary = summarize_text(text)
        st.write("### Summary")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")
