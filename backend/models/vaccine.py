from models.base import BM, Base
from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Vaccine(BM, Base):
    __tablename__ = "vaccines"
    
    # foreign keys and relationships
    
    administeredForId = Column(
        String(40), ForeignKey("patients.id")
    )
    # ID of the patient receiving the vaccine