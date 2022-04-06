# Text to Morse Converter

Hi! It's [my](https://github.com/dembskii) first public project on github. This website is hosted on heroku with gunicorn. I created this converter in python using Flask Framework and Bootstrap.
**https://text-to-morse-converter.herokuapp.com/**


# How is the translation going?
There is two lists that contain alphabet and morse translated alphabet, both in same order so It is pretty simple to translate.

**Flowchart**
```mermaid
flowchart TD
	A[Pass any text to one of two fields] --> B[Loop for each letter in passed text];
	B--> F{If last letter}
	F --> No-->C[Find index of letter];
	C --> D[Match index in another alphabet];
	D --> E[Add translated letter to text that has to be returned];
	F --> Yes --> G[Return translated text]
	E --> F
