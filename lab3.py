from flask import Blueprint, url_for, redirect, render_template, request, make_response
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', 'Аноним')
    name_color = request.cookies.get('name_color')
    age = request.cookies.get('age', 'неизвестный')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)

@lab3.route('/lab3/cookie/')
def cookie():
    resp = make_response(redirect('/lab3/'))  
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp

@lab3.route('/lab3/del_cookie/')
def del_cookie():
    resp = make_response(redirect('/lab3/'))  
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/lab3/form1/')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else: 
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    size = request.args.get('size')
    backgroundСolor = request.args.get('backgroundСolor')
    if color: 
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('color', color)
    if size:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('size', size)
    if backgroundСolor:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('backgroundСolor', backgroundСolor)
   

    color = request.cookies.get('color')
    size = request.cookies.get('size', '16px')
    backgroundColor = request.cookies.get('backgroundColor')
    resp = make_response(render_template('lab3/settings.html', color=color, size=size, backgroundColor=backgroundColor))
    return resp

