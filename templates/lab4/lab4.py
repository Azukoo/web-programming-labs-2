from flask import Blueprint, render_template, request, redirect, session
lab4 = Blueprint('lab4',__name__)


@lab4.route('/lab4')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error = 'Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)
     
    if x2 == 0:
        return render_template('lab4/div.html', error='Ошибка: Деление на ноль невозможно!')
    
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/sum', methods=['POST'])
def sum_op():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    x1 = int(x1) if x1 else 0
    x2 = int(x2) if x2 else 0
    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/multiply-form')
def multiply_form():
    return render_template('lab4/multiply-form.html')

@lab4.route('/lab4/multiply', methods=['POST'])
def multiply_op():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    x1 = int(x1) if x1 else 1
    x2 = int(x2) if x2 else 1
    result = x1 * x2
    return render_template('lab4/multiply.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/subtract-form')
def subtract_form():
    return render_template('lab4/subtract-form.html')

@lab4.route('/lab4/subtract', methods=['POST'])
def subtract_op():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/subtract.html', error='Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('lab4/subtract.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/power-form')
def power_form():
    return render_template('lab4/power-form.html')

@lab4.route('/lab4/power', methods=['POST'])
def power_op():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/power.html', error='Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)
    if x1 == 0 and x2 == 0:
        return render_template('lab4/power.html', error='Ошибка: Оба поля не могут быть равны нулю!')
    
    result = x1 ** x2
    return render_template('lab4/power.html', x1=x1, x2=x2, result=result)

tree_count = 0

@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    if operation == 'cut' and tree_count > 0:
        tree_count -= 1
    elif operation == 'plant' and tree_count < 10:
        tree_count += 1

    return redirect('/lab4/tree')

users = [
    {'login': 'alex', 'password': 'password123', 'name': 'Александр Александров', 'gender': 'male'},
    {'login': 'john9977', 'password': 'qwerty', 'name': 'Иван Иванов', 'gender': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Николай Николаевич', 'gender': 'male'},
    {'login': 'martin', 'password': '222', 'name': 'Андрей Борисов', 'gender': 'male'},
    {'login': 'patric', 'password': '666', 'name': 'Сергей Анатольевич', 'gender': 'male'},
    {'login': 'alic', 'password': '999', 'name': 'Петров Петр', 'gender': 'male'},
]

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
        else:
            authorized = False
            login = ''
        return render_template("lab4/login.html", authorized=authorized, login=login)
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)

    if not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    
    for user in users:
        if login == user['login'] and password == user['password']:
               session['login'] = user['name'] 
               return redirect('/lab4/login')
       
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False)

@lab4.route('/lab4/logout', methods = ['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')