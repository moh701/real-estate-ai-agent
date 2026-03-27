# real-estate-ai-agent
# 🏠 Local Real Estate AI Agent (Llama 3.2 + RAG)

[cite_start]This is a Python-based AI agent that uses **Llama 3.2** to answer questions about a specific property[cite: 1, 11]. [cite_start]It uses **RAG (Retrieval-Augmented Generation)** to read a PDF and provide accurate details[cite: 11, 12].

## 📍 Project Location
[cite_start]The data is based on a mixed-use building located in **Via Belzoni, Padua, Italy**[cite: 2, 3].

## 🛠️ How it Works
1. **PDF Loading:** It reads `property_spec.pdf` using `PyPDFLoader`.
2. **Vector Store:** It saves the data into a local Chroma database.
3. **Retrieval:** When you ask a question, it finds the relevant part of the PDF.
4. **Local LLM:** Llama 3.2 generates the final answer through **Ollama**.

## 📊 Property Highlights
* [cite_start]**Unit A1:** €450,000 for a 120sqm 3-bedroom apartment.
* [cite_start]**Unit B2:** €310,000 for an 80sqm professional studio[cite: 12].
* [cite_start]**Energy Class:** A4 High Efficiency.
* [cite_start]**Tech:** Geothermal heat pump and biometric security[cite: 7, 8].

## 🚀 How to Run
1. Install [Ollama](https://ollama.com).
2. Run `ollama pull llama3.2`.
3. Install Python libraries:
   `pip install langchain langchain-ollama langchain-community chromadb pypdf`
4. Run `python app.py`.
