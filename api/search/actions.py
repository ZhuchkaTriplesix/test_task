from sqlalchemy.orm import Session

import services.postgres.models as models
from services.elasticsearch.elastic import MyElastic

my_elastic = MyElastic()


def search_post_by_text(db: Session, search_text: str):
    ids_list = my_elastic.search_by_text(search_text)
    result = db.query(models.Post) \
        .filter(models.Post.id.in_(ids_list)) \
        .order_by(models.Post.created_date.desc()) \
        .all()
    return result


def delete_by_id(db: Session, id: int) -> bool:
    delete_item = my_elastic.search_by_id(id)
    if delete_item is not None:
        elastic_result = my_elastic.delete_by_id(delete_item[0]["_id"])
        if elastic_result:
            db_result = bool(db.query(models.Post).filter(models.Post.id == id).delete())
            db.commit()
            return db_result
        return elastic_result
    return False
