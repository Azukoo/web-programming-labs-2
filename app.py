from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/web")
@app.route("/author")
def web():
    return """<!doctype html> 
        <html> 
            <body>
                <h1>web-сервер на flask</h1>
            </body>
        </html>"""

@app.route("/author")
def author():
    name = "Санданова Виктория Болотовна"
    group = "ФБИ-22"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/web">web</a>
            </body>
        </html>"""
