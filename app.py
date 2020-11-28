from flask import Flask, render_template, request, session, redirect, send_file
import requests
import json
app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
@app.route('/')
def hello_world():
    r = requests.get('http://0.0.0.0:5000/keys/tim')
    #print(r.json())
    return render_template('index.html', r = r.json())

@app.route('/upload', methods = ['POST'])
def upload():
    print(request.form)
    doc = request.files['file']
    r = requests.get('/sign/tim', file = doc)
    print(r.json())
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/result')
def download():
    #doc = session['file']
    return send_file('filr.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=8080,host='0.0.0.0')