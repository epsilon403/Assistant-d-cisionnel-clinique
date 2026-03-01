
from langchain.retrievers import EnsembleRetriever, ContextualCompressionRetriever
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_community.document_compressors import FlashrankRerank
from langchain_google_genai import ChatGoogleGenerativeAI
from rag.embeddings.store import load_vector_store
import os
import mlflow
from rag.generation.llm import get_llm

@mlflow.trace
def get_hybrid_retriever(documents=None):
   

    vector_db = load_vector_store()
    vector_retriever = vector_db.as_retriever(
        search_type="mmr", 
        search_kwargs={'k': 6, 'fetch_k': 20}
    )

    if documents is None:
        stored = vector_db.get()
        if not stored['documents']:
            raise ValueError("Vector store is empty. Please ingest documents first via POST /api/v1/query/document")

        from langchain_core.documents import Document
        documents = [
            Document(page_content=text, metadata=(meta or {}))
            for text, meta in zip(stored['documents'], stored['metadatas'])
        ]

    bm25_retriever = BM25Retriever.from_documents(documents)
    bm25_retriever.k = 6


    ensemble_retriever = EnsembleRetriever(
        retrievers=[vector_retriever , bm25_retriever],
        weights=[0.5, 0.5] 
    )


    llm = get_llm()
    mq_retriever = MultiQueryRetriever.from_llm(
        retriever=ensemble_retriever, 
        llm=llm
    )


   

    return mq_retriever