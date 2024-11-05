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

@lab4.route('/lab4/logout', methods = ['GET','POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')

@lab4.route('/lab4/set_temperature', methods=['GET','POST'])
def set_temperature():
    temperature_str = request.form.get('temperature')
    
    # Преобразуем значение в число, если оно задано
    if not temperature_str:
        message = "Ошибка: не задана температура"
    else:
        try:
            temperature = float(temperature_str)  # Преобразование в float
            if temperature < -12:
                message = "Не удалось установить температуру — слишком низкое значение"
            elif temperature > -1:
                message = "Не удалось установить температуру — слишком высокое значение"
            elif -12 <= temperature <= -9:
                message = f"Установлена температура: {temperature}°C ❄️❄️❄️"
            elif -8 <= temperature <= -5:
                message = f"Установлена температура: {temperature}°C ❄️❄️"
            elif -4 <= temperature <= -1:
                message = f"Установлена температура: {temperature}°C ❄️"
        except ValueError:
            message = "Ошибка: температура должна быть числом"

    return render_template('/lab4/temperature.html', message=message)

grain_prices = {
    "barley": 12345,
    "oats": 8522,
    "wheat": 8722,
    "rye": 14111
}

@lab4.route('/order_grain', methods=['GET','POST'])
def order_grain():
    grain_type = request.form.get('grain_type')
    weight = request.form.get('weight')

    if not weight or float(weight) <= 0:
        message = "Ошибка: вес не был указан или указан неверно."
        return render_template('lab4/order_grain.html', message=message)

    weight = float(weight)
    
    if weight > 500:
        message = "Не хватает товара на складе."
    else:
        total_price = grain_prices[grain_type] * weight
        discount_message = ""
        if weight > 50:
            total_price *= 0.9  # скидка 10%
            discount_message = "Применена скидка за большой объём."

        message = f"Заказ успешно сформирован. Вы заказали {weight} т. Сумма к оплате: {total_price:.2f} руб."
        if discount_message:
            message += f" {discount_message}"

    return render_template('lab4/order_result.html', message=message)

@lab4.route('/lab4/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        login = request.form['login']
        password = request.form['password']
        
        # Добавление пользователя в массив
        users.append({
            'name': name,
            'login': login,
            'password': password
        })
        
        return redirect('/lab4/login')
    return render_template('/lab4/register.html')

@lab4.route('/lab4/users')
def users_list():
    if not session.get('authorized', False):
        return redirect('/lab4/login')
    return render_template('lab4/users_list.html', users=users)

@lab4.route('/lab4/delete/<login>', methods=['POST'])
def delete_user(login):
    global users
    users = [user for user in users if user['login'] != login]
    return redirect('/lab4/users')

@lab4.route('/lab4/edit/<login>', methods=['GET'])
def edit_user(login):
    # логика для редактирования пользователя
    pass


