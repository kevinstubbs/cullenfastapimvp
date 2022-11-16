from pydantic import BaseModel


class MetaData(BaseModel):
    folder_name: str
    file_name: str
    caption: str
    user_id: str
    project_number: int
    report_number: int
