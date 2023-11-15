from app.models import Category, Product, User
from app import app
import hashlib


def load_categories():
    return Category.query.all()


def load_products(kw=None, cate_id=None, page=None):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    if page:
        pass

    return products.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)
