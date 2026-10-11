from flask import Flask, request, jsonify
from flask_cors import CORS
from services.identifyExtension import identifyExtension
from services.EXIFExtract.ExtractController import extractController
app = Flask(__name__)

CORS(app)
@app.post("/login")
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
@app.get("/upload")
def upload():
    query = request.args.get("name")
    return query
@app.post("/checktype")
def handleUpload():
    file = request.files["file"]
    name = file.filename
    type = identifyExtension(file)
    result = {"name":name,"type":type}
    return jsonify(result)
@app.post("/checkdetail")
def handleCheckDetail():
    file = request.files["file"]
    fileName = file.filename
    result = extractController(file)
    return jsonify(result)  
@app.get("/")
def home(): 
    return "Home"
if __name__ == "__main__":
    app.run()