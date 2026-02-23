# ============================================================
# chat.py - Page principale de chat avec l'assistant RAG
# ============================================================
# Responsabilités:
#   - Interface de chat (style conversationnel)
#   - Zone de saisie pour la question médicale
#   - Affichage des réponses avec:
#       * Réponse générée par le RAG
#       * Sources utilisées (chunks, pages, documents)
#       * Temps de réponse
#   - Historique de la conversation dans la session
#   - Appeler l'API backend POST /query/
#   - Indicateur de chargement pendant le traitement
# ============================================================
