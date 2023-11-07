# Put your app in here.
from flask import Flask, request
from operations import add, sub , mult, div

app = Flask(__name__)

operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<calc>')
def calc(calc):
    operation = operators[calc]
    answer = operation(int(request.args['a']), int(request.args['b']))
    return f'{answer}'




# @app.route('/add')
# def add_terms():
#     terms = request.args
#     answer = add(int(terms['a']), int(terms['b']))
#     return f'{answer}'

# @app.route('/sub')
# def sub_terms():
#     terms = request.args
#     answer = sub(int(terms['a']), int(terms['b']))
#     return f'{answer}'

# @app.route('/mult')
# def mult_terms():
#     terms = request.args
#     answer = mult(int(terms['a']), int(terms['b']))
#     return f'{answer}'

# @app.route('/div')
# def div_terms():
#     terms = request.args
#     answer = div(int(terms['a']), int(terms['b']))
#     return f'{answer}'
    

