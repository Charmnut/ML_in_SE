from flask import Flask, render_template, send_file, request, session
from main import run_main

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'



@app.route('/', methods=["POST"])
def return_page():
    session['form'] = request.form
    return render_template('result.html')


@app.route('/')
def main():
    """Entry point; the view for the main page"""
    return render_template('main.html')


@app.route('/main.png')
def main_plot():
    """The view for rendering the scatter chart"""
    fs_function = []
    number = int(session['form']['number'])
    method = session['form']['method']
    score_name = session['form']['score']
    if session['form']['pearson'] != '':
        fs_function.append(session['form']['pearson'])
    if session['form']['fisher'] != '':
        fs_function.append(session['form']['fisher'])
    if session['form']['greedy'] != '':
        fs_function.append(session['form']['greedy'])
    img = run_main(method, fs_function, score_name, number)
    return send_file(img, mimetype='image/png', cache_timeout=0)


if __name__ == '__main__':
    app.run()
