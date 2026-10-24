
# GenAI Document Chatbot using RAG

## Overview
A Generative AI application that lets users upload PDF
and TXT documents and ask questions about their content.

## Features
- PDF and TXT file upload
- Text extraction and chunking
- Semantic search using embeddings
- Retrieval-Augmented Generation (RAG)
- AI-generated answers
- Supporting document passages
- Interactive Streamlit interface

## Technologies
- Python
- Streamlit
- Hugging Face Inference API
- Sentence Transformers
- NumPy
- pdfplumber

## Installation

1. Clone or download the repository.
2. Create a Python virtual environment.
3. Install the dependencies:

   pip install -r requirements.txt

4. Create a .env file with your Hugging Face token:

   HF_TOKEN=your_token_here

5. Run the application:

   streamlit run app.py

## Workflow
1. Upload a document.
2. Extract and split its text.
3. Convert chunks into embeddings.
4. Retrieve relevant passages for a question.
5. Send the passages and question to the language model.
6. Display the answer and supporting passages.

## Security
Never upload API tokens or private documents to GitHub.

## Limitations
Answers depend on the quality of extracted text,
retrieved passages, and language-model output.
Scanned PDFs may require OCR.

## License
Add a suitable license before distributing the project.
