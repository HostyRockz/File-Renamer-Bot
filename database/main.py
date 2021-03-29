from sqlalchemy import Column, String, UnicodeText, Integer
from __init__ import BASE, SESSION


class Stark(BASE):
    __tablename__ = "AccountGenerator"
    user_id = Column(Integer, primary_key=True)
    usage_limit = Column(Integer, default=0)
    user_limit = Column(Integer, default=0)

    def __init__(self, user_id, usage_limit, user_limit):
        self.user_id = user_id
        self.usage_limit = usage_limit
        self.user_limit = user_limit


Stark.__table__.create(checkfirst=True)
