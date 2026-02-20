from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from src.core.database import Base

class Group(Base):
  __tablename__ = "kx_groups"

  id_group = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(100), nullable=False)
  is_enable = Column(Boolean, nullable=False)  # Use Text for longer content
  created_at = Column(DateTime, server_default=func.now())
  updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

  # 🔗 Foreign Keys
  category_id = Column(Integer,ForeignKey("kx_categories.id_category"),nullable=False)
    
  # 🔁 Relationships
  category = relationship("Category", back_populates="groups")
  products = relationship("Product", back_populates="group")
