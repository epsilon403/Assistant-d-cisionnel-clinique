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
