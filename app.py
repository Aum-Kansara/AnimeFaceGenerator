from flask import Flask,send_file
from generator import generate_faces

app=Flask(__name__)


@app.route("/")
def index():
    generate_faces()
    return send_file('static/generated_faces.png',mimetype='image/gif')

if __name__=="__main__":
    app.run(debug=True)