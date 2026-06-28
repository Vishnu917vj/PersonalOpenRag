from uuid import uuid4

import pandas as pd
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# -----------------------------
# Configuration
# -----------------------------

PINECONE_API_KEY="api key here"
PINECONE_INDEX="personal-rag"
NAMESPACE = "qa-dataset"

EXCEL_FILE = r"C:\\Users\\iamvi\\Downloads\\cleaned_dataset.xlsx"

# -----------------------------
# Load embedding model
# -----------------------------

print("Loading BAAI model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Model loaded.")

# -----------------------------
# Pinecone
# -----------------------------

pc = Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index(PINECONE_INDEX)

# -----------------------------
# Read Excel
# -----------------------------

df = pd.read_excel(EXCEL_FILE)

vectors = []

print(f"Processing {len(df)} rows...")

for _, row in tqdm(df.iterrows(), total=len(df)):

    question = "" if pd.isna(row["Clean Question"]) else str(row["Clean Question"]).strip()
    answer = "" if pd.isna(row["Clean Answer"]) else str(row["Clean Answer"]).strip()

    text = f"Question: {question}\nAnswer: {answer}"

    embedding = model.encode(
        text,
        normalize_embeddings=True
    ).tolist()

    vectors.append(
        {
            "id": str(uuid4()),
            "values": embedding,
            "metadata": {
                "text": text
            }
        }
    )

# -----------------------------
# Upload
# -----------------------------

print("Uploading to Pinecone...")

index.upsert(
    vectors=vectors,
    namespace=NAMESPACE
)

print("Done!")
print(f"Indexed {len(vectors)} documents.")