import os
import PyPDF2
from transformers import pipeline
import tensorflow as tf

# Set environment variable to disable oneDNN custom operations
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Limit TensorFlow GPU memory growth
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

def chunk_text(text, chunk_size=250):  # Reduced chunk size
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", framework="pt")

def summarize_text_chunks(text_chunks, max_length=150):
    summaries = []
    for chunk in text_chunks:
        summary = summarizer(chunk, max_length=max_length, min_length=30, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    return " ".join(summaries)

def summarize_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    text_chunks = chunk_text(text)
    summary = summarize_text_chunks(text_chunks)
    return summary

# Example usage
pdf_path = "Operations Management.pdf"  # Replace with your actual PDF path
summary = summarize_pdf(pdf_path)
print(summary)
