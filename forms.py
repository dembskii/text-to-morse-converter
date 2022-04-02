from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class PlainText(FlaskForm):
    text_plain = StringField("Plain Text",validators=[DataRequired()],widget=TextArea())
    submit_plain = SubmitField("Convert to morse code")


class MorseText(FlaskForm):
    text_morse = StringField("Morse Text",validators=[DataRequired()],widget=TextArea())
    submit_morse = SubmitField("Convert to plain text")
