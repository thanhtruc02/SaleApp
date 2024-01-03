from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = '*%*&#&)(hfiUYGYII*&(^(^)^)GgUGIiugifg'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 4

import cloudinary

cloudinary.config(
    cloud_name="duxbitj2i",
    api_key="596724224287136",
    api_secret="hSYGJmknTcF6SD2IP7cbxboBBM4"
)

db = SQLAlchemy(app=app)
login = LoginManager(app=app)
