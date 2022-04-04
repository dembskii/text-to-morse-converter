from flask import Flask,render_template,redirect,url_for, flash
from flask_bootstrap import Bootstrap
from forms import PlainTextForm, MorseTextForm
from alphabets import default_alphabet, morse_alphabet
import os
from flask_sqlalchemy import SQLAlchemy

# create app
app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL","sqlite:///entry.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


Bootstrap(app)
db = SQLAlchemy(app)


class Entry(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    entry = db.Column(db.String)

db.create_all()

# Home route
@app.route('/',methods=["GET","POST"])
def home():
    # CREATE FORMS
    form_plain = PlainTextForm()
    form_morse = MorseTextForm()


    # TRANSLATION AND VALIDATION LOGIC
    translated=""
    """
        if form.validate_on_submit():
        can not be used because it validates both forms when both are empty
    """
    if form_plain.submit_plain.data and form_plain.validate():
        to_translate = form_plain.text_plain.data
        to_translate = to_translate.upper()
        

        for letter in to_translate:
            if letter not in default_alphabet:
                flash(f'"{letter}" can not be translated.')
                return redirect(url_for('home'))
            translated_letter = morse_alphabet[default_alphabet.index(letter)] + " "
            translated += translated_letter

        translated = translated[:-1]
        form_morse = MorseTextForm(
            text_morse= translated
        )

        #New entry create
        entry = Entry(
            entry=to_translate
        )
        #Add entry to db
        db.session.add(entry)
        db.session.commit()

        return render_template('index.html', form_plain=form_plain, form_morse=form_morse)

    if form_morse.submit_morse.data and form_morse.validate():
        to_translate = form_morse.text_morse.data
        to_translate = to_translate.upper().split(" ")
        
        for letter in to_translate:
            if letter not in morse_alphabet:
                flash(f'"{letter}" can not be translated.')
                return redirect(url_for('home'))
            translated_letter = default_alphabet[morse_alphabet.index(letter)]
            translated += translated_letter
        
        form_plain = PlainTextForm(
            text_plain=translated
        )
        return render_template('index.html', form_plain=form_plain, form_morse=form_morse)

    return render_template('index.html', form_plain=form_plain, form_morse=form_morse)
    

# Display symbols comparison
@app.route('/table')
def table():
    return render_template("table.html",morse_alphabet=morse_alphabet,default_alphabet=default_alphabet)


@app.route('/entry/<secret_stuff>')
def entry(secret_stuff):
    if secret_stuff == os.environ.get("SECRET_STUFF"):
        
        data = Entry.query.all()
        return render_template("entry.html",data=data)
    return '<img style="display: block; margin-left: auto; margin-right: auto;width: 60%;" src="https://c.tenor.com/DDhyzgQ23a0AAAAM/star-trek-james-t-kirk.gif" alt="Not this time">'
# Run app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)