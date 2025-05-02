from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a5f0a7c6be7c4f6e8d15fa457e2c4dd9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db = SQLAlchemy()

db.init_app(app)

from ToDoList.users import users
from ToDoList.tasks import tasks
from ToDoList.main import main

app.register_blueprint(users)
app.register_blueprint(tasks)
app.register_blueprint(main)

with app.app_context():
    db.create_all()


