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

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic_settings import BaseSettings

class LLMConfig(BaseSettings):

    model_name: str = "gemini-2.0-flash"
    temperature: float = 0.0 # Strict accuracy for clinical decisions [cite: 5, 55]
    max_tokens: int = 1000
    top_p: float = 0.95
    top_k: int = 40

    class Config:
        env_file = ".env"
        extra = "ignore"

def get_llm():
    """Initialise le LLM avec les hyperparamètres du projet."""
    config = LLMConfig()
    return ChatGoogleGenerativeAI(
        model=config.model_name,
        temperature=config.temperature,
        max_output_tokens=config.max_tokens,
        top_p=config.top_p,
        top_k=config.top_k,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )