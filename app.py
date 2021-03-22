from flask import Flask, request, jsonify, abort, redirect, url_for, flash
from model import load, infer
app = Flask(__name__)

@app.route('/')
def check_is_running():
    return 'Application is running'


@app.route('/badrequest400')
def bad_request():
    return abort(400)


@app.route('/model/test_api_external', methods=['POST'])
def hello_world():
    model = load()
    try:
        content = request.get_json()
        query = content['query']
        # TODO try-except blocks to check that everything is correct
        output = {'answer': infer(model, query)}
        return jsonify(output)
    except:
        return redirect(url_for('bad_request'))


app.run()
