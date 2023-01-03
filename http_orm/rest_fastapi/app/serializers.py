from pydantic import BaseModel, Field

class ProductSerializer(BaseModel):
    id: int
    title: str
    price: float = Field(default=None)
    quantity: int = Field(default=None)
    description: str = Field(default=None)

    class Config:
        orm_mode = True

class ProductCreateSerializer(BaseModel):
    title: str
    price: float = Field(default=None)
    quantity: int = Field(default=None)
    description: str = Field(default=None)

class ProductUpdateSerializer(BaseModel):
    title: str = Field(default=None)
    price: float = Field(default=None)
    quantity: int = Field(default=None)
    description: str = Field(default=None)
