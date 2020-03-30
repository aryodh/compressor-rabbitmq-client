import zipfile, requests, random, string
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    uniqueId = randomId()
    return render_template('index.html', uniqueId = uniqueId)

def randomId():
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(10))

@app.route('/upload/', methods=['POST'])
def upload():
    try:
        uniqueId = request.args.to_dict().get("uniqueId")
        temp = request.files.get('file')
        url = "http://152.118.148.95:20644/compress"
        files = {"file": (temp.filename, temp.stream, temp.mimetype)}
    except:
        print("failed")
    r = requests.post(url, files=files, headers={"X-ROUTING-KEY":uniqueId})
        # isthisFile.save("./"+isthisFile.filename)
    return "success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20643)


