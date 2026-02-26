# ============================================================
# app.py - Point d'entrée Streamlit
# ============================================================
import streamlit as st
import requests

BACKEND_URL = "http://backend:8000"

st.set_page_config(
    page_title="CliniQ - Assistant Décisionnel Clinique",
    page_icon="🏥",
    layout="wide",
)

st.title("🏥 CliniQ - Assistant Décisionnel Clinique")
st.markdown("Posez vos questions médicales et obtenez des réponses basées sur les protocoles cliniques.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Posez votre question médicale..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Recherche en cours..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/api/v1/query/ask",
                    json={"query": prompt},
                    timeout=60,
                )
                if response.status_code == 200:
                    answer = response.json().get("reponse", "Pas de réponse.")
                else:
                    answer = f"Erreur du serveur: {response.status_code}"
            except requests.exceptions.ConnectionError:
                answer = "Impossible de se connecter au serveur backend."
            except Exception as e:
                answer = f"Erreur: {e}"

        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

# Sidebar
with st.sidebar:
    st.header("À propos")
    st.markdown(
        "CliniQ est un assistant décisionnel clinique basé sur une architecture RAG "
        "(Retrieval-Augmented Generation) pour fournir un accès instantané aux protocoles médicaux."
    )
    if st.button("🗑️ Effacer la conversation"):
        st.session_state.messages = []
        st.rerun()
