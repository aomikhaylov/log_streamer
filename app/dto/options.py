# Author: Anton Mikhaylov
# Created: 16/08/2020
from pydantic import BaseModel


class LogRecordOptionsDTO(BaseModel):
    offset: int = 0
    limit: int = 0
