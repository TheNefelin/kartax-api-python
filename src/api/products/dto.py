from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict

class ProductDTO(BaseModel):
  id_product: int
  name: str
  description: str
  price: Decimal
  img_url: str
  is_fractional: bool
  base_unit: str
  sale_unit: Optional[Decimal]
  stock: Decimal
  waste_percentage: Decimal
  is_enable: bool
  created_at: datetime
  updated_at: datetime
  parent_product_id: Optional[int]
  group_id: int

  model_config = ConfigDict(from_attributes=True)