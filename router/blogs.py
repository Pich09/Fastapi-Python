from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from authorization import oauth2
from database import get_db
import model, schemas
from respository import blogs

router = APIRouter(
    prefix = "/Blogs",
    tags = ["Blog"]
)

#create users
@router.post("/", status_code=201)
async def create_user(request: schemas.Blogs, current_user: dict = Depends(oauth2.get_current_user), db : Session = Depends(get_db)):
    new_blog = model.Blogs(title = request.title, information = request.information, userEmail = current_user)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return "Created Blog"

@router.get("/getallblogs", status_code=201, response_model= List[schemas.Blogs])
def get_blogs(current_user: dict = Depends(oauth2.get_current_user), db : Session = Depends(get_db)):
    report = db.query(model.Blogs).filter(model.Blogs.userEmail == current_user).all()
    return report


'''@router.get("/getbyid/{id}", status_code=201, response_model= schemas.GetUser)
def get_user_id(id, response: Response, db : Session = Depends(get_db), current_user : schemas.GetUser = Depends(oauth2.get_current_user)):
    return user.User.one_user(id, db, model.User)

@router.delete("/deletebyid/{id}", status_code=201)
def delete_by_id(id, db: Session = Depends(get_db), current_user : schemas.GetUser = Depends(oauth2.get_current_user)):
    return user.User.delete_user(id, db, model.User)

@router.post("/updatebyid/{id}", status_code=201)
def update_by_id(id, request: schemas.UpdateUser, db: Session = Depends(get_db), current_user : schemas.GetUser = Depends(oauth2.get_current_user)):
    return user.User.update_user(id, db, model.User, request)'''