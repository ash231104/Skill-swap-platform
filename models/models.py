from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100))
    skills_offered = db.Column(db.String(300))
    skills_wanted = db.Column(db.String(300))
    availability = db.Column(db.String(100))
    is_private = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)

class SwapRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    skill = db.Column(db.String(100))
    status = db.Column(db.String(20), default='Pending')

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)

class AdminLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

--- forms/forms.py --- # type: ignore
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ProfileForm(FlaskForm):
    location = StringField('Location')
    skills_offered = TextAreaField('Skills Offered', validators=[DataRequired()])
    skills_wanted = TextAreaField('Skills Wanted', validators=[DataRequired()])
    availability = StringField('Availability')
    is_private = BooleanField('Private Profile')
    submit = SubmitField('Save Changes')

class SwapRequestForm(FlaskForm):
    skill = StringField('Skill', validators=[DataRequired()])
    submit = SubmitField('Send Request')

class FeedbackForm(FlaskForm):
    rating = SelectField('Rating', choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')], coerce=int)
    comment = TextAreaField('Comment')
    submit = SubmitField('Submit Feedback')

class AnnouncementForm(FlaskForm):
    message = TextAreaField('Announcement Message', validators=[DataRequired()])
    submit = SubmitField('Send Announcement')