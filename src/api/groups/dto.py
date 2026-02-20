from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict

class GroupDTO(BaseModel): 
  id_group: int
  name: str
  is_enable: bool
  created_at: datetime
  updated_at: datetime
  category_id: int

  model_config = ConfigDict(from_attributes=True)