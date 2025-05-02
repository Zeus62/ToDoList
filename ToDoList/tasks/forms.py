from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class TaskForm(FlaskForm):
    content = StringField('New Task', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Add Task')