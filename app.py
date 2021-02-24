from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print("Form Received!")
        # TODO: write code...
        
        # if file not have information redirect user to homepage
        if "file" not in request.files:
            return redirect(request.url)
        
        # if someone submit a blank file
        # if file not imported and button got clicked
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        
        if file:
            recognizer = sr.Recognizer()
            audio_file = sr.AudioFile(file)
            with audio_file as source:
                data = recognizer.record(source)
                
            text = recognizer.recognize_google(data, key=None)
            print(text)
            
    return render_template('index.html')
    
@app.route("/about")
def about():
    return "about page"
    
@app.route("/contact")
def contact():
    return "contact page"

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
