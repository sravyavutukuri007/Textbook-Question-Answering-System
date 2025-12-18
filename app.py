import streamlit as st
from rag_pipeline import chatbot
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="RAG Assistant", layout="centered")

st.title("📘 Textbook Question Answering System")
st.write("Ask questions based on the uploaded textbook.")

# Input box
question = st.text_input("Enter your question")

if st.button("Get Answer") and question:
    with st.spinner("Thinking..."):
        result = chatbot.invoke(
            {
                "messages": [
                    HumanMessage(content=question)
                ]
            }
        )

        answer = result["messages"][-1].content

    st.subheader("Answer")
    st.write(answer)
