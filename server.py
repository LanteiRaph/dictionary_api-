
from flask import Flask
from flask import jsonify

from app import translate
from flask_cors import CORS

#Create a new flas app
app = Flask(__name__)
CORS(app,resource={r"/*":{"origins":"*"}})


#main Route: returns a messge to the user
@app.route('/', methods=['GET', 'POST'])
def welcome():
    return jsonify({"msg":"Welcome to our Dictonary plaese vist our site to access the api"})


@app.route('/search/<string:word>/', methods=['GET', 'POST'])
def meaning(word):

    #translate the given wrd to its meaning
    output = translate(word)
    #respond back to the user with the given data.
    return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)