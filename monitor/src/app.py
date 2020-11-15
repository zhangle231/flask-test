from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/data.json')
def data():
    result = {}
    result['result'] = 200
    result['categories'] = ["衬衫","羊毛衫","裤子","高跟鞋","袜子"]
    result['data'] = [15,20,36,50,18]
    import time
    time.sleep(1)
    return result;
