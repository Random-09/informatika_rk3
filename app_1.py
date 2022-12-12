from app_setup import app
from db_setup import db


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run()