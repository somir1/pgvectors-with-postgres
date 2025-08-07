import os
# import openai  # Commented out OpenAI
import psycopg2
from dotenv import load_dotenv
import numpy as np  # To simulate fake embeddings

# Load .env variables
load_dotenv()

# Sample content
text = "PostgreSQL + pgvector is great for AI-powered search!"

# ====== MOCK EMBEDDING ======
embedding = np.random.rand(1536).tolist()  # A Python list

# Insert into DB
try:
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
        (text, embedding)
    )

    conn.commit()
    print("✅ Mock embedding inserted!")

except Exception as e:
    print("❌ Error inserting embedding:", e)

finally:
    if conn:
        cur.close()
        conn.close()
