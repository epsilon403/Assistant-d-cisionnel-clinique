# ============================================================
# chunker.py - Stratégies de chunking des documents
# ============================================================
# Responsabilités:
#   - Implémenter plusieurs stratégies de chunking:
#       * RecursiveCharacterTextSplitter (recommandé)
#       * SemanticChunker (basé sur les embeddings)
#       * MarkdownHeaderTextSplitter (si applicable)
#   - Paramètres configurables:
#       * chunk_size: taille maximale d'un chunk (ex: 512, 1000)
#       * chunk_overlap: chevauchement entre chunks (ex: 100, 200)
#       * separators: séparateurs personnalisés
#   - Préserver le contexte maximal dans chaque chunk
#   - Attacher les métadonnées à chaque chunk (voir metadata.py)
# ============================================================

from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_medical_documents(documents, chunk_size=1000, chunk_overlap=200):
    """
    Splits documents into smaller chunks while preserving medical context.
    - chunk_size: Max characters per chunk.
    - chunk_overlap: Shared text between chunks to prevent losing context at the edges.
    """
    # We use these separators to prioritize splitting at logical breaks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks from {len(documents)} pages.")
    return chunks