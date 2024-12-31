from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return jsonify(message="You are welcome!")

if __name__ == '__main__':
    app.run(host="52.91.51.113", port=5000)
