from pydantic import BaseModel


class EmployeeModel(BaseModel):
    first_name: str
    last_name: str
    mail : str | None = None  # optional param
    mobile_number : str