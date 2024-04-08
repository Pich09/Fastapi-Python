from fastapi import HTTPException, status
from hashpassword import hashing


class User:
    
    def new_user(request, model, db):
        hashed_password = hashing.HashPassword.hashing(request.password)
        new_user = model(email = request.email, username = request.username, password = hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return "Created Account"
    
    def all_user(db, model):
        user = db.query(model).all()
        return user
    
    def one_user(id, db, model):
        one_user = db.query(model).filter(model.id == id).first()
        if not one_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"User with id {id} not found")
        return one_user
    
    def delete_user(id, db, model):
        user = db.query(model).filter(model.id == id)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"User with id {id} not found")
        user.delete(synchronize_session=False)
        db.commit()
        return "Deleted Account"
    
    def update_user(id, db, model, request):
        getuser = db.query(model).filter(model.id == id)
        if not getuser:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"User with id {id} not found")
        getuser.update({"username": request.username})
        db.commit()
        return "Updated"