import os
from flask import Flask, render_template, url_for, request, flash, send_file


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'sounds'
app.secret_key = 'some_secret'


def get_sounds() -> list:
    path = 'sounds'
    files = os.listdir(path)
    return files


def allowed_file(file_name):
    allowed = set(['mp3', 'ogg', 'wav'])
    return '.' in file_name and \
        file_name.rsplit('.', 1)[1].lower() in allowed


@app.route('/sounds/<name>')
def sounds(name):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], name))


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        else:
            flash('Non-audio file detected')
    if request.method == 'GET':
        command = request.args.get('command')
        if command == 'list':
            return get_sounds()
        elif command == 'upload':
            print('upload')
    sounds = get_sounds()
    url = list()
    for name in sounds:
        url.append(url_for('sounds', name=name))
    sounds_url = zip(sounds, url)
    return render_template('index.html', pair=sounds_url)


if __name__ == '__main__':
    app.run(port=8888)
