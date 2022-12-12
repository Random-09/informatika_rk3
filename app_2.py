from app_setup import app, render_template
from db_setup import db


@app.route('/task_2/')
def main():
    data = list(db.engine.execute('SELECT * FROM film'))
    return render_template('task_2.html', data=data)


if __name__ == '__main__':
    app.run()