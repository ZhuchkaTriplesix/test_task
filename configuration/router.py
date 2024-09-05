from dataclasses import dataclass

from api.search.handlers import search_router


@dataclass(frozen=True)
class Router:
    routers = [
        (search_router, "/api/user", ["user"])
    ]
