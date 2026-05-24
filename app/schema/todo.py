from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select, col
from datetime import datetime

class TodoBase(SQLModel):
    task : str
    is_done: bool = False
    


class ToDoItem(TodoBase):
    pass

class ToDo(TodoBase, table = True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)





# def create_heros():
#     hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
#     hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
#     hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
#     hero_4 = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
#     hero_5 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
#     hero_6 = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
#     hero_7 = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)

#     with Session(engine) as session:
#         session.add(hero_1)
#         session.add(hero_2)
#         session.add(hero_3)
#         session.add(hero_4)
#         session.add(hero_5)
#         session.add(hero_6)
#         session.add(hero_7)

#         session.commit()
#         # print("After committing the session")
#         # print("Hero 1:", hero_1)
#         # print("Hero 2:", hero_2)
#         # print("Hero 3:", hero_3)

#         # print("After committing the session, show IDs")
#         # print("Hero 1 ID:", hero_1.id)
#         # print("Hero 2 ID:", hero_2.id)
#         # print("Hero 3 ID:", hero_3.id)

#         # print("After committing the session, show names")
#         # print("Hero 1 name:", hero_1.name)
#         # print("Hero 2 name:", hero_2.name)
#         # print("Hero 3 name:", hero_3.name)


# #def select_heroes():
#     with Session(engine) as session:
#         #statement = select(Hero).where(col(Hero.name) == "Deadpond")
#         statement = select(Hero).limit(3)
#         results = session.exec(statement)
#         heroes = results.all()
#         print(heroes)


# #def update_heroes():
#     with Session(engine) as session:
#         statement = select(Hero).where(Hero.name == "Spider-Boy")
#         results = session.exec(statement)
#         hero = results.one()
#         print("Hero:", hero)
#         hero.age = 16
#         hero.name = "Spider-Youngster"
#         session.add(hero)
#         session.commit()
        
#         session.refresh(hero)
#         print("Updated Hero:", hero)

# #def delete_heroes():
#     with Session(engine) as session:
#         statement = select(Hero).where(Hero.name == "Spider-Youngster")
#         results = session.exec(statement)
#         hero = results.one()
#         print("Hero: ", hero)
#         session.delete(hero)
#         session.commit()

#         print("Deleted hero:", hero)

#         statement = select(Hero).where(Hero.name == "Spider-Youngster")
#         results = session.exec(statement)
#         hero = results.first()

#         if hero is None:
#             print("There's no hero named Spider-Youngster")
        
# def main():
#     create_db_and_tables()
#     # create_heros()
#     # select_heroes()
#     # update_heroes()
#     # delete_heroes()
    

# if __name__ == "__main__":
#     main()