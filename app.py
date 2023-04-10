import logging
from Transcribe import transcribe
import speech_recognition as sr
from flask import Flask, render_template, request, redirect, url_for

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    if request.method == 'POST':
        logger.info("Received POST request")
        language = request.form['language']
        file = request.files['audiofile']

        file.save(file.filename)

        text = transcribe(file.filename, language=language)
    return render_template('index.html', text=text)


if __name__ == '__main__':
    app.run(debug=True)
