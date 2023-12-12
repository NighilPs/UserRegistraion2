from sqlalchemy.orm import Session
from models.properties import User,Profile



def get_user(db: Session):
    return db.query(User).all()

def get_image_by_user_id(db,user_id):
    return db.query(Profile).filter(Profile.user_id == user_id).first()
    
def post_user(db:Session,full_name,password,email,phone,image_base64,image):
    email_exist = db.query(User).filter(User.email == email).first()
    if not email_exist:
        data = User(full_name = full_name,password = password,email=email,phone=phone)
        db.add(data)
        db.commit()

        data = Profile(user_id=data.id ,image = image_base64,content_type = image.content_type,filename=image.filename)
        db.add(data)
        db.commit()

        return True
    return False
