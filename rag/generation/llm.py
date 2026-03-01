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
from langchain_ollama import ChatOllama
from pydantic_settings import BaseSettings

class LLMConfig(BaseSettings):
    model_name: str = "llama3.1"
    temperature: float = 0.0 
    max_tokens: int = 1000
    top_p: float = 0.95
    top_k: int = 40
    ollama_base_url: str = "http://host.docker.internal:11434"

    class Config:
        env_file = ".env"
        extra = "ignore"

import mlflow

@mlflow.trace
def get_llm():
    """Initialise le LLM local avec les hyperparamètres du projet."""
    config = LLMConfig()
    
    return ChatOllama(
        base_url=config.ollama_base_url,
        model=config.model_name,
        temperature=config.temperature,
        num_predict=config.max_tokens,
        top_k=config.top_k,
    )