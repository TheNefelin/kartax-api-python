from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict

class CategoryDTO(BaseModel): 
  id_category: int
  name: str
  img_url: str
  is_enable: bool
  created_at: datetime
  updated_at: datetime

  model_config = ConfigDict(from_attributes=True)
