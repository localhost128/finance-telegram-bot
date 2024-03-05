from dataclasses import dataclass
from datetime import datetime


@dataclass
class Category:
    id: int
    name: str


@dataclass
class Item:
    name: str
    cost: int
    date: datetime = datetime.now()
    id: int | None = None
    category: int | None = None
