from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.api.categories.models import Category

# GetAll
def get_all(db: Session):
  try:
    return db.query(Category).all()
  except SQLAlchemyError as e:
    raise e
