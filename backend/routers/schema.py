import strawberry

from typing import List
from backend.routers.item import get_items
from backend.routers.util import SQLAlchemySession
from backend.schemas.item import Item


@strawberry.type
class Query:
    item: List[Item] = strawberry.field(resolver=get_items)


schema = strawberry.Schema(Query, extensions=[SQLAlchemySession])