import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_answer(question, relevant_chunks):
    context="\n\n".join(relevant_chunks)
    prompt=f"""Answer using only the context. Context:\n{context}\nQuestion:{question}"""
    response=client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return response.text
