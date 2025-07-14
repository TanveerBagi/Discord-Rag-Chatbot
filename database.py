import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from docx import Document
import os

client = chromadb.PersistentClient(path='C:/Users/tanve/PycharmProjects/Discord Rag Chatbot/database_storage')
collection = client.get_or_create_collection(
                    name = 'chatbot_data',
                    embedding_function=SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2"))

docx_folder = "C:/Users/tanve/Documents/documents for chromadb"
documents= []
ids = []
metadatas = []

def chunk_text(text, chunk_size=300):
    words = text.split()
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]


def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = []

    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text)

    return '\n'.join(text)


existing_ids = set()
try:
    existing_docs = collection.get(include=['metadatas'])
    existing_ids = set(existing_docs["ids"])
except:
    pass

for filename in os.listdir(docx_folder):
    if filename.endswith('.docx'):
        file_id = filename.replace('.docx', '')

        file_path = os.path.join(docx_folder,filename)

        text_content = extract_text_from_docx(file_path)
        if text_content.strip():
            chunks = chunk_text(text_content)
            for i, chunk in enumerate(chunks):
                documents.append(chunk)
                ids.append(f"{filename.replace('.docx', '')}_chunk_{i}")
                metadatas.append({
                    'filename': filename,
                    'file_path': file_path,
                    'file_type': 'docx',
                    'chunk_index': i
                })

if documents:
    collection.add(
        ids = ids,
        documents=documents,
        metadatas = metadatas
    )


print("everything happened successfully")


def retrieved_text(query):
    results = collection.query(
        query_texts=[query],
        n_results=1
    )

    for i, doc in enumerate(results['documents'][0]):
        metadata = results['metadatas'][0][i]
        combined_context = "\n\n".join([
            f"Document: {metadata['filename']}",
            f"Content: {doc}"
        ])
        return combined_context

