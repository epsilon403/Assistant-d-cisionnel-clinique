# ============================================================
# prompts.py - Templates de prompts centralisés
# ============================================================
# Responsabilités:
#   - Définir les templates de prompts LangChain:
#
#   - RAG_SYSTEM_PROMPT: Prompt système pour l'assistant médical
#       * Rôle: assistant médical spécialisé
#       * Instructions: répondre uniquement à partir du contexte
#       * Format: structuré, précis, avec références aux sources
#       * Garde-fous: ne pas inventer, indiquer si info insuffisante
#
#   - RAG_USER_PROMPT: Template pour la question + contexte
#       * Variables: {context}, {question}
#       * Structure: contexte récupéré + question de l'utilisateur
#
#   - QUERY_EXPANSION_PROMPT: Prompt pour l'expansion de requêtes
#       * Générer N variantes de la question originale
#
#   - CONDENSE_QUESTION_PROMPT: (optionnel) Pour le mode conversationnel
#       * Condenser l'historique + nouvelle question
# ============================================================
