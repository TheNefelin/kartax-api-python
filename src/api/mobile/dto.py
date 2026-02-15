from typing import List
from pydantic import ConfigDict

from src.api.categories.dto import CategoryDTO
from src.api.groups.dto import GroupDTO
from src.api.products.dto import ProductDTO

class GroupHierarchyDTO(GroupDTO): 
  products: List[ProductDTO]

  model_config = ConfigDict(from_attributes=True, orm_mode=True)

class CategoryHierarchyDTO(CategoryDTO): 
  groups: List[GroupHierarchyDTO]

  model_config = ConfigDict(from_attributes=True, orm_mode=True)

  