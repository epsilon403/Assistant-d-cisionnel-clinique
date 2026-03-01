from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.session import get_db
from backend.models.query import Query
from backend.api.v1.schemas.query import QueryCreate, QueryResponse
from rag.pipeline import RAGPipeline
from backend.api.v1.endpoints.auth import get_current_user
from backend.models.user import User

router = APIRouter()


@router.post("/ask", response_model=QueryResponse)
def ask_medical_assistant(
    payload: QueryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Send a medical question through the RAG pipeline and store the result."""
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
    """Return all past queries ordered by most recent first."""
    return db.query(Query).order_by(Query.created_at.desc()).all()


@router.post("/document")
def ingest_medical_document(
    file_path: str = "data/raw/Guide-des-Protocoles.pdf",
    db: Session = Depends(get_db),
):
    """Ingest a medical PDF into the vector store."""
    pipeline = RAGPipeline()
    result = pipeline.ingest(file_path)
    return {"message": result}