#works as a middle mam between the api and the database
from . import database , schemas,models
from sqlalchemy.orm import Session

#creating the database
#def create_db():
    #return models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db=database.session_local()
    try:
        yield db
    finally:
        db.close()

def create_user(db:Session,user:schemas.UserBase):
    db_user = models.User(First_Name=user.First_Name,Last_Name=user.Last_Name,DOB=user.DOB)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db:Session,skip:int,limit:int):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user(db:Session,user_id:int):
    return db.query(models.User).filter(models.User.id==user_id).first()

#def del_user(db:Session,user_id:int):
    #db.query(models.User).filter(models.User.id==user_id).delete(synchronize_session=False)
    #db.commit()
    #return 'done'
    #query(models.User).filter(models.User.id==user_id).delete(synchronize_session='evaluate')
    
    
#def destroy(id:int, db:Session):
   # user = db.query(models.User).get(id)
   #db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
  # db.commit()
  # return f'user with id {id} is deleted'


