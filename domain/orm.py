from enum import auto
import sqlalchemy as sql
from sqlalchemy.orm import mapper, relationship

import domain

metadata = sql.MetaData()

order_lines = sql.Table(
    "order_lines", 
    metadata,
    sql.Column("id", sql.Integer, primary_key=True, autoincrement=True),
    sql.Column("sku", sql.String(255)),
    sql.Column("qty", sql.Integer, nullable=False),
    sql.Column("orderid", sql.String(255)),
)



def start_mappers():
    lines_mapper = mapper(domain.OrderLine, order_lines)