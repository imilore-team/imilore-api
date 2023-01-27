from pydantic import BaseModel
from datetime import datetime


class InMlDataModel(BaseModel):
    time: int
    value: float
    error: bool
    warn: bool

class InMlDiskTableModel(BaseModel):
    title: str
    description: str
    disk_id: str
    data: list[InMlDataModel]

class OutSmallMlDiskTableModel(BaseModel):
    id: int
    title: str
    description: str
    disk_id: str

class OutMlDiskDataModel(BaseModel):
    time: datetime
    value: float
    error: bool
    warn: bool

class OutMlDiskTableModel(BaseModel):
    id: int
    title: str
    description: str
    disk_id: str
    data: list[OutMlDiskDataModel]