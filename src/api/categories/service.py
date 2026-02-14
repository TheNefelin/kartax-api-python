from fastapi import UploadFile
from sqlalchemy.orm import Session

from src.api.categories.models import Category
from src.services.cloudinary_service import delete_image, upload_image_16_9

PATH = "kartax"

def create_with_images(
  name: str,
  file: UploadFile,
  db: Session
):
  public_id = None

  try:
    url, public_id = upload_image_16_9(
      file_bytes=file.file.read(),
      folder=PATH
    )

    new_item = Category(
      name=name,
      img_url=url
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item    
  except Exception as e:
    db.rollback()

    if public_id:
      try:
        delete_image(public_id)
      except Exception:
        pass

    raise e