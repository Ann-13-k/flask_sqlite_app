from flask import Flask

app = Flask(__name__)

@app.route('/info')
def info():
    return "This is an informational page."

if __name__ == "__main__":
    app.run(debug=True)