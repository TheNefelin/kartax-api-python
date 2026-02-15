from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload, contains_eager

from src.api.mobile.dto import CategoryHierarchyDTO
from src.api.categories.models import Category
from src.api.groups.models import Group
from src.api.products.models import Product

# GetAll con jerarquía  
def get_all_hierarchy(db: Session):
  try:
    #items = (
    #  db.query(Category)
    #  .join(Category.groups)            # JOIN a Group
    #  .join(Group.products)             # JOIN a Product
    #  .filter(
    #    Category.is_enable == True,
    #    Group.is_enable == True,
    #    Product.is_enable == True
    #  )
    #  .options(
    #    contains_eager(Category.groups)
    #    .contains_eager(Group.products) # evita lazy loading
    #  )
    #  .all()
    #)

    items = (
      db.query(Category)
      .options(
        joinedload(Category.groups.and_(Group.is_enable == True))
        .joinedload(Group.products.and_(Product.is_enable == True))
      )
      .filter(Category.is_enable == True)
      .all()
    )

    return [CategoryHierarchyDTO.model_validate(item) for item in items]
  except SQLAlchemyError as e:
    raise e
