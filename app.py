from flask import flask

app =Flask(__name__)

@app.route('/')
def home():
    return "hello,Flask!"

if__name__ =='__main__':
    app.run(debug=True)
