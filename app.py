from flask import Flask,render_template,send_file
from generator import generate_faces

app=Flask(__name__)


@app.route("/")
def index():
    return send_file('generates_faces.png',mimetype='image/gif')

if __name__=="__main__":
    app.run(debug=True)