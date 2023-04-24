from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads' # 上传文件保存的目录
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 上传文件大小的限制为 16MB
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'} # 允许上传的文件类型

def allowed_file(filename):
    """判断上传的文件类型是否在允许上传的文件类型中"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # 判断是否有上传的文件
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # 如果文件名为空，返回错误信息
        if file.filename == '':
            return redirect(request.url)
        # 如果上传的文件类型不在允许上传的文件类型中，返回错误信息
        if not allowed_file(file.filename):
            return redirect(request.url)
        # 如果上传的文件符合要求，保存到本地文件系统中
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('upload_file', filename=filename))
    return render_template('upload.html')

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'D:\\Python\\study\\flask_study\\quickstart\\9_fileupload\\uploads'
    app.run(debug=True, host='0.0.0.0', port=8080)
