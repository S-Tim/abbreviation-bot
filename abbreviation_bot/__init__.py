import os
from flask import Flask, request, abort
from . import abbreviation

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'dev_key')

def verified(func):
    def verify_and_execute(*args, **kwargs):
        if request.form['token'] != os.environ.get('VERIFICATION_TOKEN'):
            abort(401)

        func(*args, **kwargs)

    return verify_and_execute

@app.route("/")
def hello():
    return ("Hello this is the abbreviation bot! Try /abbreviation if "
            "you want to know what an abbreviation means.")


@verified
@app.route("/abbreviation", methods=['POST'])
def get_abbreviation():
    if request.form['text'] == "":
        return abbreviation.find_all()
    else:
        return abbreviation.find(request.form['text'])
