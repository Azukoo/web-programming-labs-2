from flask import Flask, url_for, redirect, render_template
from static.lab1.lab1 import lab1
from static.lab2.lab2 import lab2
from templates.lab3.lab3 import lab3
from templates.lab4.lab4 import lab4

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)

app.secret_key = 'секретно-секретный секрет'

@app.errorhandler(404)
def not_found(err):
    path=url_for("static", filename='/lab2/i.webp')
    return '''
    <!doctype html>
<html>
    <body style="background-color:yellow">
       <h1 style="text-align: center;">Такой страницы не существует!<h1>
       <p style="text-align:center;"><img src="''' + path + '''" width="700" style="padding: 40px;"></p>
    </body>
</html>
''', 404

@app.errorhandler(400)
def not_found400(err):
    return '''
    <!doctype html>
<html>
    <body style="background-color: yellow">
        <h1 style="text-align: center;">Некорректный запрос. Будьте внимательнее!<h1>
    </body>
</html>
''', 400

@app.errorhandler(400)
def er4(e):
  return not_found400(), 400

@app.errorhandler(401)
def not_found401(err):
    return '''
    <!doctype html>
<html>
    <body style="background-color: red">
        <h1 style="text-align: center;">Вы не авторизованы!<h1>
    </body>
</html>
''', 401

@app.errorhandler(403)
def not_found403(err):
    return '''
<!doctype html>
<html>
    <body style="background-color: red">
        <h1 style="text-align: center;">Доступ к ресурсу запрещен!></h1>
    </body>
</html>
''', 403

@app.errorhandler(405)
def not_found405(err):
    return '''
    <!doctype html>
<html>
    <body style="background-color: red">
        <h1 style="text-align: center;">Метод HTTP не разрешен веб-сервером для запрошенного URL-адреса<h1>
    </body>
</html>
''', 405

@app.errorhandler(418)
def not_found418(err):
    return '''
    <!doctype html>
<html>
    <body style="background-color: red">
        <h1 style="text-align: center;">Время ожидания сервером передачи от клиента истекло<h1>
    </body>
</html>
''', 418

@app.errorhandler(500)
def not_found500(err):
    return '''
    <!doctype html>
<html>
    <body style="background-color: blue">
        <h1 style="text-align: center;">Внутренняя ошибка сервера!<h1>
    </body>
</html>
''', 500

@app.route("/")

@app.route("/index")
def index():
    path = url_for("static", filename='lab1.css')
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <link rel="stylesheet" href="''' + path + '''">
</head>
<body>
    <header>
        НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
    </header>

    <main>
        <h1>Лабораторные работы по WEB-программированию</h1>
        <div>
            <ol>
                <li>
                    <a href="/lab1">Лабораторная работа 1</a>
                </li>
                <li>
                    <a href="/lab2">Лабораторная работа 2</a>
                </li>
                <li>
                    <a href="/lab3">Лабораторная работа 3</a>
                </li>
                <li>
                    <a href="/lab4">Лабораторная работа 4</a>
                </li>
            </ol>
        </div>
    </main>

    <footer>
        <hr>
        &copy; Санданова Виктория, ФБИ-22, 3 курс, 2024
    </footer>
</body>
</html>
'''


