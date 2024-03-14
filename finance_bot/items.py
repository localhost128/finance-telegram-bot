from dataclasses import dataclass
from datetime import datetime

import db


CATEGORIES = list(map(lambda x: x[0], db.fetchall(sql="select name from category")))
# CATEGORIES = dict(db.fetchall(sql="select * from category"))


@dataclass
class Item:
    name: str
    cost: int
    date: datetime = datetime.now()
    id: int | None = None
    category: str | None = None


def confirm() -> None:
    db.commit()


def cancel() -> None:
    db.close_conection()


def add_item(item: Item) -> None:
    sql = "INSERT INTO item(name, cost, date, category) VALUES (?, ?, ?, ?)"

    if item.category:
        category = CATEGORIES.index(item.category) + 1
    else:
        category = None

    db.execute(sql, (item.name, item.cost, item.date, category))


def predict_category(item_name: str) -> str | None:
    sql = f'SELECT DISTINCT category FROM item WHERE name = "{item_name}"'
    print(sql)
    if res := db.fetchall(sql):
        return CATEGORIES[res[0][0] - 1]
    return None
