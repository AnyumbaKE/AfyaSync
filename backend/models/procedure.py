from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base

class Procedure(BM, Base):
    __tablename__ = "procedures"
    
    # foreign key references & relationships
    prescribedById = Column(
        String(40), ForeignKey("hcws.id")
    )
    # prescribed by HCW - doctor
    prescribedBy = relationship(
        "HCW", foreign_keys=[prescribedById]
    )
    # relationship with HCW model
    performedById = Column(
        String(40), ForeignKey("hcws.id")
    )
    # patient ID for whom the procedure is performed
    patient = relationship("Patient")
    # relationship with patient model
    status = Column(
        Boolean, default=False
    ) # status of the procedure -completed or not-
    # name of the procedure
    name = Column(String(150))
    # additional notes for the procedure
    notes = Column(String(2048))
    