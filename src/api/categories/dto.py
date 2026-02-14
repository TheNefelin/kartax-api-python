from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict

from src.api.groups.dto import GroupDTO

class CategoryDTO(BaseModel): 
  id_category: int
  name: str
  img_url: str
  is_enable: bool
  created_at: datetime
  updated_at: datetime

  groups: List[GroupDTO]

  model_config = ConfigDict(from_attributes=True)
