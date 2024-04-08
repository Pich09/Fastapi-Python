from fastapi import HTTPException, status


class Blogs:
    
    def new_blog(request, model, db, current_user):
        new_blog = model(title = request.title, information = request.information, userID = current_user["id"])
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        return "Created Blog"
    
    '''def all_user(db, model):
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
        return "Updated"'''