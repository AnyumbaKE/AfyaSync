from uuid import uuid4
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import models

# Declaring a base class for SQLAlchemy models
Base = declarative_base()

# Defining base model class with common attributes and methods
class BM:
    """Defining columns for the base model"""
    id = Column(
        String(40), primary_key=True, index=True
    )
    # Identifier for each instance

    created_at = Column(Integer) #Timestamp for creation time
    modified_at = Column(Integer) #Timestamp for the last modification time

    # Flag to indicate if the instance is archived
    archived = Column(Boolean, default=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in ["__class__", "id", "modified_at", "created_at"]:
                setattr(self, key,value)
        # Setting the creation and modification timestamps
        setattr(self, "created_at", int(datetime.now().timestamp()))
        setattr(self, "modified_at", int(datetime.now().timestamp()))
        # Generating a unique ID for the instance
        setattr(self, "id", str(uuid4()))
        self.save() # Save the instance after initialization

        def save(self):
            """saves the update with the current datetime and saves the instance"""
            setattr(self, "modified_at", int(datetime.now().timestamp()))
            # adds the instance to the database session
            models.database.new(self)
            # Saves changes to the database
            models.database.save()

        def delete(self):
            """deleting the current instance from the database"""
            models.database.delete(self)

        def archive(self):
            """setting the archive attribute to true and save the instance"""
            setattr(self, "archived", True)
            # saving the instance after archiving
            self.save()

        def to_dict(self):
            """returns a dictionary containing all keys/values of the instance"""
            from api.base import (
                timestamp_to_str,
            ) # import a function for timestamp conversion

            new_dict = {}
            for key, value in self.__dict__.items():
                if isinstance(value, (int, float, str, bool, list, dict, tuple)):
                    if key in ["created_at", "modified_at", "time"]:
                        # Format timestamp to string
                        value = timestamp_to_str(
                            value, "%Y-%m-%d at %I:%M %p"
                        )
                    if key == "birthDate":
                        # Format birthdate to string
                        value = timestamp_to_str(
                            value, "%Y-%m-%d"
                        )
                    new_dict[key] = value
            # Return the dictionary representation of the instance
            return new_dict
