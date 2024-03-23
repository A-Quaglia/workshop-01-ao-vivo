from datetime import datetime

from pydantic import BaseModel, PositiveFloat, PositiveInt

from enum import Enum

class CategoriaEnum(str, Enum):
    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"


class Vendas(BaseModel):
    email: str
    data: datetime
    valor: PositiveFloat
    produto: str
    quantidade: PositiveInt
    categoria: CategoriaEnum
