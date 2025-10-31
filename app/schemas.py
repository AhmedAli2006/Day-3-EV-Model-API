from pydantic import BaseModel

class EVInput(BaseModel):
    Site: int
    CP_ID: int
    Connector_Type: int
    Duration_hours: float
    hour: int
    day_of_week: int
    month: int
    Postcode: int

