from pprint import pprint

from flask import Flask, render_template, request

from utils import create_db, get_all_films, get_film_by_id, add_film

app = Flask(__name__)
create_db()  # создание БД, если еще не создана


@app.route('/')
def index():
    films_data = get_all_films()
    print(films_data)
    return render_template(
        'index.html', films=films_data
    )


@app.route('/films/<int:film_id>')
def film_page(film_id):
    print(film_id, type(film_id))
    film_data = get_film_by_id(film_id)
    return render_template(
        'film_page.html', film=film_data
    )


@app.route('/add', methods=['GET', 'POST'])
def add_film_page():
    if request.method == 'GET':
        return render_template(
            'add_page.html',
            request_method='GET'  # при значении GET отображается форма
        )
    if request.method == 'POST':
        add_data = request.form.to_dict()
        add_film(add_data)
        return render_template(
            'add_page.html',
            request_method='POST'  # при значении POST отображается сообщение о добавлении
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
