from flask import Flask
import math
from flask import request

app = Flask(__name__)

@app.route('/')
def main():
    return """
    Доступные функции: <br>
    1. /add?x=<num>&y=<num> - Сложение <br>
    2. /sub?x=<num>&y=<num> - Вычитание <br>
    3. /mult?x=<num>&y=<num> - Умножение <br>
    4. /div?x=<num>&y=<num> - Деление <br>
    5. /int_div?x=<num>&y=<num> - Целочисленное деление <br>
    6. /mod?x=<num>&y=<num> - Остаток от деления <br>
    7. /pow?x=<num>&y=<num> - Возведение в степень <br>
    8. /sqrt?x=<num> - Квадратный корень <br>
    9. /fact?x=<num> - Факториал <br>
    10. /trig?function=<func>&x=<num>&mode=<mode> - Тригонометрическая функция (func=sin, cos, tan) (mode=.../degress)
    """

@app.route('/add')
def add():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    result = x + y
    return str(result)

@app.route('/sub')
def sub():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    result = x - y
    return str(result)

@app.route('/mult')
def mult():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    result = x * y
    return str(result)

@app.route('/div')
def div():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    if y == 0:
        return 'Нельзя делить на ноль!'
    result = x / y
    return str(result)

@app.route('/int_div')
def int_div():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    if y == 0:
        return 'Нельзя делить на ноль!'
    result = x // y
    return str(result)

@app.route('/mod')
def modulo():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    if y == 0:
        return 'Нельзя делить на ноль!'
    result = x % y
    return str(result)

@app.route('/pow')
def power():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    result = x ** y
    return str(result)

@app.route('/sqrt')
def square_root():
    x = float(request.args.get('x'))
    if x < 0:
        return 'Введите положительный аргумент'
    result = math.sqrt(x)
    return str(result)

@app.route('/fact')
def factorial():
    x = int(request.args.get('x'))
    result = math.factorial(x)
    return str(result)

@app.route('/trig')
def trig():
    function = request.args.get('function')
    x = float(request.args.get('x'))
    mode = request.args.get('mode')
    if mode == 'degrees':
        x = math.radians(x)
    if function == 'sin':
        result = math.sin(x)
    elif function == 'cos':
        result = math.cos(x)
    elif function == 'tan':
        if abs(math.cos(x)) < 1e-10: # Проверка деления на ноль
            return 'Тангенс не существует для данного значения угла'
        result = math.tan(x)
    else:
        return 'Неподдерживаемая тригонометрическая функция'
    return str(result)
