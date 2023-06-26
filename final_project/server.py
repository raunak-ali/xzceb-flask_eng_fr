from machinetranslation import translator
from machinetranslation import englishToFrench
from machinetranslation import frenchToEnglish
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")



@app.route("/englishToFrench")
def englishToFrench():
    
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_text = request.form[textToTranslate]
    french_text = englishToFrench(english_text)

    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_text = request.form[textToTranslate]
    english_text = frenchToEnglish(french_text)
    return english_text
    

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    # Write the code to render template
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
