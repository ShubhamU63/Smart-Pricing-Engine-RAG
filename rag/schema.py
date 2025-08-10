from pydantic import BaseModel, Field
from typing import List, Optional


class Labor(BaseModel):
    hours: float
    rate_per_hour: float
    total: float


class Task(BaseModel):
    name: str
    estimated_duration: str
    labor: Labor
    material_cost: float
    vat_rate: float
    total_price: float
    margin: float
    confidence_score: float


class Zone(BaseModel):
    name: str

class Quote(BaseModel):
    system: str = "System T"
    zones: List[Zone]
    tasks: List[Task]
    margin: Optional[float] = Field(None, description="Average margin across all tasks")
