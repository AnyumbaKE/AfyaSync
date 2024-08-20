from models.base import BM, Base
from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Vaccine(BM, Base):
    __tablename__ = "vaccines"
    
    # foreign keys and relationships
    
    administeredForId = Column(
        String(40), ForeignKey("patients.id")
    ) # ID of the patient receiving the vaccine
    
    administeredFor = relationship(
        "Patient", back_populates="vaccines"
    ) # relationship with the patient model
    
    administeredById = Column(
        String(40), ForeignKey("hcws.id")
    ) # ID of the HCW administering the vaccine
    
    administeredBy = relationship("HCW") # relationship with the HCW model
    drugId = Column(
        String(60), ForeignKey("drugs.id")
    ) # ID of the drug used for the vaccine
    
    drug = relationship("Drug", uselist=True) # relationship with the drug model
    
    notes = Column(String(2048)) # Additional notes about the vaccine administration
    