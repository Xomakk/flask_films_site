import sqlite3


def create_db():
    """
        Создает базу данных и таблицы, если они еще не существуют.
    """
    con = sqlite3.connect("data.db")

    SQL_CREATE = """
    CREATE TABLE IF NOT EXISTS films (
      id INTEGER PRIMARY KEY,
      name STRING,
      rating REAL,
      description TEXT,
      year INTEGER,
      poster_url TEXT, 
      genres TEXT,
      country TEXT,
      movieLength INTEGER,
      shortDescription TEXT,
      ageRating INTEGER,
      trailer_url TEXT
    )
    """
    con.execute(SQL_CREATE)


def get_all_films():
    """
    Получает из БД id, название, URL постера и короткое описание для каждого фильма.
    Возвращает список фильмов в виде словарей
    """
    con = sqlite3.connect("data.db")

    SQL_SELECT = """
        SELECT id, name, poster_url, shortDescription FROM films
    """
    query = con.execute(SQL_SELECT)
    row_data = query.fetchall()

    data = []
    for row in row_data:
        film = {}
        film["id"] = row[0]
        film["name"] = row[1]
        film["poster_url"] = row[2]
        film["shortDescription"] = row[3]
        data.append(film)
    return data


def get_film_by_id(id):
    """
    Поиск фильма в БД по его ID.
    Функция возвращает полную информацию о фильме в виде словаря.
    """
    con = sqlite3.connect("data.db")

    SQL_SELECT = f"""
        SELECT * FROM films WHERE id = {id}
    """
    query = con.execute(SQL_SELECT)
    row_data = query.fetchone()

    data = {
        "id": row_data[0],
        "name": row_data[1],
        "rating": row_data[2],
        "description": row_data[3],
        "year": row_data[4],
        "poster_url": row_data[5],
        "genres": row_data[6],
        "country": row_data[7],
        "movieLength": row_data[8],
        "shortDescription": row_data[9],
        "ageRating": row_data[10],
        "trailer_url": row_data[11],
    }
    return data


def add_film(data):
    """
    Принимает данные фильм и добавляет его в БД.
    """
    name = data["name"]
    rating = data["rating"]
    description = data["description"]
    year = data["year"]
    poster_url = data["poster_url"]
    genres = data["genres"]
    country = data["country"]
    movieLength = data["movieLength"]
    shortDescription = data["shortDescription"]
    ageRating = data["ageRating"]
    trailer_url = data["trailer_url"]

    con = sqlite3.connect("data.db")

    SQL_INSERT = f"""
        INSERT INTO films(name, rating, description, year, poster_url, genres, country, movieLength, shortDescription, ageRating, trailer_url)
        VALUES ('{name}',{rating},'{description}',{year},'{poster_url}','{genres}','{country}',{movieLength},'{shortDescription}',{ageRating},'{trailer_url}')
    """

    con.execute(SQL_INSERT)
    con.commit()
