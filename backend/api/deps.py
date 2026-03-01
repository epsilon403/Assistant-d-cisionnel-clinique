# Re-export common dependencies so endpoints can import from one place
from backend.db.session import get_db  # noqa: F401
