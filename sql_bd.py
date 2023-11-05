import sqlite3

# создание соединения
connection = sqlite3.connect('Feat.db') # подключение к бд, если нет - создание
cursor = connection.cursor() # объект для отправки запросов

# создание таблицы Роли
cursor.execute('''
CREATE TABLE IF NOT EXISTS Role(
    id_role INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT);''')

# создание таблицы Пользователь
# enabled - в сети/не в сети, принимает значения 0 и 1
cursor.execute('''
CREATE TABLE IF NOT EXISTS User(
    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    nickname TEXT,
    discription TEXT,
    enabled INTEGER,
    birthday TEXT,
    registration_date TEXT, 
    id_role INTEGER,
               
    FOREIGN KEY (id_role) REFERENCES Role (id_role)
);''')

# создание таблицы Посты
cursor.execute('''
CREATE TABLE IF NOT EXISTS Post(
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT, 
    date TEXT,
    time TEXT,
    id_user INTEGER,

    FOREIGN KEY (id_user) REFERENCES User (id_user)
);''')

# создание таблицы Сообщения
cursor.execute('''
CREATE TABLE IF NOT EXISTS Messages(
    id_message INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT, 
    date TEXT,
    time TEXT,
    id_user_from INTEGER,
    id_user_to INTEGER,

    FOREIGN KEY (id_user_from) REFERENCES User (id_user),
    FOREIGN KEY (id_user_to) REFERENCES User (id_user)
);''')

# создание таблицы Подписки
cursor.execute('''
CREATE TABLE IF NOT EXISTS Following(
    id_user INTEGER,
    id_user_followed INTEGER,
    
    FOREIGN KEY (id_user) REFERENCES User (id_user),
    FOREIGN KEY (id_user_followed) REFERENCES User (id_user),
               
    CONSTRAINT new_pk PRIMARY KEY (id_user, id_user_followed)
);''')
# PK задается отдельно, чтобы уникальность смотрелась по паре

connection.commit() # сохранение

# Добавление данных
role = [('Admin', ), ('Technical support', ), ('Member', )]
user = [('Polina', 'Kobtseva', 'FEATPRESIDENT', 'лучший босс эвер', 0, '25.10.2006', '12.01.1023', 1, ), ('Tatiana', 'Taekina', 'FEATVICEPRESIDENT', 'лучший аналитик эвер', 1, '03.06.2006', '12.01.1023', 1, )]
post = [('НОВЫЙ ДРОП', "бегом лайкать!!!", "05.11.2023", "13:23", 1, ), ('Добавили подписки!', "169 руб/мес", "10.09.2023", "9:00", 2, )]
message = [('го запишем feat?', "05.11.2023", '14:00', 2, 1, ), ('го', "05.11.2023", '14:01', 1, 2, )]
following = [(1, 2, ), (2, 1, )]
# !!! тут по паре штук добавить надо
cursor.executemany("INSERT INTO Role (name) VALUES (?);", role)
cursor.executemany("INSERT INTO User (first_name, last_name, nickname, discription, enabled, birthday, registration_date, id_role) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", user)
cursor.executemany("INSERT INTO Post (title, content, date, time, id_user) VALUES (?, ?, ?, ?, ?);", post)
cursor.executemany("INSERT INTO Messages (content, date, time, id_user_from, id_user_to) VALUES (?, ?, ?, ?, ?);", message)
cursor.executemany("INSERT OR IGNORE INTO Following (id_user, id_user_followed) VALUES (?, ?);", following)


connection.commit()

# Выборка данных
cursor.execute('SELECT * FROM User')
# получить и вывести
rows = cursor.fetchall()

for row in rows:
    print(row)

# Обновление данных
user_update = (1, 'lalalal', ) # тут важно что с новым id, или что указано в WHERE
cursor.execute('''
    UPDATE User 
    SET discription = ? WHERE id_user = ?''',
    user_update)

connection.commit()

# Удаление данных
user_id = 2
cursor.execute('DELETE FROM User WHERE id_user = ?', (user_id, )) # (,) - для кортежа

connection.commit()



