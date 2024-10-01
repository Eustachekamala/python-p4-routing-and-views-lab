#!/usr/bin/env python3

from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_route(parameter):
    return parameter

@app.route('/print/hello')
def print_hello():
    print('hello')
    return ('hello')

@app.route('/count/<parameter>')
def count_route(parameter):
    return '\n'.join(str(i) for i in range(int(parameter)))

@app.route('/count/<int:parameter>')
def count_range(parameter):
    output = ""
    for i in range(parameter):
        output += f"{i}\n"
    return output

@app.route('/math/<int:param1>/<op>/<int:param2>')
def math_operation(param1, op, param2):
    if op == "+":
        result = param1 + param2
        return str(result)
    elif op == "-":
        result = param1 - param2
        return str(result)
    elif op == "*":
        result = param1 * param2
        return str(result)
    elif op == "div":
        result = param1 / param2
        return str(result)
    elif op == "%":
        result = param1 % param2
        return str(result)
    else:
        return "Unsupported operation", 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)
