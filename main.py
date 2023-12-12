from fastapi import FastAPI, HTTPException ,UploadFile ,File,Depends
from storage.database import get_db
from fastapi.responses import StreamingResponse
from io import BytesIO
from crud import querydata
from sqlalchemy.orm import Session
from models import properties
from storage.database import engine
from base64 import b64encode
properties.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/register")
async def upload_image(full_name:str, password:str ,email:str,phone:str,image: UploadFile = File(...),db:Session = Depends(get_db)):
    image_data = await image.read()
    image_base64 = b64encode(image_data).decode("utf-8")
    data = querydata.post_user(db,full_name,password,email,phone,image_base64,image)
    if data:
        return {"Profile Created"}
    raise HTTPException(status_code=403, detail="Email ID is Already Exist")



@app.get("/users")
async def index(db:Session = Depends(get_db)):
    data = querydata.get_user(db)
    for i in data:
        i.profile_pic = 'http://localhost:8000/profile/image/'+str(i.id)
    return data

@app.get("/profile/image/{user_id}/")
async def get_image(user_id: int,db:Session = Depends(get_db)):
    data = querydata.get_image_by_user_id(db,user_id)
    if data:
        filename= data.filename
        content_type = data.content_type 
        image_data_base64 = data.image
        image_data = BytesIO(b64encode(image_data_base64.encode("utf-8")))
        return StreamingResponse(
    content=image_data,
    media_type=content_type,
    headers={"Content-Disposition": f"inline; filename={filename}"}
)
    else:
        raise HTTPException(status_code=404, detail="Image not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)