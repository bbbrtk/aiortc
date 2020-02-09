from flask import Flask, request
import base64
import os

app = Flask(__name__)
@app.route('/filter', methods=['POST'])
def result():
    ip = request.environ['REMOTE_ADDR']
    img = request.form['image'].encode('utf-8')
    benchmark = request.form['benchmark']
    color = request.form['color']

    server_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_name = os.path.join(server_dir, "images", f"{ip.replace('.','-')}.jpg")
    txt_name = os.path.join(server_dir, "txt", f"{ip.replace('.','-')}.txt")

    print(f"{img_name} - {benchmark} - {color}")
    
    with open(img_name, "wb") as fh:
        fh.write(base64.decodestring(img))

    with open(txt_name, "w") as fh2:
        fh2.write(f"{str(benchmark)}\n{str(color)}")

    return f"received and stored {img_name}" # response to request
