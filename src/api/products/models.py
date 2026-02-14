from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, func
from sqlalchemy.orm import relationship

from src.core.database import Base

class Product(Base):
  __tablename__ = "kx_products"

  id_product = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(100), nullable=False)
  description = Column(String(256), nullable=False)
  price = Column(Numeric(10, 2), nullable=False)
  img_url = Column(String(100), nullable=False)
  is_fractional = Column(Boolean, nullable=False, server_default="false")
  base_unit = Column(String(20), nullable=False)
  sale_unit = Column(Numeric, nullable=True)
  stock = Column(Numeric, nullable=False, server_default="0")
  waste_percentage = Column(Numeric(5, 2), nullable=False, server_default="0")
  is_enable = Column(Boolean, nullable=False, server_default="true")
  created_at = Column(DateTime, server_default=func.now())
  updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

  # 🔗 Foreign Keys
  parent_product_id = Column(Integer, ForeignKey("kx_products.id_product"), nullable=True)
  group_id = Column(Integer, ForeignKey("kx_groups.id_group"), nullable=False)

  # 🔁 Relationships
  parent = relationship("Product", remote_side=[id_product], backref="variants")
  group = relationship("Group", back_populates="products")
