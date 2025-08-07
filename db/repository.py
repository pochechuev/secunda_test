class SQLAlchemyRepository:

    def __init__(self, session):
        self.session = session

    def __repr__(self) -> str:
        return f"Repo: {self.__class__.__name__}"
