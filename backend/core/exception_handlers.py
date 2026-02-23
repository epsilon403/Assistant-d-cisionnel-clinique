# ============================================================
# exception_handlers.py - Gestionnaires d'exceptions FastAPI
# ============================================================
# Responsabilités:
#   - Enregistrer les handlers pour chaque type d'exception
#   - Formater les réponses d'erreur de manière cohérente
#     (structure JSON: { "detail": ..., "status_code": ..., "error_type": ... })
#   - Logger les erreurs pour le monitoring
#   - Handler global pour les exceptions non gérées (500)
# ============================================================
