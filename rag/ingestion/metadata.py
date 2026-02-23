# ============================================================
# metadata.py - Extraction et gestion des métadonnées
# ============================================================
# Responsabilités:
#   - Enrichir chaque chunk avec des métadonnées utiles:
#       * source: nom du fichier d'origine
#       * page: numéro de page (si PDF)
#       * chunk_index: index du chunk dans le document
#       * section: titre de la section (si détectable)
#       * category: catégorie du protocole médical
#       * document_type: type de document (protocole, guide, fiche)
#       * date: date du document
#   - Fournir des fonctions d'extraction automatique de métadonnées
# ============================================================
