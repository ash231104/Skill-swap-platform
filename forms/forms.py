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
