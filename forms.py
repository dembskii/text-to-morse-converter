from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class PlainText(FlaskForm):
    text_plain = StringField("Plain Text",validators=[DataRequired()])
    submit_plain = SubmitField("Convert to plain text")


class MorseText(FlaskForm):
    text_morse = StringField("Morse Text",validators=[DataRequired()])
    submit_morse = SubmitField("Convert to plain text")
