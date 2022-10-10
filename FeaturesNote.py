from pydantic import BaseModel

class FeatureNote(BaseModel):
    bike_name : int
    city : int
    kms_driven : int
    owner : int
    age : int
    power : float
    brand : int