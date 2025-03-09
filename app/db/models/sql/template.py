from sqlalchemy import Column, Integer, String
from .base_model import Base

class Template(Base):
    __tablename__ = "templates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    product_type = Column(String, nullable=False)
    view_angle = Column(String, nullable=False)
    model_type = Column(String, nullable=False)
    template_path = Column(String, nullable=False)
