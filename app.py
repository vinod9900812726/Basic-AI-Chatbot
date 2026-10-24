
import streamlit as st
from rag import process_document, answer_question

st.set_page_config(
    page_title="GenAI Document Chatbot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 GenAI Document Chatbot")
st.write("Upload a PDF or TXT file and ask questions about its content.")

with st.sidebar:
    st.header("Document Upload")
    uploaded_file = st.file_uploader(
        "Choose a document",
        type=["pdf", "txt"]
    )

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_data" not in st.session_state:
    st.session_state.document_data = None

if uploaded_file is not None:
    if st.button("Process Document"):
        with st.spinner("Reading document and creating embeddings..."):
            try:
                st.session_state.document_data = process_document(
                    uploaded_file.getvalue(),
                    uploaded_file.name
                )
                st.session_state.messages = []
                st.success("Document processed successfully!")
            except Exception as error:
                st.error(f"Could not process document: {error}")

if st.session_state.document_data:
    st.success("Your document is ready for questions.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a question about your document...")

if question:
    if not st.session_state.document_data:
        st.warning("Upload and process a document first.")
    else:
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Searching document and generating answer..."):
                try:
                    result = answer_question(
                        question,
                        st.session_state.document_data
                    )

                    st.markdown(result["answer"])

                    if result["sources"]:
                        with st.expander("View supporting passages"):
                            for index, source in enumerate(
                                result["sources"], start=1
                            ):
                                st.markdown(f"**Passage {index}**")
                                st.write(source)

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": result["answer"]
                    })

                except Exception as error:
                    st.error(
                        "Could not generate an answer. "
                        "Check your API token, model availability, "
                        "and internet connection."
                    )
                    st.caption(str(error))

