from flask import Blueprint, render_template, request, abort, jsonify, make_response

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')


films = [
    {
        "title": "The Substance",
        "title_ru": "Субстанция",
        "year": 2024,
        "description": "Слава голливудской звезды Элизабет Спаркл осталась в прошлом, \
                        хотя она всё ещё ведёт фитнес-шоу на телевидении. Когда её передачу собираются перезапустить \
                        с ведущей помоложе, от отчаяния Элизабет решает принять инновационный препарат, создатели которого обещают невероятное преображение, \
                        но при соблюдении правила одной недели. \
                        Так на свет появляется молодая красотка Сью. Девушка начинает делать карьеру в шоу-бизнесе и вскоре решает, что семи дней ей маловато."
    },
    {
        "title": "Venom: The Last Dance",
        "title_ru": "Веном: Последний танец",
        "year": 2024,
        "description": "Приспособившись к совместному существованию, Эдди и Веном стали друзьями и вместе сражаются со злодеями.\
                        Но теперь за Эдди охотятся военные,\
                        а за Веномом — его инопланетные сородичи, угрожающие всему живому."
    },
    {
        "title": "Home Alone",
        "title_ru": "Один дома",
        "year": 1990,
        "description": "Американское семейство отправляется из Чикаго в Европу, но в спешке сборов бестолковые родители забывают дома...\
                        одного из своих детей. Юное создание, однако, не теряется и демонстрирует чудеса изобретательности. \
                        И когда в дом залезают грабители, им приходится не раз пожалеть о встрече с милым крошкой."
    },
    {
        "title": "The Grinch",
        "title_ru": "Гринч",
        "year": 2018,
        "description": "Любой бы на месте Гринча позеленел и взбесился.\
                        Как порядочный интроверт он живёт в тёмной пещере на самой вершине горы подальше ото всех, но эти «все» готовят грандиознейшее празднование нового года.\
                        Они шумят, всё украшают и дико бесят. Кто бы отказал себе в удовольствии испортить праздник? Гринч решает украсть Новый год."
    },
    {
        "title": "Елки",
        "title_ru": "Елки",
        "year": 2010,
        "description": "Новогодние события происходят в 11 городах: Калининграде, Казани, Перми, Уфе, Бавлах, Екатеринбурге, Красноярске, Якутске, Новосибирске, Санкт-Петербурге и Москве. \
                        Герои фильма — таксист и поп-дива, бизнесмен и актер, сноубордист и лыжник, студент и пенсионерка, пожарный и директриса, вор и милиционер, гастарбайтер и президент России.  \
                        Все они оказываются в самый канун Нового года в очень непростой ситуации, выйти из которой им поможет только чудо… или Теория шести рукопожатий, согласно которой каждый человек на земле знает другого через шесть знакомых."
    },
    {
        "title": "Frozen",
        "title_ru": "Холодное сердце",
        "year": 2013,
        "description": "Когда сбывается древнее предсказание, и королевство погружается в объятия вечной зимы, трое бесстрашных героев - принцесса Анна, \
                        отважный Кристофф и его верный олень Свен - отправляются в горы, чтобы найти сестру Анны, Эльзу, которая может снять со страны леденящее заклятие."
    },

]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films): 
        abort(404)
    return films[id]


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    del films[id]
    return '', 204


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    data = request.get_json()
    title = data.get('title', '').strip()
    title_ru = data.get('title_ru', '').strip()
    year = data.get('year')
    description = data.get('description', '')
    
    if not description:
        return {'description': 'Заполните описание'}, 400
    
    if not title and title_ru:
        title = title_ru

    new_film = {
        "title": title,
        "title_ru": title_ru,
        "year": year,
        "description": description
    }

    films.append(new_film)
    return jsonify(new_film), 201

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def update_film(id):
    if id < 0 or id >= len(films):
        abort(404)

    data = request.get_json()
    
    title = data.get('title', '').strip()
    title_ru = data.get('title_ru', '').strip()
    year = data.get('year', films[id]['year'])  # Сохраняем старое значение, если новое не передано
    description = data.get('description', films[id]['description'])

    if not description:
        return {'description': 'Заполните описание'}, 400
    
    if not title and title_ru:
        title = title_ru

    # Обновляем фильм
    films[id] = {
        "title": title,
        "title_ru": title_ru,
        "year": year,
        "description": description
    }
    return jsonify(films[id])  # Возвращаем обновленный фильм
