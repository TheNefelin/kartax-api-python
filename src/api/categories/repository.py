from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from . import dto, models

# GET All
def get_all(db: Session):
  try:
    items = db.query(models.Category).all()
    return [dto.CategoryDTO.model_validate(item) for item in items]
  except SQLAlchemyError as e:
    raise e

# GET BY ID
def get_by_id(id: int, db: Session):
  try:
    item = db.query(models.Category).filter(models.Category.id_category == id).first()
    return dto.CategoryDTO.model_validate(item)
  except SQLAlchemyError as e:
    raise e

# CREATE
def create(name: str, img_url: str, db: Session):
  try:
    item = models.Category(
      name=name,
      img_url=img_url
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return dto.CategoryDTO.model_validate(item)
  except IntegrityError as e:
    db.rollback()
    raise ValueError("Error de integridad en la base de datos")  
  except SQLAlchemyError as e:
    db.rollback()
    raise e

# DELETE
def delete(id: int, db: Session):
  try:
    item = db.query(models.Category).filter(models.Category.id_category == id).first()
    
    
    if not item:
      return 0

    db.delete(item)
    db.commit()

    return 1
  except IntegrityError as e:
    db.rollback()
    raise ValueError("Error de integridad en la base de datos")  
  except SQLAlchemyError as e:
    db.rollback()
    raise e
