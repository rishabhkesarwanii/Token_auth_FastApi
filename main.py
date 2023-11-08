from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestFormStrict

app = FastAPI()

@app.get("/test/")
async def test():
    return {"Hello":"world"}

