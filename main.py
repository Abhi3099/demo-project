#This is where our api lives
from fastapi import FastAPI, Depends,HTTPException,status
from . import services,schemas,models,database
from sqlalchemy.orm import Session
from typing import List

app= FastAPI()

#services.create_db()
models.Base.metadata.create_all(bind=database.engine)

@app.post("/users/",status_code=status.HTTP_201_CREATED)
#Session is basically a session within our database
def create_user(user:schemas.UserBase, db:Session=Depends(services.get_db)):
    return services.create_user(db=db,user=user)


@app.get("/users/",status_code=200)
def read_users(skip:int=0,limit:int=10 , db:Session=Depends(services.get_db)):
    users=services.get_users(db=db,skip=skip,limit=limit)
    return users

@app.get("/users/{user_id}",status_code=200)
def get_user(user_id:int ,db:Session=Depends(services.get_db)):
    user=services.get_user(db=db,user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'sorry user with id {user_id} does not exist')

    return user


@app.delete("/deluser/{id}")
def del_users(id:int,db:Session=Depends(services.get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'sorry user with id {id} does not exist')
    else:
       db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
       db.commit()
       raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f'User with id {id} has been successfully deleted')
    
    #return {"Done":f'user with id {id} is deleted'}
    
   
    
