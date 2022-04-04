from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class PlainTextForm(FlaskForm):
    text_plain = StringField("Plain Text",validators=[DataRequired(message="This field has to be filled.")],widget=TextArea())
    submit_plain = SubmitField("Convert to morse code")


class MorseTextForm(FlaskForm):
    text_morse = StringField("Morse Code",validators=[DataRequired(message="This field has to be filled.")],widget=TextArea())
    submit_morse = SubmitField("Convert to plain text")
