from pydantic import BaseModel
from typing import Optional

class MetaData(BaseModel):
    folder_name: str
    file_name: str
    caption: str
    user_id: Optional[str]
    project_number: Optional[int]
    report_number: Optional[int]


class MetaDataRequest(BaseModel):
    data: list[MetaData]
