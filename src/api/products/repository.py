from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.api.products.models import Product

# GetAll
def get_all(db: Session):
  try:
    return db.query(Product).all()
  except SQLAlchemyError as e:
    raise e