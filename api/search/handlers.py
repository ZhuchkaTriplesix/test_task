from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from api.search.models import *
from services.postgres.session import get_db


search_router = APIRouter()


@search_router.get("/posts/search")
def search_post(text: str, db: AsyncSession = Depends(get_db)):
    return {"result": crud.search_post_by_text(db=db, search_text=text)}


@search_post.delete("/posts/delete")
def remove_post(remove_item: PostRemoveItem, db: AsyncSession = Depends(get_db)):
    return {"result": crud.delete_by_id(db=db, id=remove_item.id)}
