from pydantic import BaseModel
from typing import Optional

class ReadmeRequest(BaseModel):
    """
    Schema for the request to generate a README file.
    """
    repo_name: str
    repo_description: str
    author: Optional[str] = None
    license: Optional[str] = "MIT"

class ReadmeResponse(BaseModel):
    """
    Schema for the response containing the generated README content.
    """
    content: str
