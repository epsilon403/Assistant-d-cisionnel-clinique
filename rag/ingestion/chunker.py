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
