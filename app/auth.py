from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "yBrOevAqjoZjX9OkeVexbFnonOyiYDQ7LlnQY5GnRmM"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users = {
    "admin": {
        "username": "admin",
        "password": "$2b$12$mUaYNvsn4VV0nthPiAKLcerkTEq2.yOOylPQlQiSO1IbdaUAul0EK"  # "admin123"
    },
    "testuser": {
        "username": "testuser",
        "password": "$2b$12$akrSRi/9LwvHO3bzlK0JgOXOrL5.J68hMmbtnAYnbYWkjm5mLzjne"  # "test123"
    }
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    print("Verifying password...")
    result = pwd_context.verify(plain_password, hashed_password)
    print("Password verified:", result)
    return result


def authenticate_user(username: str, password: str):
    print("Authenticating user...")
    user = fake_users.get(username)
    if not user:
        print("Username not found")
        return False
    if not verify_password(password, user["password"]):
        print("Password mismatch")
        return False
    print("Authentication successful")
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None or username not in fake_users:
            raise HTTPException(status_code=401, detail="Invalid token or user")
        return {"username": username}
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
