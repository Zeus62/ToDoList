from . import tasks
from flask import render_template, redirect, url_for, session, abort
from .forms import TaskForm
from models import db, User, Task

@tasks.route('/dashboard')
def dashboard():
    user = User.query.get(session['user_id'])
    tasks = Task.query.filter_by(user_id=user.id).order_by(Task.date_created.desc()).all()
    form = TaskForm()
    return render_template('dashboard.html', username=user.username, tasks=tasks, form=form)


@tasks.route('/add_task', methods=['POST'])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(content=form.content.data, user_id=session['user_id'])
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('tasks.dashboard'))


@tasks.route('/complete_task/<int:id>', methods=['POST'])
def complete_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != session['user_id']:
        abort(403)  
    task.completed = True
    db.session.commit()
    return redirect(url_for('tasks.dashboard'))

@tasks.route('/delete_task/<int:id>', methods=['POST'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != session['user_id']:
        abort(403)  
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks.dashboard'))

@tasks.route('/reopen_task/<int:id>', methods=['POST'])
def reopen_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != session['user_id']:
        abort(403)  
    task.completed = False
    db.session.commit()
    return redirect(url_for('tasks.dashboard'))