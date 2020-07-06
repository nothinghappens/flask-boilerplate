import datetime as dt

from marshmallow import Schema, fields, post_dump
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import Category, Tag, Article


class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        exclude = ['created_at']

    tags = fields.Nested(lambda: TagSchema(exclude=['category']), many=True)


class TagSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tag
        include_fk = True
        exclude = ['created_at', 'category_id']

    category = fields.Nested(CategorySchema(exclude=['tags']))


class ArticleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Article

    tags = fields.Nested(TagSchema, many=True)
