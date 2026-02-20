from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from . import models, dto

# GET ALL
def get_all(db: Session):
  try:
    items = db.query(models.Product).all()
    return [dto.ProductDTO.model_validate(item) for item in items]
  except SQLAlchemyError as e:
    raise e

# GET BY ID
def get_by_id(id: int, db: Session):
  try:
    item = db.query(models.Product).filter(models.Product.id_product == id).first()
    return dto.ProductDTO.model_validate(item)
  except SQLAlchemyError as e:
    raise e
  
# GET BY ID GROUP
def get_by_id_group(id: int, db: Session):  
  try:
    items = db.query(models.Product).filter(models.Product.group_id == id).all()
    return [dto.ProductDTO.model_validate(item) for item in items]
  except SQLAlchemyError as e:
    raise e
