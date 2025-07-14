from pydantic import BaseModel, Field


class IrisModel(BaseModel):
    sepal_length: float = Field(..., description="Length of the sepal")
    sepal_width: float = Field(..., description="Width of the sepal")
    petal_length: float = Field(..., description="Length of the petal")
    petal_width: float = Field(..., description="Width of the petal")
    
    class Config:
        json_schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2,
            }
        }