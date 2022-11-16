from pydantic import BaseModel


class MetaData(BaseModel):
    file_name: str
    caption: str
    user_id: str
    project_number: int
    report_number: int
