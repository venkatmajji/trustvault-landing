
import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
import os

st.set_page_config(page_title="TrustVault Investor Agent", page_icon="📊", layout="wide")

if not os.getenv("OPENAI_API_KEY"):
    st.warning("Investor Agent requires OpenAI API key configured in Streamlit secrets.")
    st.stop()

pdf_loader = PyPDFLoader("assets/TrustVault_Investor_One_Pager.pdf")
pdf_docs = pdf_loader.load()
pdf_texts = [d.page_content for d in pdf_docs]

additional_docs = [
    "TrustVault is the immutable audit layer for AI and LLMs. Capture, certify, and verify all interactions.",
    "Product: SDK + WORM storage + Merkle hashing + daily PDF seals + Evaluator Marketplace.",
    "TAM: $15B+, SAM: $2.5B, SOM: $100M wedge from regulated AI teams.",
    "Business model: Free → $199 Pro → $999 Compliance → $50k+ Enterprise.",
    "Roadmap: Immutable Vault → Real-time evaluator proxy → Evaluator Marketplace → Compliance automation.",
    "Why now: EU AI Act, SOC 2, HIPAA and enterprise AI buyers all need traceability today.",
    "Competitive edge: Only product with WORM+Merkle+root cert + marketplace + audit-first design."
]

all_docs = pdf_texts + additional_docs

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = FAISS.from_texts(all_docs, embeddings)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
qa = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever(), memory=memory)

st.markdown("<h1 style='color:#2563eb;'>TrustVault Investor Agent</h1>", unsafe_allow_html=True)

if "answer" not in st.session_state:
    st.session_state.answer = ""
if "selected_question" not in st.session_state:
    st.session_state.selected_question = ""

example_questions = [
    "👉 What problem does TrustVault solve?",
    "👉 How do you make money?",
    "👉 What is your roadmap for the next 12 months?",
    "👉 Who is your competition?",
    "👉 How big is the market opportunity?",
    "👉 Why should we invest?",
    "👉 Who is the founding team?",
    "👉 Is there founder to product fit?",
    "👉 What are the risks of investing?"
]

st.markdown("#### Example Questions")
cols = st.columns(3)
for idx, q in enumerate(example_questions):
    if cols[idx % 3].button(q, key=q):
        st.session_state.selected_question = q
        st.session_state.answer = ""

if st.session_state.selected_question:
    result = qa({'question': st.session_state.selected_question})
    answer = result['answer']
    if "I don't know" in answer or len(answer.strip()) < 10:
        answer = "This is not covered directly in our materials, but TrustVault is designed to be enterprise-grade and compliant."

    st.session_state.answer = answer
    st.markdown(f"<div style='background-color:#f9fafb;padding:20px;border-radius:12px;border:1px solid #e5e7eb;'>{st.session_state.answer.replace('\n', '<br>')}</div>", unsafe_allow_html=True)

st.components.v1.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSDzdc5x-xYZn3vCGhBiUxtK0Tmdkd9ufjXmja6mMaLcIyLkR9M61j_YszleNivSA/embed?start=false&loop=false&delayms=3000", height=550)
