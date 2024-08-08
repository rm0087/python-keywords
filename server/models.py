from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db


class Type(db.Model, SerializerMixin):

    __tablename__='type_table'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)

    
    keywords = db.relationship('Keyword', back_populates='type')

    # serialize_rules = ('-keyword.type',)

class Keyword(db.Model, SerializerMixin):

    __tablename__='keyword_table'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('type_table.id'))

    type = db.relationship('Type', back_populates='keywords')

    # serialize_rules = ('-type.keywords',)

