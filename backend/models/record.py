from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base

class Record(BM, Base):
    
    __table__ = "records"
    
    # foreign key references and relationships
    patientId = Column(
        String(40), ForeignKey("patients.id")
    ) # patient ID associated with the record