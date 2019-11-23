from src.query import Query


class QueryBuilder:
    @staticmethod
    def new_query():
        return QueryBuilder()

    def build(self):
        return Query()
