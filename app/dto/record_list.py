# Author: Anton Mikhaylov
# Created: 16/08/2020
from typing import Dict, List, Any

from pydantic import BaseModel


class LogRecordListDTO(BaseModel):
    amount: int = None
    offset: int = None
    messages: List[Dict[str, Any]] = None
    next_offset: int = None
