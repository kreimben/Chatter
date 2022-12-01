from sqlalchemy import Integer, Column, String, BLOB
from sqlalchemy.orm import relationship, Session

from server.database import Base, get_db


class File(Base):
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True, autoincrement=True)

    file_name = Column(String(100))
    file_extension = Column(String(100))
    file_content = Column(BLOB)

    chat = relationship('Chat', back_populates='file', cascade='all, delete-orphan')


db: Session = get_db()


def create_file(file_name: str, file_extension: str, file_content: bytes):
    file_obj = File(file_name=file_name, file_extension=file_extension, file_content=file_content)
    db.add(file_obj)
    db.commit()
    db.refresh(file_obj)


def get_file(file_name: str, file_extension: str) -> [File]:
    return db.query(File).filter(File.file_name == file_name, File.file_extension == file_extension).all()


def get_file_by_id(file_id: int) -> File:
    return db.query(File).filter(File.id == file_id).first()

# I will not implement update and delete feature.
