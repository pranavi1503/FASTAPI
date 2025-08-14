from fastapi import FastAPI, Depends, HTTPException
from app.auth import authenticate_user, create_access_token, get_current_user
from app.database import database_connection
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
import pandas as pd

app = FastAPI()

# Use JSON-based login instead of form
class LoginRequest(BaseModel):
    username: str
    password: str
engine = database_connection()

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = create_access_token(data={"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/data")
def get_data(current_user: dict = Depends(get_current_user)):
    print(current_user)
    df = pd.read_sql("select * from healthdataset limit 10", engine)
    #print("Fetched DataFrame:")
    #print(df)
    return df.to_dict(orient="records")
    #return df.to_dict(orient="records")
