from flask import render_template
from ToDoList.main import main

@main.route('/')
def index():
    return render_template('index.html')