# ============================================================
# loader.py - Chargement des documents
# ============================================================
# Responsabilités:
#   - Charger les fichiers PDF depuis le dossier data/raw/
#   - Supporter plusieurs formats (PDF, DOCX, TXT)
#   - Utiliser LangChain Document Loaders:
#       * PyPDFLoader pour les PDF
#       * DirectoryLoader pour le chargement en batch
#   - Extraire le texte brut de chaque document
#   - Retourner une liste de LangChain Documents
# ============================================================
from langchain_community.document_loaders import PyPDFLoader
import os

def load_medical_document(file_path: str):
    """
    Loads a PDF document and returns a list of LangChain Document objects.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No file found at {file_path}")
    
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    
    print(f"Successfully loaded {len(documents)} pages from {file_path}")
    return documents