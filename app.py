from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    path=url_for("static", filename='i.webp')
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
@app.route("/lab1")
def lab1():
    path = url_for("static", filename='lab1.css')
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Лабораторная 1</title>
    <link rel="stylesheet" href="''' + path + '''">
</head>
<body>
    <header>
        НГТУ, ФБ, WEB-программирование, часть 2.
    </header>

    <main>
        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>

        <a href="/">Ссылка на меню</a>
        <h2>Список роутов</h2>

        <ol>
            <li>
                <a href="/lab1/web">web</a>
            </li>

            <li>
                <a href="/lab1/oak">Дуб</a>
            </li>

            <li>
                <a href="/lab1/author">Автор</a>
            </li>

            <li>
                <a href="/lab1/counter">Счетчик</a>
            </li>
 
            <li>
                <a href="/lab1/info">Роут info</a>
            </li>
            <li>
                <a href="/lab1/cont">Content Language</a>
            </li>

            <li>
                <a href="/lab1/err5">Ошибка 505</a>
            </li>
        </ol>
    </main>

    <footer>
        <hr>
        &copy; Санданова Виктория,ФБИ-22,3 курс,2024
    </footer>
</body>
</html>
'''

@app.route("/lab1/web")
def web():
    return """<!doctype html> \
        <html> \
            <body> \
                <h1>web-сервер на flask</h1> \
            </body> \
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
            }

@app.route("/lab1/author")
def author():
    name = "Санданова Виктория Болотовна"
    group = "ФБИ-22"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """+name+"""</p>
                <p>Группа: """+group+"""</p>
                <p>Факультет: """+faculty+"""</p>
                <a href="/web">web</a>
            </body>
        </html>"""

@app.route('/lab1/oak')
def oak():
    path = url_for("static", filename="oak.jpg")
    path2 = url_for("static", filename='lab1.css')
    return '''
<!doctype html>
<html>
    <head>
    <link rel="stylesheet" href="''' + path2 + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' +path+ '''">
    </body>
</html>
'''

count = 0 

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + ''' 
        <a href="/lab1/counter0">очистка</a>
    </body>
</html>
'''
count2 = 0
@app.route('/lab1/counter0')
def counter0():
    global count2
    count2 += 1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: '''+ str(count2) +'''
        <a href="/lab1">в список</a>
    </body>
</html>
'''

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i><div>
    </body>
</html>
''', 201

@app.route("/lab1/cont")
def cont():
    path = url_for("static", filename='lab1.css')
    return '''
<!DOCTYPE html>
<html lang="de, en, ru">
<head>
    <meta charset="UTF-8">
    <title>Лабораторная 1</title>
    <link rel="stylesheet" href="''' + path + '''">
</head>
<body>
    <header>
        НГТУ, ФБ, WEB-программирование, часть 2.
    </header>
    <main>
        <h2>Дисконт как учёт векселей</h2>
        <p>
            Учёт <s>векселей</s>, также называемый <b>дисконтом</b>, — это покупка переводных <s>векселей</s>, казначейских <s>векселей</s> или 
            облигаций по <u><i><b>цене</b></i></u> ниже номинальной. <s>Векселя</s> и облигации погашаются в определённый момент в будущем по своей 
            номинальной стоимости. Покупатель, который приобретает <s>вексель</s> или облигацию в момент выпуска, платит за них 
            меньше номинальной, или лицевой, стоимости (с <b>дисконтом</b>). Разница (<b>дисконт</b>) между <u><i><b>ценой</b></i></u>, по которой он покупает
            <s>вексель</s> или облигацию, и их номинальной стоимостью представляет собой <u>процент</u> по займу, предоставленному под 
            обеспечение <s>векселем</s> или облигацией. Если владелец <s>векселя</s> или облигации захочет затем продать их до истечения 
            срока их действия (редисконтировать, переучесть их), он сможет получить за них сумму, меньшую, чем номинальная 
            стоимость, хотя и бо́льшую, чем та, что была за них заплачена. Разница между исходной <u><i><b>ценой</b></i></u>, заплаченной им, и 
            полученной суммой зависит главным образом от того, сколько времени осталось до истечения срока действия данной 
            ценной бумаги. Например, если облигация с номинальной стоимостью 1000 и сроком действия один год была приобретена 
            за 900, то <b>дисконт</b> по стоимости погашения соответствует <u>процентной</u> ставке: (1000-900)/900=11,1% по займу.
        </p>
        <h2>Дисконт на валютном рынке</h2>
        <p>
            <b>Дисконтом</b> на валютном рынке называют <i>скидку</i> (вычет) с курса валюты по наличным, кассовым операциям, 
            если предполагается,что её курс будет понижаться между датами заключения и исполнения сделки. Здесь 
            противоположным понятием является премия — когда при сделке на срок валюта котируется дороже,чем по 
            наличным сделкам<sup>[1]</sup>.
        </p>
        <h2>Дисконт на фондовом рынке</h2>
        <p>
            На фондовом рынке под <b>дисконтом</b> понимают <i>скидку</i> в <u>процентах</u> с номинальной стоимости ценной бумаги. 
            Например, если облигацию с номиналом 1000 $ продают за 900 $, <b>дисконт</b> составляет 10%. <b>Дисконтом</b> 
            также называют разницу между <u><i><b>ценой</b></i></u> ценной бумаги при её реализации и при погашении<sup>[1]</sup>.
        </p>
        <h2>Дисконт в денежном обращении</h2>
        <p>
            В денежном обращении <b>дисконтом</b> называют обесценивание одних видов денег по отношению к другим, 
            параллельно обращающимся (например, бумажных денег по отношению к золотым монетам)<sup>[1]</sup>.
        </p>
    </main>

    <footer>
        <hr>
        &copy; Санданова Виктория, ФБИ-22, 3 курс, 2024
    </footer>
</body>
</html>
'''

a=33
b=0
@app.route('/lab1/err5')
def err5():
    c = a/b
    return '''
<!doctype html>
<html>
    <body>
        Равно: '''+ str(c) +'''
    </body>
</html>
'''
@app.route('/lab2/a')
def a():
    return 'без слэша'


@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

