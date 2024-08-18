from uuid import uuid4
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import models

Base = declarative_base()

class BM:
    id = Column(
        String(40), primary_key=True, index=True
    )
    created_at = Column(Integer)
    modified_at = Column(Integer)
    archived = Column(Boolean, default=False)
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in ["__class__", "id", "modified_at", "created_at"]:
                setattr(self, key, value)
        setattr(self, "created_at", int(datetime.now().timestamp()))
        setattr(self, "modified_at", int(datetime.now().timestamp()))
        
        # Generates a unique ID for the instance
        setattr(self, "id", str(uuid4()))
        
        # Save the instance after initialization
        self.save()