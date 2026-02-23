# ============================================================
# llm.py - Configuration du modèle LLM
# ============================================================
# Responsabilités:
#   - Initialiser le LLM (via LangChain):
#       * Ollama (modèles locaux: llama3, mistral, etc.)
#       * OpenAI (GPT-4, GPT-3.5-turbo)
#       * HuggingFace Hub
#   - Hyperparamètres configurables:
#       * model_name: nom du modèle
#       * temperature: créativité (0.0 - 1.0)
#       * max_tokens: longueur max de la réponse
#       * top_p: nucleus sampling
#       * top_k: top-k sampling
#   - Fournir une interface unifiée pour la génération
# ============================================================
