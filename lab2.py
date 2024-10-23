from flask import Blueprint, url_for, redirect, render_template
lab2 = Blueprint('lab2',__name__)


@lab2.route('/lab2/a')
def a():
    return 'без слэша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']


@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return (""" <h1> Упс! Такого цветка нет :(" </h1>
                <a href="/lab2/flowers">Вернуться к списку цветов</a>
                """), 404
    else:
        return (f""" <h1> Цветок: {flower_list[flower_id]} </h1>
    <a href="/lab2/flowers">Вернуться к списку цветов</a>
""")
    

@lab2.route('/lab2/add_flower/', 
           defaults={'name': None})


@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    if not name:  # Проверка, что имя цветка не пустое
        return "Упс! Вы не задали имя цветка :(", 400
    else:
        flower_list.lab2end(name)  # Добавление имени в список
        return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1> 
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    <p><a href="{url_for('get_flowers')}">Посмотреть все цветы</a></p>
    </body>
</html>
'''  


@lab2.route('/lab2/flowers')
def get_flowers():
    return f''' 
<!doctype html>
<html>
    <body>
    <h1>Список всех цветов</h1>
            {"".join(f"<li><a href='/lab2/flowers/{i}'>{flower}</a></li>" for i, flower in enumerate(flower_list))}
    </ul>
    <p>Всего цветов: {len(flower_list)}</p>
    <p><a href="{url_for('clear_flowers')}">Очистить список цветов</a></p>
    </body>
</html>
'''


@lab2.route('/lab2/example')
def example():
    name ,group, course, lab_num = 'Санданова Виктория', 'ФБИ-22', '3 Курс', 'Лабораторная работа 2' 
    fruits = [
        {'name': 'яблоки', 'price': 100}, 
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95}, 
        {'name': 'манго','price': 321} 
    ]

    return render_template('example.html', 
                           name=name, group=group, 
                           course=course,lab_num=lab_num, fruits=fruits)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')
   

@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)


@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()  # Очистка списка цветов
    return '''<h1>Список цветов очищен!</h1>
              <a href="/lab2/flowers">Вернуться к списку цветов</a>'''


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    results = {
        'sum': a + b,
        'difference': a - b,
        'product': a * b,
        'quotient': "Ошибка: деление на ноль" if b == 0 else a / b,
        'power': a ** b
    }
    return results


@lab2.route('/lab2/calc/')
def default_calc():
    # Перенаправление на /lab2/calc/1/1
    return redirect(url_for('calc', a=1, b=1))


@lab2.route('/lab2/calc/<int:a>')
def redirect_to_default_b(a):
    # Перенаправление на /lab2/calc/a/1
    return redirect(url_for('calc', a=a, b=1))

books = [
    {"title": "1984", "author": "Джордж Оруэлл", "genre": "Дистопия", "pages": 328},
    {"title": "Война и мир", "author": "Лев Толстой", "genre": "Исторический роман", "pages": 1225},
    {"title": "Гарри Поттер и философский камень", "author": "Джоан Роулинг", "genre": "Фэнтези", "pages": 223},
    {"title": "Убить пересмешника", "author": "Харпер Ли", "genre": "Драма", "pages": 281},
    {"title": "Мастер и Маргарита", "author": "Михаил Булгаков", "genre": "Роман", "pages": 384},
    {"title": "Преступление и наказание", "author": "Фёдор Достоевский", "genre": "Роман", "pages": 430},
    {"title": "Три товарища", "author": "Эрих Мария Ремарк", "genre": "Роман", "pages": 360},
    {"title": "451 градус по Фаренгейту", "author": "Рэй Брэдбери", "genre": "Научная фантастика", "pages": 158},
    {"title": "Собачье сердце", "author": "Михаил Булгаков", "genre": "Сатира", "pages": 150},
    {"title": "Анна Каренина", "author": "Лев Толстой", "genre": "Роман", "pages": 864}
]


@lab2.route('/lab2/books')
def show_books():
    return render_template('books.html', books=books)

items = [
    {
        "name": "Клубника",
        "description": "Сладкая и сочная ягода, популярная в летнее время.",
        "image": "/static/berry.jpg"
    },
    {
        "name": "Спортивная машина",
        "description": "Быстрая и мощная машина для любителей скорости.",
        "image": "/static/car.jpg"
    },
    {
        "name": "Леопард",
        "description": "Милое животное, известное своей независимостью.",
        "image": "/static/cat.jpg"
    },
    {
        "name": "Стул",
        "description": "Основной элемент мебели для сидения.",
        "image": "/static/chair.jpg"
    },
    {
        "name": "Стол",
        "description": "Мебель для работы или приема пищи.",
        "image": "/static/table.jpg"
    },
]


@lab2.route('/lab2/items')
def show_items():
    return render_template('items.html', items=items)


