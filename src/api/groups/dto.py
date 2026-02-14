from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict

from src.api.products.dto import ProductDTO

class GroupDTO(BaseModel): 
  id_group: int
  name: str
  is_enable: bool
  created_at: datetime
  updated_at: datetime
  category_id: int

  products: List[ProductDTO]

  model_config = ConfigDict(from_attributes=True)