from db_setup import db


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    film_name = db.Column(db.Text, nullable=False)
    film_producer = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    category = db.Column(db.Text, nullable=False)

    @staticmethod
    def add(film_name, film_producer, year, category):
        db.session.add(Film(film_name, film_producer, year, category))
        db.session.commit()
