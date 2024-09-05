import os
from typing import List, Union

import elasticsearch
from elasticsearch import Elasticsearch


class MyElastic:
    def __init__(self, index: str = "posts"):
        connection_str = os.getenv("SERVER_ELASTIC_CONNECTION", None)
        self.__connection = Elasticsearch(connection_str)
        self.__index = index

    def search_by_id(self, id: int) -> Union[list, None]:
        result = self.__connection.search(index=self.__index, body={
            "size": 1,
            "query": {
                "match": {
                    'id': id
                }
            }
        })["hits"]["hits"]
        if len(result) == 0:
            return None
        return result

    def delete_by_id(self, id: int) -> bool:
        try:
            self.__connection.delete(index=self.__index, doc_type="record", id=id)
            return True
        except elasticsearch.exceptions:
            return False

    def search_by_text(self, text: str) -> List[dict]:
        result = self.__connection.search(index=self.__index, body={
            "size": 20,
            "query": {
                "match": {
                    'text': text
                }
            }
        })
        return [item["_source"]["id"] for item in result["hits"]["hits"]]