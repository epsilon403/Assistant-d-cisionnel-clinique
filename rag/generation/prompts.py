
from langchain_core.prompts import ChatPromptTemplate

# RAG_SYSTEM_PROMPT: Role and safety guardrails [cite: 2, 4, 5, 25]
RAG_SYSTEM_PROMPT = (
    "Vous êtes un assistant intelligent basé sur une architecture RAG optimisée, "
    "fournisant aux professionnels de santé un accès instantané et contextualisé "
    "aux protocoles médicaux[cite: 2]. "
    "Utilisez exclusivement les extraits de protocoles fournis pour répondre[cite: 5]. "
    "Si la réponse n'est pas contenue dans le contexte, indiquez clairement que "
    "l'information est insuffisante. Ne pas inventer d'informations[cite: 25]. "
    "Répondez de manière structurée et précise en citant vos sources."
)

# RAG_USER_PROMPT: Template for retrieval integration
RAG_USER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", RAG_SYSTEM_PROMPT),
    ("human", "Contexte: {context}\n\nQuestion: {input}")
])

# QUERY_EXPANSION_PROMPT: For generating variations [cite: 21]
QUERY_EXPANSION_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "Vous êtes un expert en recherche d'information médicale."),
    ("human", "Générez 3 variantes différentes de la question suivante pour "
              "optimiser la recherche dans une base de données médicale: {question}")
])