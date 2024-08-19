from sqlalchemy import Column, Double, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base

class Vital(BM, Base):
    __tablename__ = "vitals"
    
    # Foreign keys & relationships
    
    takenById = Column(
        # ID of the HCW who took the vital signs
        String(40), ForeignKey("hcws.id")
    ) 
    # relationship with the HCW model
    takenBy = relationship("HCW")
    
    takenForId = Column(
        # ID of the patien the vitals were taken for
        String(40), ForeignKey("patients.id")
    )
    # relationship with the Patient model
    takenFor = relationship("Patient")
    
    # Status indicating normal or abnormal vitals
    status = Column(
        Boolean, default=True
    )
    
    # temperature measurement
    temp = Column(Double)
    # Blood pressure measurement
    bp = Column(String(40))
    # Beats per minutes (heart rate)
    bpm = Column(Integer)
    # weight measurement
    weight = Column(Double)
    # height measurement
    height = Column(Double)
    # glucose level measurement
    glucose = Column(Double)
    # custom additional date for vitals
    custom = Column(String(2048))
    # additional notes related to the vitals
    notes = Column(String(2048))
    