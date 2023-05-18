from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Данные пользователей и сообщения
users = []
messages = []

# Главная страница с формой ввода имени пользователя
@app.route('/')
def index():
    return render_template('index.html')

# Обработка отправки формы с именем пользователя
@app.route('/join', methods=['POST'])
def join():
    username = request.form['username']
    # Добавляем пользователя в список
    users.append(username)
    # Редирект на страницу с чатом
    return redirect(url_for('chat', username=username))

# Страница с чатом
@app.route('/chat')
def chat():
    username = request.args.get('username')
    if username is None:
        # Если имя пользователя не указано, редирект на главную страницу
        return redirect(url_for('index'))
    else:
        return render_template('chat.html', username=username, messages=messages)

# Обработка отправки сообщения
@app.route('/send_message', methods=['POST'])
def send_message():
    username = request.form['username']
    message = request.form['message']
    messages.append((username, message))
    # Редирект на страницу с чатом
    return redirect(url_for('chat', username=username))

if __name__ == '__main__':
    # Генерируем случайный секретный ключ
    app.secret_key = os.urandom(24)
    app.run(debug=True)
