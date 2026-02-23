# ============================================================
# query_expansion.py - Techniques d'expansion de requêtes
# ============================================================
# Responsabilités:
#   - Implémenter des techniques pour améliorer la recherche:
#       * Multi-Query: Générer plusieurs variantes de la requête
#         via un LLM pour couvrir différentes formulations
#       * HyDE (Hypothetical Document Embeddings):
#         Générer un document hypothétique pour la recherche
#       * Step-back Prompting: Reformuler la requête
#         à un niveau d'abstraction plus élevé
#   - Chaque technique retourne une liste de queries alternatives
# ============================================================
