from sqlmodel import Field, Session, Relationship, SQLModel, create_engine, select


class ContactCategory(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    contacts: list["Contact"] = Relationship(back_populates="category")


class Contact(SQLModel, table=True):
    id: int | None = Field(
        default=None, primary_key=True
    )  # id will be auto-generated by the database
    first_name: str
    last_name: str | None
    category_id: int | None = Field(default=None, foreign_key="contactcategory.id")
    category: ContactCategory | None = Relationship(back_populates="contacts")


sqlite_file_name = "rolodex.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_contacts():
    with Session(engine) as session:
        family = ContactCategory(name="Family")
        friends = ContactCategory(name="Friends")
        jane = Contact(first_name="Jane", last_name="Doe", category=friends)
        john = Contact(first_name="John", last_name="Smith", category=family)
        gene = Contact(first_name="Gene", last_name="Good", category=friends)
        session.add(jane)
        session.add(john)
        session.add(gene)
        session.commit()


def select_contacts():
    with Session(engine) as session:
        print("=== Select all contacts ===")
        contacts = session.exec(select(Contact)).all()
        print(contacts)
        print("=== Select where ===")
        jane = session.exec(select(Contact).where(Contact.first_name == "Jane")).first()
        print("Jane: ", jane)
        print("=== Select join ===")
        sql = select(Contact).join(ContactCategory).where(ContactCategory.name == "Friends")
        contacts = session.exec(sql).all()
        print(contacts)
        print("*********")
        print(contacts[0].category)


if __name__ == "__main__":
    create_db_and_tables()
    create_contacts()
    select_contacts()
