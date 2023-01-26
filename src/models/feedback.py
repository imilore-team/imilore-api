from pydantic import BaseModel, Field


class InFeedbackModel(BaseModel):
    email: str = Field(
        regex=r"\A[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}\Z", 
        example="example@example.com"
    )
    description: str = Field(max_length=10000)