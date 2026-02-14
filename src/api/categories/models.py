from sqlalchemy import Boolean, Column, DateTime, Integer, String, func, text
from sqlalchemy.orm import relationship
from src.core.database import Base


class Category(Base):
  __tablename__ = "kx_categories"

  id_category = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(100), nullable=False)
  img_url = Column(String(256), nullable=False)
  is_enable = Column(Boolean, server_default=text("true"))
  created_at = Column(DateTime, server_default=func.now())
  updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

  # 🔁 Relationship
  groups = relationship("Group", back_populates="category", order_by="Group.id_group")
