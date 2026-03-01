# ============================================================
# chain.py - Chaîne RAG LangChain
# ============================================================
# Responsabilités:
#   - Construire la chaîne RAG complète avec LangChain:
#       * RetrievalQA chain ou custom LCEL chain
#       * Combiner: retriever → prompt → LLM → output parser
#   - Pipeline:
#       1. Recevoir la question utilisateur
#       2. (Optionnel) Query expansion
#       3. Retrieval: chercher les chunks pertinents
#       4. (Optionnel) Reranking des chunks
#       5. Construire le prompt avec le contexte
#       6. Générer la réponse via le LLM
#       7. Parser et formater la réponse
#       8. Retourner réponse + sources
#   - Supporter le streaming (optionnel)
# ============================================================
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from rag.generation.llm import get_llm
from rag.generation.prompts import RAG_USER_PROMPT
import mlflow

@mlflow.trace
def create_medical_rag_chain(retriever):
    
    """
    Construit la chaîne RAG complète[cite: 22, 58].
    1. Retrieval: Chercher les chunks (inclut expansion/reranking via le retriever passé)[cite: 20, 21].
    2. Prompt: Appliquer le template médical[cite: 23].
    3. LLM: Générer via Gemini[cite: 24].
    """
    llm = get_llm()
    

    question_answer_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=RAG_USER_PROMPT
    )
    

    full_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return full_chain