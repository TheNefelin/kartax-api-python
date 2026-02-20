from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from . import models, dto

# GET ALL
def get_all(db: Session):
  try:
    items = db.query(models.Group).all()
    return [dto.GroupDTO.model_validate(item) for item in items]
  except SQLAlchemyError as e:
    raise e
  
# GET BY ID
def get_by_id(id: int, db: Session):
  try:
    item = db.query(models.Group).filter(models.Group.id_group == id).first()
    return dto.GroupDTO.model_validate(item)
  except SQLAlchemyError as e:
    raise e
  
# GET BY ID CATEGORY
def get_by_id_category(id: int, db: Session):
  try:
    items = db.query(models.Group).filter(models.Group.category_id == id).all()
    return [dto.GroupDTO.model_validate(item) for item in items]
  except SQLAlchemyError as e:
    raise e