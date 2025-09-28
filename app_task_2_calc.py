from flask import Flask

app = Flask(__name__)

@app.route('/calc/<num1>/<num2>')
def calc(num1, num2):
    try:
        num1, num2 = int(num1), int(num2)
    except ValueError:
        return "Ошибка: нужно вводить только целые числа!"

    sum_number = num1 + num2
    return f"The sum of {num1} and {num2} is {sum_number}."


if __name__ == "__main__":
    app.run(debug=True)