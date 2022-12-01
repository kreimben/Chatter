from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Session

from server.database import Base, get_db


class Chat(Base):
    __tablename__ = 'chat'

    id = Column(Integer, primary_key=True, autoincrement=True)

    sender_name = Column(String(100))
    target_name = Column(String(100))

    # One of things are exists. `message` or `file`.
    message = Column(String(4000), nullable=True)
    file_id = Column(Integer, ForeignKey('file.id'), nullable=True)

    file = relationship('File', back_populates='chats')

    def __repr__(self):
        return f'{self.message if self.message is not None else self.file_id} ({self.target_name} sent to {self.sender_name})'


db: Session = get_db()


def create_chat(sender_name: str, target_name: str, message: str | None = None, file_id: int | None = None):
    chat = Chat(
        sender_name=sender_name,
        target_name=target_name,
        message=message,
        file_id=file_id
    )
    db.add(chat)
    db.commit()
    db.refresh(chat)


def get_chats(target_name: str, sender_name: str | None = None) -> [Chat]:
    if sender_name is not None:
        return db.query(Chat).filter(Chat.sender_name == sender_name, Chat.target_name == target_name).all()
    else:
        return db.query(Chat).filter(Chat.sender_name == sender_name).all()

# I will not implement update and delete feature.
