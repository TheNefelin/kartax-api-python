# GetAll
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.api.groups.models import Group

# GetAll
def get_all(db: Session):
  try:
    return db.query(Group).all()
  except SQLAlchemyError as e:
    raise e