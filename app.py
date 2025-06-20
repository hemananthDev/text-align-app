from flask import Flask, render_template, request, send_file
import os
from aligner import align_text  # <-- import from new module

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALIGNED_FOLDER = 'aligned'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ALIGNED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        input_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(input_path)

        with open(input_path, 'r') as f:
            content = f.read()

        # Use the external align function
        aligned_text = align_text(content)

        aligned_filename = f'aligned_{uploaded_file.filename}'
        output_path = os.path.join(ALIGNED_FOLDER, aligned_filename)
        with open(output_path, 'w') as f:
            f.write(aligned_text)

        return send_file(output_path, as_attachment=True)

    return "No file uploaded", 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
