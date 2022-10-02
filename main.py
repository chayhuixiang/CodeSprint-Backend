from flask import Flask, request, jsonify
from detect import detect
import base64
import os
import glob
import shutil


app = Flask(__name__)

@app.route("/", methods=["GET"])
def health_check():
    return "Health Check"

@app.route('/scoreimgs', methods=['POST'])
def get_score():                    
    img = request.json['image']
    #img = base64.b64encode(open("./images.jpeg", "rb").read())
    with open("./data/images/img.png", "wb") as fh:
        fh.write(base64.b64decode((img)))
    results = detect()
    
    upload = glob.glob('./data/images/*')
    for f in upload:
        os.remove(f)
    shutil.rmtree("./runs/detect", ignore_errors=False)
    print("------")
    print(results)
    return results
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

