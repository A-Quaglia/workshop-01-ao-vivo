from datetime import datetime

from pydantic import BaseModel, PositiveFloat, PositiveInt, EmailStr

from enum import Enum

class CategoriaEnum(str, Enum):
    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"


class Vendas(BaseModel):
    """
    Contrato formato dos dados
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    produto: str
    quantidade: PositiveInt
    categoria: CategoriaEnum
