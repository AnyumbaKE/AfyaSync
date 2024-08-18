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
    
    def save(self):
        setattr(self, "modified_at", int(datetime.now().timestamp()))
        # Adding the instance to the database session
        models.database.new(self)
        # Saving changes to the database
        models.database.save()
        
    def delete(self):
        # Deleting the instance from the database
        models.database.delete(self)
    
    def archive(self):
        setattr(self, "archived", True)
        # Saving the instance after archiving
        self.save()
    
    def to_dict(self):
        from api.base import (
            timestamp_to_str,
        )
        
        new_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (int, float, str, bool, list, dict, tuple)):
                if key in ["created_at", "modified_at", "time"]:
                    value = timestamp_to_str(
                        value, "%Y-%m-%d at %I:%M %p"
                    ) # Format timestamp to string
                
                if key == "birthDate":
                    value = timestamp_to_str(
                        value, "%Y-%m-%d"
                    ) # Format birth date to string
                    new_dict[key] = value
        return new_dict # Return the dictionary representation of the instance