from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['GET','POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    image = Image.open(io.BytesIO(file.read()))
    
    text = pytesseract.image_to_string(image)
    

    if len(text) > 0:
        return jsonify({'text': text})
    else:
        return jsonify({'text': 'abhishek'})

if __name__ == '__main__':
    app.run(debug=True)
