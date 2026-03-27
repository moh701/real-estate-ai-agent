import os
import time
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --- 1. CONFIGURATION ---
pdf_path = "property_spec.pdf"
llm = OllamaLLM(model="llama3.2", temperature=0)
embeddings = OllamaEmbeddings(model="llama3.2")

print("🚀 Starting Real Estate AI Agent...")

# --- 2. DATA INGESTION ---
if not os.path.exists(pdf_path):
    print(f"❌ Error: {pdf_path} not found!")
    exit()

loader = PyPDFLoader(pdf_path)
docs = loader.load()
splits = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100).split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
retriever = vectorstore.as_retriever()

# --- 3. THE RAG CHAIN ---
template = """Answer the question based ONLY on the context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# --- 4. EXECUTION ---
print("✅ Database Indexed. Llama-3.2 is ready.")
query = "What is the price and features of Unit A1?"
print(f"\n❓ Question: {query}")
response = rag_chain.invoke(query)
print(f"\n🤖 Llama's Answer: {response}")