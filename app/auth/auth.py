from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import firebase_admin
from firebase_admin import auth, credentials
from dotenv import load_dotenv
import os

load_dotenv()

# print("FIREBASE_PROJECT_ID:", os.getenv("FIREBASE_PROJECT_ID"))
# print("FIREBASE_PRIVATE_KEY_ID:", os.getenv("FIREBASE_PRIVATE_KEY_ID"))
# print("FIREBASE_PRIVATE_KEY:", os.getenv("FIREBASE_PRIVATE_KEY"))
# print("FIREBASE_CLIENT_EMAIL:", os.getenv("FIREBASE_CLIENT_EMAIL"))

# print(repr(os.getenv("FIREBASE_PRIVATE_KEY")))


cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace('\\n', '\n'),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL")
})

firebase_admin.initialize_app(cred)

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        print("Token received in backend:", token)
        decoded_token = auth.verify_id_token(token)
        print("Decoded token:", decoded_token)
        return decoded_token
    except Exception as e:
        print("Firebase verification failed:", e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
