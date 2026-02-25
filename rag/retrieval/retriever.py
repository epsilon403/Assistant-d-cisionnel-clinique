# ============================================================
# retriever.py - Configuration du retriever
# ============================================================
# Responsabilités:
#   - Configurer le retriever LangChain à partir du vector store
#   - Paramètres:
#       * search_type: "similarity", "mmr" (Maximal Marginal Relevance)
#       * k: nombre de chunks à retourner (ex: 4, 6, 10)
#       * score_threshold: seuil minimum de similarité
#       * filter: filtres sur les métadonnées
#   - Supporter plusieurs types de retrievers:
#       * VectorStoreRetriever (base)
#       * ContextualCompressionRetriever (avec reranker)
#       * EnsembleRetriever (combinaison de retrievers)
#       * MultiQueryRetriever (query expansion automatique)
# ============================================================
from langchain.retrievers import EnsembleRetriever, ContextualCompressionRetriever
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers.document_compressors import FlashrankRerank
from langchain_openai import ChatOpenAI # or your choice of LLM
from rag.embeddings.vector_store import load_vector_store

def get_hybrid_retriever(documents):
   
    # 1. Setup Vector Retriever (Semantic)
    vector_db = load_vector_store()
    vector_retriever = vector_db.as_retriever(
        search_type="mmr", # Max Marginal Relevance to reduce redundancy [cite: 53]
        search_kwargs={'k': 6, 'fetch_k': 20}
    )


    bm25_retriever = BM25Retriever.from_documents(documents)
    bm25_retriever.k = 6


    ensemble_retriever = EnsembleRetriever(
        retrievers=[vector_retriever , bm25_retriever],
        weights=[0.5, 0.5] 
    )


    llm = ChatOpenAI(temperature=0) 
    mq_retriever = MultiQueryRetriever.from_llm(
        retriever=ensemble_retriever, 
        llm=llm
    )


   

    return mq_retriever