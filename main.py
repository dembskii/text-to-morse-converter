from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from forms import PlainTextForm, MorseTextForm
from alphabets import default_alphabet, morse_alphabet
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
Bootstrap(app)



@app.route('/',methods=["GET","POST"])
def home():
    # CREATE FORMS
    form_plain = PlainTextForm()
    form_morse = MorseTextForm()


    # TRANSLATION AND VALIDATION LOGIC
    translated=""
    if form_plain.validate_on_submit():
        to_translate = form_plain.text_plain.data
        to_translate = to_translate.upper()

        for letter in to_translate:
            translated_letter = morse_alphabet[default_alphabet.index(letter)] + " "
            translated += translated_letter

        translated = translated[:-1]
        form_morse = MorseTextForm(
            text_morse= translated
        )
        return render_template('index.html', form_plain=form_plain, form_morse=form_morse)

    if form_morse.validate_on_submit():
        to_translate = form_morse.text_morse.data
        to_translate = to_translate.upper().split(" ")
        
        for letter in to_translate:
            translated_letter = default_alphabet[morse_alphabet.index(letter)]
            translated += translated_letter
        
        form_plain = PlainTextForm(
            text_plain=translated
        )
        return render_template('index.html', form_plain=form_plain, form_morse=form_morse)

    return render_template('index.html', form_plain=form_plain, form_morse=form_morse)
    

@app.route('/table')
def table():
    return render_template("table.html",morse_alphabet=morse_alphabet,default_alphabet=default_alphabet)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)