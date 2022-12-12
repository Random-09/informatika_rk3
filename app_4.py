from app_setup import app, render_template, request
from db_setup import db


@app.route('/task_4/')
def main():
    id_request = request.form.get('id')
    if id_request != None:
        print(id_request)
        db.engine.execute(f'DELETE * FROM film WHERE id={id_request}')
    return render_template('task_4.html')


if __name__ == '__main__':
    app.run()