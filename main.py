from flask import Flask, render_template, request, jsonify
from botengine import make_reply
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    message = str(request.form['messageText'])
    res = make_reply(message)

    while True:
        if message=="quit":
            exit()
        else:
            return jsonify({'status':'OK','answer':res})
    
if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0',debug='True')