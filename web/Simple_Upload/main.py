from flask import Flask, request, send_file, render_template_string, redirect, url_for, session
import os
import time

app = Flask(__name__)
app.secret_key = 'supersecretkey'

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'txt'}
MAX_FILE_SIZE = 10 * 1024

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template()


@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        session['message'] = 'No file part'
        return redirect(url_for('success'))

    file = request.files['file']
    if file.filename == '':
        session['message'] = 'No selected file'
        return redirect(url_for('success'))

    if file and allowed_file(file.filename):
        file_content = file.read()
        if len(file_content) > MAX_FILE_SIZE:
            session['message'] = 'File too large! Max size is 10KB'
            return redirect(url_for('success'))

        original_name, file_extension = os.path.splitext(file.filename)
        timestamp = int(time.time())
        new_filename = f"{original_name}_{timestamp}{file_extension}"
        file_path = os.path.join(UPLOAD_FOLDER, new_filename)

        with open(file_path, 'wb') as f:
            f.write(file_content)

        session['message'] = 'File uploaded successfully'
        session['file_url'] = request.host_url + f'download?file=uploads/{new_filename}'
        return redirect(url_for('success'))
    else:
        session['message'] = 'Invalid file type! Allowed types: ' + ', '.join(ALLOWED_EXTENSIONS)
        return redirect(url_for('success'))

@app.route('/success')
def success():
    message = session.pop('message', '')
    file_url = session.pop('file_url', None)
    return render_template(message=message, file_url=file_url)

@app.route('/download')
def download_file():
    filename = request.args.get('file')
    if not filename:
        return "No file specified", 400
    file_path = os.path.join(app.root_path, filename)
    print(file_path)
    if not os.path.exists(file_path):
        return "File not found", 404
    return send_file(file_path)

def render_template(message='', file_url=None):
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>File Upload</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f5f5f5;
                }
                .container {
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                .header {
                    text-align: center;
                    margin-bottom: 20px;
                }
                .upload-form {
                    display: flex;
                    flex-direction: column;
                    gap: 15px;
                }
                .file-input {
                    border: 2px dashed #ccc;
                    padding: 20px;
                    text-align: center;
                    cursor: pointer;
                }
                .submit-btn {
                    background: #4CAF50;
                    color: white;
                    padding: 10px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                .submit-btn:hover {
                    background: #45a049;
                }
                .message {
                    padding: 10px;
                    margin-top: 20px;
                    border-radius: 4px;
                }
                .success {
                    background: #dff0d8;
                    border: 1px solid #d0e9c6;
                    color: #3c763d;
                }
                .error {
                    background: #f2dede;
                    border: 1px solid #ebccd1;
                    color: #a94442;
                }
                .requirements {
                    background: #f8f9fa;
                    padding: 15px;
                    border-radius: 4px;
                    margin-top: 20px;
                }
                .requirements ul {
                    margin: 0;
                    padding-left: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>File Upload System</h1>
                </div>
                
                <form class="upload-form" method="post" action="/api/upload" enctype="multipart/form-data">
                    <div class="file-input">
                        <input type="file" name="file" id="file">
                    </div>
                    <button type="submit" class="submit-btn">Upload File</button>
                </form>
                
                {% if message %}
                <div class="message {% if 'successfully' in message %}success{% else %}error{% endif %}">
                    {{ message }}
                    {% if file_url %}
                    <div style="margin-top: 10px;">
                        File link: <a href="{{ file_url }}" target="_blank">{{ file_url }}</a>
                    </div>
                    {% endif %}
                </div>
                {% endif %}
                
                <div class="requirements">
                    <h3>Requirements:</h3>
                    <ul>
                        <li>Maximum file size: 10KB</li>
                        <li>Allowed file types: .png, .jpg, .jpeg, .gif, .txt</li>
                    </ul>
                </div>
            </div>
        </body>
        </html>
    ''', message=message, file_url=file_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5312)