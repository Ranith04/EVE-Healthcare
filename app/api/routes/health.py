from fastapi import APIRouter, Response, status
from sqlalchemy import text
from app.db.session import SessionLocal

router = APIRouter()

@router.get("/health")
def health_check(response: Response) -> dict[str, str]:
    try:
        with SessionLocal() as session:
            session.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "unhealthy", "details": "Database is unreachable"}
