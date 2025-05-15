from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy_serializer import SerializerMixin

from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


class Base(DeclarativeBase):
    pass


class User(Base, SerializerMixin):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(), nullable=False)
    balance = Column(Integer(), default=0)

    inventory = relationship("Inventory", back_populates="author", cascade="all, delete")


class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    item_id = Column(String(), ForeignKey('items.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))

    author = relationship("User", back_populates="inventory")


class Items(Base, SerializerMixin):
    __tablename__ = "items"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    cost = Column(Integer(), nullable=False)
    rname = Column(String(), nullable=False)
    rarity = Column(String(), nullable=False)
    color = Column(String(), nullable=False)
    w = Column(Integer(), nullable=False)


class Community(Base):
    __tablename__ = "community"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    name = Column(String(50), nullable=False)
    rname = Column(String(), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    rarity = Column(String(), nullable=False)
    cost = Column(Integer(), nullable=False)
    history = Column(String(), nullable=False)
    history_user = Column(String(), nullable=False)


engine = create_engine("sqlite:///database/db.db")
Base.metadata.create_all(engine)
factory = sessionmaker(bind=engine)
