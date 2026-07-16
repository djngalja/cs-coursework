from datasource.db.connection import engine
from datasource.model.current_game_ds import CurrentGameDs, GameBoardDs, Base # type: ignore
from datasource.model.user_ds import UserDs # type: ignore

def create_tables() -> None:
    Base.metadata.create_all(engine)
    print("Tables created")

if __name__ == "__main__":
    create_tables()