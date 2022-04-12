# Text to Morse Converter

Hi! It's [my](https://github.com/dembskii) first public project on github. This website is hosted on heroku with gunicorn. I created this converter in python using Flask Framework and Bootstrap.
**https://text-to-morse-converter.herokuapp.com/**

## Background 
### What is Morse Code?
**Morse code** is a method used in telecommunication. Text characters are encoded as sequences of different signal durations. This is split into _dots_ and _dashes_. The two signal durations are encoded into different combinations of _dots_ and _dashes_, which in turn forms different letters or numbers. The Morse code was invented in the 1830s by [Samuel Morse](https://en.wikipedia.org/wiki/Samuel_Morse). The original Morse code only encoded numerals, which was not very useful. It was then refined to included letters and punctuation by [Alfred Vail](https://en.wikipedia.org/wiki/Alfred_Vail). Morse code has since then been publicized into what we know now as **International Morse Code**, which encodes the 26 letters of the alphabet, numbers 0-9, and a list of simple punctuation.

The benefit of Morse code lies in the flexibility of its usage. Morse code can be used with any signal as a medium, ranging from sounds,light sources to tapping. Some internationally known signals, such as 'SOS', can be conveyed through morse code. While the need for morse code has reduced due to advances in communication technology, morse code remains relevant and can be used as discreet means of communication, or even by those incapbale of speech.

![International_Morse_Code svg](https://user-images.githubusercontent.com/56427665/163046633-b5391e8e-8f28-457f-a540-fd03cf55a8eb.png)

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
