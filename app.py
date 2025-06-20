from flask import Flask, request, send_file, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALIGNED_FOLDER = 'aligned'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ALIGNED_FOLDER, exist_ok=True)

def align_text(text):
    lines = text.strip().split('\n')
    max_length = max(len(line.strip()) for line in lines)
    aligned_lines = [line.strip().ljust(max_length) for line in lines]
    return '\n'.join(aligned_lines)

# 🆕 HTML upload form route
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Existing file upload API
@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename.endswith('.txt'):
        input_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        output_path = os.path.join(ALIGNED_FOLDER, 'aligned_' + uploaded_file.filename)

        uploaded_file.save(input_path)

        with open(input_path, 'r') as f:
            original_text = f.read()
        aligned_text = align_text(original_text)

        with open(output_path, 'w') as f:
            f.write(aligned_text)

        return send_file(output_path, as_attachment=True)
    else:
        return 'Only .txt files are allowed.', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
