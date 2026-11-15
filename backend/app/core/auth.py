import secrets
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.core.config import settings

security = HTTPBasic(auto_error=False)

def require_owner(credentials: HTTPBasicCredentials | None = Depends(security)):
    if not credentials or not (
        secrets.compare_digest(credentials.username.encode(), settings.owner_username.encode())
        and secrets.compare_digest(credentials.password.encode(), settings.owner_password.encode())
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True
