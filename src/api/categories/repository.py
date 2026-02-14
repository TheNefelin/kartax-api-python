from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, contains_eager, joinedload

from src.api.categories.models import Category
from src.api.groups.models import Group
from src.api.products.models import Product

# GetAll Public
def get_all_public(db: Session):
  try:
    return (
      db.query(Category)
      .join(Category.groups)
      .join(Group.products)
      .filter(
        Category.is_enable == True,
        Group.is_enable == True,
        Product.is_enable == True
      )
      .options(contains_eager(Category.groups).contains_eager(Group.products))
      .all()
    )
  except SQLAlchemyError as e:
    raise e    

# GetAll
def get_all(db: Session):
  try:
    return (
      db.query(Category)
      .options(joinedload(Category.groups).joinedload(Group.products))
      .all()
    )
  except SQLAlchemyError as e:
    raise e

