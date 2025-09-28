from flask import Flask

app = Flask(__name__)

@app.route('/reverse/')
@app.route('/reverse/<word>')
def reverse(word=""):
    if not word.strip():
        return "Ошибка: Строка пуста!"
    else:
        reverse_word = "".join(reversed(word))
    return f"{reverse_word}"


if __name__ == "__main__":
    app.run(debug=True)