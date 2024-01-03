from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, Boolean, DateTime
from app import db, app
from sqlalchemy.orm import relationship
from flask_login import UserMixin
import enum
from datetime import datetime


class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False, unique=False)
    avatar = Column(String(100), default='https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    receipts = relationship('Receipt', backref='user', lazy=True)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    receipt_details = relationship('ReceiptDetails', backref='product', lazy=True)

    def __str__(self):
        return self.name


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())


class Receipt(BaseModel):
    user_id = Column(Integer, ForeignKey(User.id), nullable=True)
    receipt_details = relationship('ReceiptDetails', backref='receipt', lazy=True)


class ReceiptDetails(BaseModel):
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        import hashlib

        u = User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                 user_role=UserRoleEnum.ADMIN)
        db.session.add(u)
        db.session.commit()

        c1 = Category(name='Mobile')
        c2 = Category(name='Tablet')

        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()

        p1 = Product(name='iPhone 13', price=20000000, category_id=1,
                     image='https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg')
        p2 = Product(name='iPhone 14', price=30000000, category_id=1,
                     image='https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg')
        p3 = Product(name='iPad Pro 2023', price=35000000, category_id=2,
                     image='https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg')
        p4 = Product(name='SamSung Salaxy S72', price=15000000, category_id=1,
                     image='https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg')
        p5 = Product(name='Galaxy Tab S9', price=27000000, category_id=2,
                     image='https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg')
        p6 = Product(name='iPhone 11', price=10000000, category_id=1,
                     image='https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg')
        p7 = Product(name='Note 23', price=10000000, category_id=1,
                     image='https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg')
        db.session.add_all([p1, p2, p3, p4, p5, p6, p7])
        db.session.commit()
