# ============================================================
# query.py - Endpoints de requêtes RAG
# ============================================================
# Responsabilités:
#   - POST /query/     : Soumettre une question au pipeline RAG
#                        → Reçoit la query, exécute le pipeline RAG,
#                          retourne la réponse générée avec les sources
#                        → Sauvegarde la query et la réponse en DB
#   - GET  /query/     : Lister l'historique des requêtes de l'utilisateur
#   - GET  /query/{id} : Récupérer une requête spécifique avec sa réponse
# ============================================================
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.session import get_db
from backend.models.query import Query
from backend.api.v1.schemas.query import QueryCreate, QueryResponse

router = APIRouter()


@router.post("/ask", response_model=QueryResponse)
def ask_medical_assistant(payload: QueryCreate, db: Session = Depends(get_db)):
    try:
        from rag.generation.chain import create_medical_rag_chain
        from rag.retrieval.retriever import get_hybrid_retriever

        retriever = get_hybrid_retriever()
        chain = create_medical_rag_chain(retriever)

        result = chain.invoke({"input": payload.query})
        answer = result["answer"]
    except Exception as e:
        answer = f"RAG pipeline not available: {e}"

    new_entry = Query(query=payload.query, reponse=answer)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry


@router.get("/history", response_model=list[QueryResponse])
def get_query_history(db: Session = Depends(get_db)):
    queries = db.query(Query).order_by(Query.created_at.desc()).all()
    return queries
    return queries