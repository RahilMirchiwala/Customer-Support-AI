from pydantic import BaseModel
from typing import Literal

class SupportTicket(BaseModel):
    message: str

class SupportResponse(BaseModel):
    category: Literal["Billing", "Technical", "General"]
    priority: Literal["High", "Medium", "Low"]
    response: str