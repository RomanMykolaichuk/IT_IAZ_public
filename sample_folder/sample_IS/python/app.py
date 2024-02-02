from flask import Flask, request, render_template, redirect, url_for
import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

def get_db_connection():
    connection = psycopg2.connect(
        host='localhost',
        port=5432,
        dbname='sampleis',
        user='postgres',
        password='admin'  # Замініть на свої дані підключення
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=RealDictCursor)

    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()

    cursor.execute('SELECT * FROM tasks order by task_id')
    tasks = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('index.html', categories=categories, tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    connection = get_db_connection()
    cursor = connection.cursor()

    category_id = request.form.get('category_id')
    task_name = request.form.get('task_name')
    task_description = request.form.get('task_description')
    due_date = request.form.get('due_date')

    cursor.execute(
        'INSERT INTO tasks (category_id, task_name, task_description, due_date) VALUES (%s, %s, %s, %s)',
        (category_id, task_name, task_description, due_date)
    )

    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('UPDATE tasks SET completed = true WHERE task_id = %s', (task_id,))
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM tasks WHERE task_id = %s', (task_id,))
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
