from app_setup import app, render_template, request
from db_setup import db


@app.route('/task_3/')
def main():
    id_request = request.form.get('id')
    genre_request = request.form.get('category')

    db.engine.execute(f'INSERT {genre_request} INTO films WHERE id={id_request}')

    data = list(db.engine.execute('SELECT * FROM film'))
    return render_template('task_3.html', data=data)


if __name__ == '__main__':
    app.run()