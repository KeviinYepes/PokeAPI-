from flask import Flask , render_template
from database import ApiRequest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',data=ApiRequest())

if __name__ == '__main__':
    app.run(debug=True)