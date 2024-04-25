import streamlit as st
import PyPDF2
import google.generativeai as genai

def retrieve_text_from_pdf(pdf):
    with open(pdf, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def main():
    # Inject custom CSS for enhanced theming
    st.markdown(
        """
        <style>
        html, body, [class*="css"] {
            font-family: "Arial", sans-serif;
        }
        .reportview-container {
            background-color: #2C3E50;
            color: #ECF0F1;
        }
        .stTextInput > label, .stButton > button, .stMarkdown > div {
            color: #ECF0F1;
        }
        .stTextInput > div > div > input {
            color: #2C3E50;
            background-color: #ECF0F1;
        }
        .stButton > button {
            background-color: #3498DB;
            border: none;
            color: white;
            padding: 8px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            transition-duration: 0.4s;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: white;
            color: #3498DB;
        }
        div.stMarkdownContainer {
            background-color: #34495E;
            border-radius: 10px;
            padding: 10px;
        }
        .question-answer {
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # PDF Path
    pdf = r"D:\A Internship JAN 2024\BACKEND_SESSIONS\GENAI_APPS\RAG\paper\2404.07143.pdf"
    model = "gemini-1.5-pro-latest"
    with open(r"D:\A Internship JAN 2024\BACKEND_SESSIONS\GENAI_APPS\RAG\gemini_key.txt", "r") as file:
        key = file.read()
    genai.configure(api_key=key)

    st.markdown("""
        <h1 style='color: #3498DB;'>The "Leave No Context Behind" paper's RAG System</h1>
        """, unsafe_allow_html=True)

    question = st.text_input("Enter your question:", "")

    if st.button("Generate"):
        if question:
            text = retrieve_text_from_pdf(pdf)
            context = text + "\n\n" + question
            ai = genai.GenerativeModel(model_name=model)
            response = ai.generate_content(context)
            st.subheader("Question:")
            st.markdown(f"<div class='question-answer'>{question}</div>", unsafe_allow_html=True)
            st.subheader("Answer:")
            st.markdown(f"<div class='question-answer'>{response.text}</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter your question.")

    # Sidebar configuration
    st.sidebar.title("Information")
    st.sidebar.info(
        "This application is built using Streamlit, PyPDF2, and Google's Generative AI APIs. "
        
    )
    



if __name__ == "__main__":
    main()
