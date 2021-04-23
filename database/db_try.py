import sqlite3
from random import choice
#создаём коннекшн
connection = sqlite3.connect('school.sqlite')
#получаем курсор
cursor = connection.cursor()

#создаём запрос на создание таблички
#раскомментировать для создания
# query = '''
# CREATE TABLE IF NOT EXISTS class (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     surname TEXT,
#     mark INTEGER
# )
# '''

#создаём запрос на добавление данных
#раскомментировать для создания
# query_insert = '''
# INSERT INTO class (name, surname, mark) VALUES
#     ('Дамир', 'Гатауллин', 5),
#     ('Дарья', 'Симакова', 5),
#     ('Иван', 'Ходырев', 3),
#     ('Лев', 'Платонов', 4),
#     ('Арман', 'Авагян', 5),
#     ('Дмитрий', 'Трофимов', 1)
# '''

#создаём запрос на добавление данных
#раскомментировать для создания
# query_insert = '''
# INSERT INTO class (name, surname, mark) VALUES
#     ('{}', '{}', {})
# '''

# pool_names = ('Дамир', 'Дарья', 'Иван', 'Лев', 'Арман', 'Дмитрий')
# pool_surnames = ('Гатауллин', 'Симакова', 'Ходырев', 'Платонов', 'Авагян', 'Трофимов')
# pool_marks = tuple(range(2,6))

# for i in range(100):
#     name = choice(pool_names)
#     surname = choice(pool_surnames)
#     mark = choice(pool_marks)
#     #выполнение запроса
#     query_insert = query_insert.format(name, surname, mark)
#     #print(query_insert)
#     cursor.execute(query_insert)

query = '''
SELECT DISTINCT name, surname, mark FROM class
WHERE surname = 'Платонов'
'''
answer = cursor.execute(query).fetchall()
print(answer)

#сохранение
connection.commit()
#закрытие соединения
connection.close()