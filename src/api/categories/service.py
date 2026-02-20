from fastapi import UploadFile
from sqlalchemy.orm import Session

from src.services.cloudinary_service import delete_image, upload_image_16_9
from . import repository, models

PATH = "kartax"

# CREATE
def create_with_images(name: str, file: UploadFile, db: Session):
  public_id = None

  try:
    url, public_id = upload_image_16_9(
      file_bytes=file.file.read(),
      folder=PATH
    )

    new_item = models.Category(
      name=name,
      img_url=url
    )

    new_item = repository.create(
      name=name,
      img_url=url,
      db=db
    )

    return new_item 
  except Exception as e:
    db.rollback()

    if public_id:
      try:
        delete_image(public_id)
      except Exception:
        pass

    raise e

# DELETE
def delete_with_images(id: int, db: Session):
  try:
    item = repository.get_model_by_id(id, db)

    if not item:
      return None

    if item.groups:
      raise ValueError("No se puede eliminar la categoria porque tiene grupos asociadas")

    public_id = extract_public_id(item.img_url)

    delete_image(public_id)
    repository.delete(id, db)
    
    return 1
  except Exception as e:
    raise e

# Extraer public_id de Cloudinary
def extract_public_id(url: str) -> str | None:
  """
  Extrae:
  news/o6md6byxzpbnygtak05j
  desde:
  https://res.cloudinary.com/.../upload/v1770756121/kartax/o6md6byxzpbnygtak05j.webp
  """
  try:
    # Quitar todo antes de /upload/
    after_upload = url.split("/upload/")[1]
    # Quitar la versión (v1770756121)
    parts = after_upload.split("/", 1)[1]
    # Quitar extensión
    public_id = parts.rsplit(".", 1)[0]

    return public_id
  except Exception:
    return None
