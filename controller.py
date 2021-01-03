from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from validator import Validator

app = Flask(__name__,instance_relative_config=True)
app.config.from_object('config.DevConfig')
upload_folder = app.config["UPLOAD_FOLDER"]
validator = Validator()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate")
def generate():
    return render_template("generate.html")

@app.route("/upload", methods = ["POST"])
def upload():
    uploaded_file = request.files["file"]
    UI_msg,file_detected = validator.validate_xml(uploaded_file.filename)
    if file_detected:
        return "File DETECTED"
    else:
        return render_template("generate.html", msg = UI_msg)

if __name__ == "__main__":
    app.run()
