from fastapi import APIRouter, Depends, Response, HTTPException, status
from database import get_db
import schemas, model, authorization.token 
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm

psw_ctx = CryptContext(schemes=['bcrypt'], deprecated = "auto")

router = APIRouter(
    prefix= "/login",
    tags = ["Login"]
)

@router.post("/", response_model=schemas.Token)
async def login(request : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.email == request.username).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credential")
    
    if not psw_ctx.verify(request.password, user.password): #user is from the filter above
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password")
    
    access_token = authorization.token.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}