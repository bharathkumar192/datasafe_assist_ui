from flask import Flask, request, jsonify, Response
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
import time 

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = '/'
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@cross_origin()
@app.route('/api/file', methods=['POST'])
def upload_file():
    return jsonify(uploaded_files="success"), 200

@cross_origin()
@app.route('/api/chat/stream', methods=['POST'])
def chat_stream():
    data = request.json
    time.sleep(3)
    text = ''' The Null Value masking format is a simple yet effective way to replace column data with NULL. This format is suitable when you want to remove sensitive information from your dataset without altering its structure or integrity.

You should consider using the Null Value masking format in situations where:

1. **Data removal is necessary**: When you need to completely eliminate sensitive information from your dataset, such as removing personally identifiable information (PII) like names, addresses, or social security numbers.
2. **NULL values are acceptable**: In cases where NULL values are allowed in your target system or application, this format is a good choice. For instance, if you're migrating data to a new system that accepts NULL values, the Null Value masking format can ensure seamless integration.
3. **Data reconstruction is not required**: Since the Null Value masking format does not support reversible masking, you shouldn't use it if you need to recover the original data at a later time.'''
    
    return jsonify(message=text,mimetype='text/plain'), 200

# def generate():
#     yield "Generating the response stream...\n"
#     time.sleep(3)  # Simulate delay
#     text = ''' The Null Value masking format is a simple yet effective way to replace column data with NULL. This format is suitable when you want to remove sensitive information from your dataset without altering its structure or integrity.

# You should consider using the Null Value masking format in situations where:

# 1. **Data removal is necessary**: When you need to completely eliminate sensitive information from your dataset, such as removing personally identifiable information (PII) like names, addresses, or social security numbers.
# 2. **NULL values are acceptable**: In cases where NULL values are allowed in your target system or application, this format is a good choice. For instance, if you're migrating data to a new system that accepts NULL values, the Null Value masking format can ensure seamless integration.
# 3. **Data reconstruction is not required**: Since the Null Value masking format does not support reversible masking, you shouldn't use it if you need to recover the original data at a later time.
# '''
#     yield text  # Send a part of the response

# @cross_origin()
# @app.route('/api/chat/stream', methods=['POST'])
# def chat_stream():
#     return Response(generate(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
