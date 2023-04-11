import os
import logging
from pydub import AudioSegment
import speech_recognition as sr

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def transcribe(audiofile, language='en-US'):
    f = ""
    logger.info("Grab the %s", audiofile)
    logger.info("Grab the %s", type(audiofile))
    if audiofile.endswith('.ogg'):
        f = audiofile.replace('.ogg', '.wav')
        convert = AudioSegment.from_file(audiofile)
        convert.export(f, format='wav')
    elif audiofile.endswith('.mp3'):
        f = audiofile.replace('.mp3', '.wav')
        convert = AudioSegment.from_file(audiofile)
        convert.export(f, format='wav')
    else:
        logger.info("File %s not supported.", audiofile)

    logger.info("Transcribing %s", f)

    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(f)
    with audio_file as source:
        data = recognizer.record(source)

    text = recognizer.recognize_google(data, language=language)

    logger.info("Transcription: %s", text)

    os.remove(audiofile)
    os.remove(f)

    return text
