#gestion des tokens JWT

import jwt
import secrets
from datetime import datetime, timedelta
from fastapi import HTTPException

SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"

# Générer un token JWT
def create_jwt_token(device_id: str):
    expiration = datetime.utcnow() + timedelta(hours=2)
    payload = {"device_id": device_id, "exp": expiration}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Vérifier un token JWT (validité + expiration)
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["device_id"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expiré")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token invalide")