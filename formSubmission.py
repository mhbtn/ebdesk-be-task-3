from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import  ValidationError, DataRequired

class FormSubmission(Form):
    channel_id = StringField(name="channel_id", validators=[DataRequired()])
    title = StringField(name="title", validators=[DataRequired()])
    channel_name = StringField(name="channel_name", validators=[DataRequired()])
    publish_date = StringField(name="publish_date", validators=[DataRequired()])