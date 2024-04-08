from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from authorization import oauth2
from database import get_db
import model, schemas
from respository import user

router = APIRouter(
    prefix = "/User",
    tags = ["User"]
)

#create users
@router.post("/", status_code=201)
async def create_user(request: schemas.User, db : Session = Depends(get_db)):
    return user.User.new_user(request, model.User, db)

@router.get("/getallusers", status_code=201, response_model= List[schemas.GetUser])
def get_user(response: Response, db : Session = Depends(get_db), current_user : schemas.GetUser = Depends(oauth2.get_current_user)):
    return user.User.all_user(db, model.User)

@router.get("/getbyid/{id}", status_code=201, response_model= schemas.GetUser)
def get_user_id(id, response: Response, db : Session = Depends(get_db), current_user : schemas.GetUser = Depends(oauth2.get_current_user)):
    return user.User.one_user(id, db, model.User)

@router.delete("/deletebyid/{id}", status_code=201)
def delete_by_id(id, db: Session = Depends(get_db), current_user : schemas.GetUser = Depends(oauth2.get_current_user)):
    return user.User.delete_user(id, db, model.User)

@router.post("/updatebyid/{id}", status_code=201)
def update_by_id(id, request: schemas.UpdateUser, db: Session = Depends(get_db), current_user : schemas.GetUser = Depends(oauth2.get_current_user)):
    return user.User.update_user(id, db, model.User, request)