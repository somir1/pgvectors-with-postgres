import os
# import openai  # Commented out OpenAI
import psycopg2
from dotenv import load_dotenv
import numpy as np  # To simulate fake embeddings

# Load .env variables
load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")

# Sample content
text = "PostgreSQL + pgvector is great for AI-powered search!"

# ====== COMMENTED OUT: Get actual embedding from OpenAI ======
# client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# response = client.embeddings.create(
#     input=[text],
#     model="text-embedding-3-small"
# )
# embedding = response['data'][0]['embedding']

# ====== MOCK EMBEDDING ======
# Simulate a 1536-dimensional vector with random floats (same size as text-embedding-3-small)
embedding = np.random.rand(1536).tolist()

# Convert to pgvector-compatible string
embedding_str = str(embedding).replace('[', '{').replace(']', '}')

# Insert into DB
conn = psycopg2.connect(
    dbname="vector_db",
    user="leon",
    password="",        # Add if needed
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute(
    "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
    (text, embedding_str)
)

conn.commit()
cur.close()
conn.close()

print("✅ Mock embedding inserted!")
