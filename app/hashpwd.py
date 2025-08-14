from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
hashed = pwd_context.hash("admin123")
print("Hashed password:", hashed)
hashed=pwd_context.hash("test123")
print("Hashed password:", hashed)
hashed=pwd_context.hash("secret")
