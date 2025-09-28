from flask import Flask

app = Flask(__name__)

@app.route('/user/<name>/<age>')
def user(name, age):
    try:
        age_num = int(age)
    except ValueError:
        return "Ошибка: возраст должен быть целым числом!"
    if age_num < 0:
        return "Ошибка: возраст не меньше 0"
    return f"Hello, {name}. You are {age_num} years old."


if __name__ == "__main__":
    app.run(debug=True)