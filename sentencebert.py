from sentence_transformers import SentenceTransformer
import openai
from pypdf import PdfReader
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv(dotenv_path=r"C:\Users\PC\Desktop\Python Stuff\SentenceBERT\apikey.env")

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please check your .env file.")

model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text+= page.extract_text()
    return text

repo1_text = extract_text_from_pdf(r'C:\Users\PC\Downloads\repos1.pdf')
repo2_text = extract_text_from_pdf(r'C:\Users\PC\Downloads\repos2.pdf')

repo1_embeddings = model.encode(repo1_text)
repo2_embeddings = model.encode(repo2_text)

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are an assistant."},
        {"role": "system", "content": "Analyze the differences between these documents."},
        {"role": "user", "content": f"Repo1: {repo1_text}\nRepo2: {repo2_text}"}
    ]
)

print (response['choices'][0]['message']['content'])